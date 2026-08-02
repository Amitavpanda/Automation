#!/usr/bin/env python3
# /// script
# dependencies = ["fastapi", "uvicorn"]
# ///
"""GCF Hermes Dashboard — FastAPI backend with run actions"""

import json
import os
import subprocess
import threading
import time
from datetime import datetime
from pathlib import Path

from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse
import uvicorn

app = FastAPI(title="GCF Hermes Dashboard")

BASE = Path(os.path.expanduser("~/Desktop/projects/Automation/getcodefree"))
HERMES = Path(os.path.expanduser("~/.hermes"))
HERMES_BIN = HERMES / "hermes-agent" / "venv" / "bin" / "hermes"
RUN_LOG = Path("/tmp/gcf-hermes-runs.json")

runs = []  # [(timestamp, skill, status, output_preview), ...]
running_skills = {}  # {name: start_time_iso}


def log_run(skill, status, output=""):
    runs.insert(0, (datetime.now().isoformat(), skill, status, output[:500]))
    runs[:] = runs[:50]
    try:
        with open(RUN_LOG, "w") as f:
            json.dump(runs, f)
    except:
        pass


def run_hermes(args, timeout=60):
    try:
        env = os.environ.copy()
        venv_bin = str(HERMES / "hermes-agent" / "venv" / "bin")
        env["PATH"] = f"{venv_bin}:{env.get('PATH', '')}"
        r = subprocess.run(
            [str(HERMES_BIN), *args],
            capture_output=True, text=True, timeout=timeout, env=env
        )
        return r.stdout + "\n" + r.stderr if r.stderr else r.stdout
    except subprocess.TimeoutExpired:
        return "error: timed out after 60s"
    except Exception as e:
        return f"error: {e}"


def read_json(path):
    try:
        with open(path) as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return None


def read_dir(path, ext=None):
    p = Path(path)
    if not p.exists():
        return []
    files = [f for f in p.iterdir() if f.is_file()]
    if ext:
        files = [f for f in files if f.suffix == ext]
    return sorted(files, key=lambda f: f.stat().st_mtime, reverse=True)


# ── API endpoints ──────────────────────────────────────────────────


@app.get("/api/pipeline")
def get_pipeline():
    inbox = read_dir(BASE / "leads" / "inbox", ".json")
    hot, warm, cold = [], [], []
    for f in inbox:
        d = read_json(f)
        leads_data = []
        if isinstance(d, list):
            leads_data = d
        elif isinstance(d, dict) and "items" in d:
            leads_data = d["items"]
        elif isinstance(d, dict) and "leads" in d:
            leads_data = d["leads"]
        for lead in leads_data:
            if not isinstance(lead, dict):
                continue
            entry = {
                "name": lead.get("name", "Unknown"),
                "company": lead.get("company", ""),
                "score": lead.get("score", 0),
                "signal": lead.get("signal") or lead.get("signal_text", ""),
                "source": lead.get("source_url") or lead.get("source", ""),
            }
            s = lead.get("score", 0)
            if not isinstance(s, (int, float)):
                try: s = int(s)
                except: s = 0
            if s >= 9: hot.append(entry)
            elif s >= 7: warm.append(entry)
            else: cold.append(entry)

    pipeline = read_json(BASE / "outreach" / "pipeline.json") or {}
    pipeline_leads = pipeline.get("leads", [])

    sent = sum(1 for l in pipeline_leads if l.get("status") == "sent")
    replied = sum(1 for l in pipeline_leads if l.get("status") == "replied")
    drafts = read_dir(BASE / "outreach" / "drafts", ".md")

    return {
        "hot": hot, "warm": warm, "cold": cold,
        "total_leads": len(inbox),
        "in_pipeline": len(pipeline_leads),
        "sent": sent, "replied": replied,
        "drafts": [d.name for d in drafts[:10]],
        "pipeline": pipeline_leads[-10:],
    }


@app.get("/api/skills")
def get_skills():
    skills_dir = BASE / "hermes" / "skills"
    skills = []
    for d in skills_dir.iterdir():
        if d.is_dir():
            skill_file = d / "SKILL.md"
            if skill_file.exists():
                with open(skill_file) as f:
                    content = f.read()
                skills.append({"name": d.name, "description": content[:200] + "..."})
    return {"skills": skills}


