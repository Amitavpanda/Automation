# LinkedIn Lead Scraper
import json
def scrape_linkedin(profile):
    data = {
        "source": "linkedin.com",
        "url": f"https://www.linkedin.com/in/{profile}",
        "signals": ["looking-for-developer", "startup-founding"],
        "absolute_urgency": "high",
        "action": "save-to-leads-json" 
    }
    return data