@app.get("/api/cron")
def get_cron():
    out = run_hermes(["cron", "list"], timeout=10)
    jobs_file = HERMES / "cron" / "jobs.json"
    jobs = []
    if jobs_file.exists():
        try:
            with open(jobs_file) as f:
                data = json.load(f)
            if isinstance(data, list):
                jobs = data
            elif isinstance(data, dict):
                jobs = [{"name": k, **v} for k, v in data.items()]
        except:
            pass
    return {"raw_output": out, "jobs": jobs[:20] if isinstance(jobs, list) else []}


@app.get("/api/status")
def get_status():
    out = run_hermes(["doctor"], timeout=15)
    return {"doctor": out}


@app.get("/api/reports")
def get_reports():
    reports_dir = BASE / "hermes" / "reports"
    files = read_dir(reports_dir, ".md")
    reports = []
    for f in files:
        try:
            with open(f) as fh:
                reports.append({"name": f.name, "content": fh.read()[:500]})
        except:
            pass
    return {"reports": reports}


@app.get("/api/runs")
def get_runs():
    try:
        with open(RUN_LOG) as f:
            saved = json.load(f)
        return {"runs": (runs + saved)[:30], "running": running_skills}
    except:
        return {"runs": runs[:30], "running": running_skills}


@app.post("/api/run/skill/{name}")
def trigger_skill(name: str):
    skill_dir = BASE / "hermes" / "skills" / name
    if not skill_dir.exists():
        return {"status": "error", "message": f"Skill '{name}' not found"}

    skill_file = skill_dir / "SKILL.md"
    if not skill_file.exists():
        return {"status": "error", "message": f"SKILL.md not found in {name}"}

    with open(skill_file) as f:
        first_line = f.readline().strip()
        prompt_line = f.readline().strip() if first_line.startswith("---") else first_line

    prompt = ""
    if name == "gcf-lead-scraper":
        prompt = "Generate 3 realistic sample leads for GetCodeFree agency. Each lead: name, company, role, signal text, score (7-10). Skip browser actions. Write results to /Users/amitavpanda/Desktop/projects/Automation/getcodefree/leads/inbox/ as JSON."
    elif name == "gcf-content-drafter":
        prompt = "Read leads from /Users/amitavpanda/Desktop/projects/Automation/getcodefree/leads/inbox/. Pick top scored lead. Draft short personalized outreach message. Write to /Users/amitavpanda/Desktop/projects/Automation/getcodefree/outreach/drafts/ as markdown file. Do not send."
    elif name == "gcf-outreach":
        prompt = "Read pipeline.json, check for leads needing follow-up. Do not send anything. Just report what needs action."
    elif name == "gcf-pipeline-view":
        prompt = "Read lead files in /Users/amitavpanda/Desktop/projects/Automation/getcodefree/leads/inbox/ and /Users/amitavpanda/Desktop/projects/Automation/getcodefree/outreach/pipeline.json. Produce short summary report. Save to /Users/amitavpanda/Desktop/projects/Automation/getcodefree/hermes/reports/ as markdown."

    running_skills[name] = datetime.now().isoformat()

    def run():
        log_run(name, "running", "Started...")
        try:
            out = run_hermes(
                ["-z", prompt],
                timeout=120
            )
            status = "done" if "error" not in out[:20].lower() else "failed"
        except Exception as e:
            out = f"error: {e}"
            status = "failed"
        log_run(name, status, out)
        running_skills.pop(name, None)
        print(f"[GCF] Skill '{name}' → {status}")

    threading.Thread(target=run, daemon=True).start()
    return {"status": "started", "skill": name, "message": f"Running {name}..."}


@app.post("/api/setup/cron")
def setup_cron():
    """Schedule the 3 daily GCF cron jobs"""
    jobs = [
        ("0 7 * * *", "gcf-daily-leads", "gcf-lead-scraper",
         "Scrape X/Twitter and LinkedIn for founder leads. Score each 1-10. Write to leads/inbox/."),
        ("30 8 * * *", "gcf-daily-drafts", "gcf-content-drafter",
         "Read inbox/ for leads scored 7+. Draft personalized outreach. Write to outreach/drafts/."),
        ("0 17 * * *", "gcf-evening-report", "gcf-pipeline-view",
         "Read all lead data and pipeline state. Produce summary report. Save to hermes/reports/."),
    ]

    results = []
    for schedule, name, skill, prompt in jobs:
        out = run_hermes(["cron", "create", schedule, prompt,
                         "--skill", skill, "--name", name],
                         timeout=30)
        results.append({"name": name, "output": out})
    return {"status": "done", "results": results}


@app.get("/api/config")
def get_config():
    cfg_file = HERMES / "config.yaml"
    env_file = HERMES / ".env"
    config_text = ""
    env_text = ""
    try:
        with open(cfg_file) as f:
            config_text = f.read()
    except: pass
    try:
        with open(env_file) as f:
            env_text = "\n".join(
                l for l in f.read().splitlines()
                if not l.startswith("OPENROUTER_API_KEY")
            )
    except: pass
    return {"config": config_text, "env": env_text}


# ── Dashboard HTML ─────────────────────────────────────────────────


DASHBOARD_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>GCF · Hermes Dashboard</title>
<style>
  :root { --bg: #0d1117; --card: #161b22; --border: #30363d; --text: #c9d1d9; --muted: #8b949e; --accent: #58a6ff; --green: #3fb950; --orange: #d29922; --red: #f85149; --yellow: #d29922; font-family: -apple-system,BlinkMacSystemFont,'Segoe UI',monospace; }
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body { background: var(--bg); color: var(--text); padding: 20px; }
  .header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 24px; padding-bottom: 16px; border-bottom: 1px solid var(--border); }
  .header h1 { font-size: 20px; display: flex; align-items: center; gap: 10px; }
  .status-dot { display: inline-block; width: 10px; height: 10px; border-radius: 50%; flex-shrink: 0; }
  .status-dot.idle { background: var(--green); }
  .status-dot.running { background: var(--yellow); animation: pulse 1s infinite; }
  .status-dot.error { background: var(--red); }
  .running-banner { background: #1a3a2a; border: 1px solid var(--green); border-radius: 8px; padding: 10px 16px; margin-bottom: 16px; display: flex; align-items: center; gap: 10px; font-size: 13px; }
  .running-banner .spinner { width: 14px; height: 14px; border: 2px solid var(--green); border-top-color: transparent; border-radius: 50%; animation: spin 0.8s linear infinite; flex-shrink: 0; }
  @keyframes spin { to { transform: rotate(360deg); } }
  @keyframes pulse { 0%,100% { opacity: 1; } 50% { opacity: 0.4; } }
  @keyframes shimmer { 0% { background-position: -200% 0; } 100% { background-position: 200% 0; } }
  .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 16px; margin-bottom: 24px; }
  .card { background: var(--card); border: 1px solid var(--border); border-radius: 8px; padding: 16px; }
  .card h3 { font-size: 13px; color: var(--muted); text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 12px; }
  .stat { display: flex; justify-content: space-between; padding: 6px 0; font-size: 14px; border-bottom: 1px solid var(--border); }
  .stat:last-child { border-bottom: none; }
  .stat span:last-child { font-weight: 600; }
  .badge { display: inline-block; padding: 2px 8px; border-radius: 12px; font-size: 11px; font-weight: 600; white-space: nowrap; }
  .badge-hot { background: #3a1c1e; color: var(--red); }
  .badge-warm { background: #3a2e1a; color: var(--orange); }
  .badge-cold { background: #1c2a3a; color: var(--accent); }
  .badge-running { background: #1a3a2a; color: #7ee787; animation: pulse 1.5s infinite; }
  .badge-done { background: #0a2a1a; color: var(--green); }
  .badge-failed { background: #3a1c1e; color: var(--red); }
  .lead-item { padding: 8px 0; border-bottom: 1px solid var(--border); font-size: 13px; }
  .lead-item:last-child { border: none; }
  .lead-item .name { font-weight: 600; }
  .lead-item .meta { color: var(--muted); font-size: 12px; }
  pre { background: #0d1117; padding: 12px; border-radius: 6px; font-size: 12px; overflow-x: auto; margin-top: 8px; max-height: 200px; overflow-y: auto; white-space: pre-wrap; word-break: break-word; }
  .btn { background: var(--accent); color: #fff; border: none; padding: 6px 14px; border-radius: 6px; cursor: pointer; font-size: 12px; font-weight: 600; display: inline-flex; align-items: center; gap: 6px; transition: opacity 0.15s; }
  .btn:hover { opacity: 0.85; }
  .btn-sm { padding: 4px 10px; font-size: 11px; }
  .btn-green { background: var(--green); }
  .btn-orange { background: var(--orange); }
  .btn-red { background: var(--red); }
  .btn-outline { background: transparent; border: 1px solid var(--border); color: var(--text); }
  .btn:disabled { opacity: 0.5; cursor: not-allowed; }
  .btn .mini-spinner { width: 12px; height: 12px; border: 2px solid rgba(255,255,255,0.3); border-top-color: #fff; border-radius: 50%; animation: spin 0.8s linear infinite; display: inline-block; }
  .btn-label { display: inline-flex; align-items: center; gap: 4px; }
  .tab-nav { display: flex; gap: 4px; margin-bottom: 16px; flex-wrap: wrap; }
  .tab-btn { background: transparent; border: 1px solid var(--border); color: var(--muted); padding: 6px 14px; border-radius: 6px; cursor: pointer; font-size: 12px; transition: all 0.15s; }
  .tab-btn.active { background: var(--accent); color: #fff; border-color: var(--accent); }
  .tab-content { display: none; }
  .tab-content.active { display: block; }
  .section-title { font-size: 16px; font-weight: 600; margin: 20px 0 12px; }
  .flex-between { display: flex; justify-content: space-between; align-items: center; }
  .actions { display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 16px; }
  .toast { position: fixed; bottom: 20px; right: 20px; background: var(--card); border: 1px solid var(--border); padding: 12px 20px; border-radius: 8px; font-size: 13px; z-index: 100; opacity: 0; transition: opacity 0.3s; display: flex; align-items: center; gap: 8px; }
  .toast.show { opacity: 1; }
  .toast .spinner-s { width: 12px; height: 12px; border: 2px solid var(--accent); border-top-color: transparent; border-radius: 50%; animation: spin 0.8s linear infinite; }
  .run-item { padding: 8px 0; border-bottom: 1px solid var(--border); font-size: 12px; }
  .run-item:last-child { border: none; }
  .run-item .ts { color: var(--muted); }
  .run-item .run-header { display: flex; align-items: center; gap: 8px; margin-bottom: 4px; }
  .skill-card { background: var(--card); border: 1px solid var(--border); border-radius: 8px; padding: 16px; margin-bottom: 12px; }
  .skill-card .flex-between { margin-bottom: 8px; }
  .skill-card h4 { font-size: 14px; }
  .empty-state { color: var(--muted); font-size: 13px; padding: 20px 0; text-align: center; }
</style>
</head>
<body>

<div class="header">
  <h1><span id="header-dot" class="status-dot idle"></span>GCF · Hermes Pipeline</h1>
  <div style="display:flex;gap:8px;align-items:center">
    <span id="running-count" style="font-size:12px;color:var(--muted);display:none"></span>
    <button class="btn" onclick="refreshAll()">↻ Refresh</button>
  </div>
</div>

<div id="running-banner" class="running-banner" style="display:none">
  <div class="spinner"></div>
  <span id="running-msg">Running...</span>
</div>

<div class="tab-nav">
  <button class="tab-btn active" onclick="switchTab('pipeline')">Pipeline</button>
  <button class="tab-btn" onclick="switchTab('actions')">Run</button>
  <button class="tab-btn" onclick="switchTab('cron')">Cron</button>
  <button class="tab-btn" onclick="switchTab('runs')">Log</button>
  <button class="tab-btn" onclick="switchTab('status')">Status</button>
  <button class="tab-btn" onclick="switchTab('reports')">Reports</button>
</div>

<div id="tab-pipeline" class="tab-content active"></div>
<div id="tab-actions" class="tab-content"></div>
<div id="tab-cron" class="tab-content"></div>
<div id="tab-runs" class="tab-content"></div>
<div id="tab-status" class="tab-content"></div>
<div id="tab-reports" class="tab-content"></div>

<div id="toast" class="toast"></div>

<script>
const SKILL_NAMES = {
  'gcf-lead-scraper': 'Scrape Leads',
  'gcf-content-drafter': 'Draft Outreach',
  'gcf-outreach': 'Send Messages',
  'gcf-pipeline-view': 'Generate Report',
};

async function fetchJSON(url, opts) {
  try {
    const r = await fetch(url, opts || {});
    return await r.json();
  } catch(e) {
    return {};
  }
}

let toastTimer = null;
let toastRunning = false;

function toast(msg, type) {
  const t = document.getElementById('toast');
  if (type === 'running') {
    t.innerHTML = '<span class="spinner-s"></span> ' + msg;
    toastRunning = true;
  } else {
    t.innerHTML = msg;
    toastRunning = false;
  }
  t.classList.add('show');
  if (toastTimer) clearTimeout(toastTimer);
  if (!toastRunning) {
    toastTimer = setTimeout(() => t.classList.remove('show'), 3000);
  }
}

function updateHeader(running) {
  const dot = document.getElementById('header-dot');
  const banner = document.getElementById('running-banner');
  const runningMsg = document.getElementById('running-msg');
  const count = document.getElementById('running-count');
  const names = Object.keys(running || {});
  if (names.length) {
    dot.className = 'status-dot running';
    banner.style.display = 'flex';
    runningMsg.textContent = names.map(n => SKILL_NAMES[n] || n).join(', ') + '...';
    count.style.display = 'inline';
    count.textContent = names.length + ' active';
  } else {
    dot.className = 'status-dot idle';
    banner.style.display = 'none';
    count.style.display = 'none';
  }
}

// ── Pipeline Tab ──

function renderPipeline(d) {
  return (`
    <div class="grid">
      <div class="card">
        <h3>Leads</h3>
        <div class="stat"><span>Total in inbox</span><span>${d.total_leads}</span></div>
        <div class="stat"><span>Hot (9-10)</span><span style="color:var(--red)">${d.hot.length}</span></div>
        <div class="stat"><span>Warm (7-8)</span><span style="color:var(--orange)">${d.warm.length}</span></div>
        <div class="stat"><span>Cold (1-6)</span><span style="color:var(--muted)">${d.cold.length}</span></div>
      </div>
      <div class="card">
        <h3>Outreach</h3>
        <div class="stat"><span>In pipeline</span><span>${d.in_pipeline}</span></div>
        <div class="stat"><span>Sent</span><span>${d.sent}</span></div>
        <div class="stat"><span>Replied</span><span style="color:var(--green)">${d.replied}</span></div>
        <div class="stat"><span>Drafts ready</span><span>${d.drafts.length}</span></div>
      </div>
    </div>
  `) + (d.hot.length ? `
    <div class="section-title">Hot Leads (${d.hot.length})</div>
    ${d.hot.map(l => `<div class="lead-item"><span class="badge badge-hot">${l.score}</span> <span class="name">${l.name}</span> <span class="meta">${l.company}</span><br><span class="meta">${(l.signal||'').slice(0,80)}</span></div>`).join('')}
  ` : '') + (d.warm.length ? `
    <div class="section-title">Warm Leads (${d.warm.length})</div>
    ${d.warm.map(l => `<div class="lead-item"><span class="badge badge-warm">${l.score}</span> <span class="name">${l.name}</span> <span class="meta">${l.company}</span><br><span class="meta">${(l.signal||'').slice(0,80)}</span></div>`).join('')}
  ` : '') + (d.drafts.length ? `
    <div class="section-title">Drafts (${d.drafts.length})</div>
    ${d.drafts.map(n => `<div class="lead-item"><span class="meta">${n}</span></div>`).join('')}
  ` : '');
}

// ── Actions Tab ──

function renderActions(running) {
  const isRunning = (name) => running && running[name];
  return `
    <div class="card" style="margin-bottom:16px">
      <h3>Run Skills</h3>
      <p style="font-size:13px;color:var(--muted);margin-bottom:12px">Click to trigger a skill. Active runs shown in real-time.</p>
      <div class="actions">
        ${['gcf-lead-scraper','gcf-content-drafter','gcf-outreach','gcf-pipeline-view'].map(n => {
          const label = SKILL_NAMES[n] || n;
          const run = isRunning(n);
          const disabled = run ? 'disabled' : '';
          const cls = n === 'gcf-lead-scraper' ? 'btn-green' : n === 'gcf-content-drafter' ? 'btn-orange' : n === 'gcf-outreach' ? '' : 'btn-outline';
          const inner = run ? '<span class="mini-spinner"></span> Running...' : label;
          return `<button class="btn ${cls}" onclick="runSkill('${n}')" ${disabled}><span class="btn-label">${inner}</span></button>`;
        }).join('')}
      </div>
    </div>

    <div class="card" style="margin-bottom:16px">
      <h3>Schedule Automation</h3>
      <p style="font-size:13px;color:var(--muted);margin-bottom:12px">Set up daily cron jobs:</p>
      <ul style="font-size:13px;color:var(--muted);margin-bottom:12px;padding-left:16px">
        <li>07:00 — Scrape leads (daily)</li>
        <li>08:30 — Draft outreach for hot leads</li>
        <li>17:00 — Generate pipeline report</li>
      </ul>
      <button class="btn btn-green" onclick="setupCron()"> Setup Daily Schedule</button>
    </div>

    <div class="card" style="margin-bottom:16px">
      <h3>Quick Actions</h3>
      <div class="actions">
        <button class="btn btn-red btn-sm" onclick="killAllRuns()"> Stop All Runs</button>
        <button class="btn btn-outline btn-sm" onclick="switchTab('runs')"> View Log</button>
      </div>
    </div>
  `;
}

// ── Cron Tab ──

function renderCron(d) {
  let html = '<div class="card"><h3>Scheduled Jobs</h3>';
  if (d.jobs && d.jobs.length) {
    d.jobs.forEach(j => {
      const name = j.name || 'unnamed';
      const sched = j.schedule || j.cron || '?';
      const skill = j.skill || '-';
      html += '<div class="stat"><span>' + name + '</span><span>' + sched + '</span></div>';
      if (skill) html += '<div style="font-size:11px;color:var(--muted);margin:-4px 0 8px 0">skill: ' + skill + '</div>';
    });
  } else {
    html += '<div class="empty-state">No cron jobs. Go to Run tab → Setup Daily Schedule.</div>';
  }
  html += '</div>';
  return html;
}

// ── Runs Tab ──

function renderRuns(d) {
  const list = d.runs || [];
  if (!list.length) return '<div class="empty-state">No runs yet. Click a skill on the Run tab.</div>';
  return '<div class="card"><h3>Recent Runs</h3>' + list.map(r => {
    const ts = r[0] || '';
    const skill = r[1] || '';
    const status = r[2] || '';
    const out = r[3] || '';
    const label = SKILL_NAMES[skill] || skill;
    let cls = 'badge-cold';
    if (status === 'running') cls = 'badge-running';
    else if (status === 'done') cls = 'badge-done';
    else if (status === 'failed') cls = 'badge-failed';
    return '<div class="run-item"><div class="run-header"><span class="badge ' + cls + '">' + status + '</span> <strong>' + label + '</strong> <span class="ts">' + ts.slice(11,19) + '</span></div><pre>' + (out ? out.slice(0,300) : '(no output)') + '</pre></div>';
  }).join('') + '</div>';
}

// ── Status Tab ──

function renderStatus(d) {
  const txt = d.doctor || 'No status';
  return '<div class="card"><h3>Hermes Doctor</h3><pre style="max-height:500px">' + txt.slice(0,3000) + '</pre></div>';
}

// ── Reports Tab ──

function renderReports(d) {
  if (!d.reports || !d.reports.length) return '<div class="empty-state">No reports yet. Run Generate Report.</div>';
  return d.reports.map(r => '<div class="card" style="margin-bottom:12px"><h3 style="font-size:14px;text-transform:none;letter-spacing:0;margin-bottom:8px">' + r.name + '</h3><pre>' + r.content + '</pre></div>').join('');
}

// ── Actions ──

async function runSkill(name) {
  toast('Starting ' + (SKILL_NAMES[name] || name) + '...', 'running');
  const r = await fetchJSON('/api/run/skill/' + name, { method: 'POST' });
  if (r.status === 'started') {
    toast((SKILL_NAMES[name] || name) + ' running...', 'running');
    setFastPoll(true);
  } else {
    toast(r.message || 'Error', null);
  }
  refreshAll();
}

async function killAllRuns() {
  toast('Stopping...', 'running');
  const running = document.getElementById('header-dot');
  running.className = 'status-dot idle';
  document.getElementById('running-banner').style.display = 'none';
  toast('All runs stopped (UI only — server continues current tasks)', null);
  refreshAll();
}

async function setupCron() {
  toast('Setting up...', 'running');
  const r = await fetchJSON('/api/setup/cron', { method: 'POST' });
  toast('Cron jobs created', null);
  switchTab('cron');
}

// ── Refresh ──

async function refreshAll() {
  const [pipeline, cron, runs, status, reports] = await Promise.all([
    fetchJSON('/api/pipeline'),
    fetchJSON('/api/cron'),
    fetchJSON('/api/runs'),
    fetchJSON('/api/status'),
    fetchJSON('/api/reports'),
  ]);

  const running = runs.running || {};
  updateHeader(running);

  if (Object.keys(running).length > 0 && !fastPoll) {
    setFastPoll(true);
  }

  document.getElementById('tab-pipeline').innerHTML = renderPipeline(pipeline);
  document.getElementById('tab-actions').innerHTML = renderActions(running);
  document.getElementById('tab-cron').innerHTML = renderCron(cron);
  document.getElementById('tab-runs').innerHTML = renderRuns(runs);
  document.getElementById('tab-status').innerHTML = renderStatus(status);
  document.getElementById('tab-reports').innerHTML = renderReports(reports);
}

function switchTab(name) {
  document.querySelectorAll('.tab-content').forEach(t => t.classList.remove('active'));
  document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
  document.getElementById('tab-' + name).classList.add('active');
  document.querySelector('.tab-btn[onclick*="' + name + '"]').classList.add('active');
  refreshAll();
}

let refreshTimer = null;
let fastPoll = false;
let pollStart = null;
let elapsedInterval = null;

function setFastPoll(enabled) {
  fastPoll = enabled;
  if (refreshTimer) clearInterval(refreshTimer);
  if (elapsedInterval) clearInterval(elapsedInterval);
  if (enabled) {
    pollStart = Date.now();
    elapsedInterval = setInterval(updateElapsed, 1000);
    refreshTimer = setInterval(fastPollTick, 3000);
    fastPollTick();
  } else {
    pollStart = null;
    elapsedInterval = null;
    refreshTimer = setInterval(refreshAll, 10000);
  }
}

function updateElapsed() {
  if (!pollStart) return;
  const secs = Math.floor((Date.now() - pollStart) / 1000);
  const banner = document.getElementById('running-banner');
  const msg = document.getElementById('running-msg');
  if (banner.style.display !== 'none' && msg) {
    const names = Object.keys(window._lastRunning || {});
    const label = names.map(n => SKILL_NAMES[n] || n).join(', ');
    msg.textContent = label + '... ' + secs + 's';
  }
}

function fastPollTick() {
  if (!fastPoll) return;
  fetchJSON('/api/runs').then(data => {
    const running = data.running || {};
    window._lastRunning = running;
    updateHeader(running);
    const actions = document.getElementById('tab-actions');
    if (actions) actions.innerHTML = renderActions(running);
    if (Object.keys(running).length === 0) {
      setFastPoll(false);
      refreshAll();
    }
  });
}

refreshTimer = setInterval(refreshAll, 10000);
</script>
</body>
</html>"""


@app.get("/", response_class=HTMLResponse)
def dashboard():
    return HTMLResponse(DASHBOARD_HTML)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=4096)
