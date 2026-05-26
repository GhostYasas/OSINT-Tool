# modules/email_check.py

import requests
import re

def check_email_breach(email):
    """Check if email was in a data breach using free LeakCheck API"""
    try:
        url = f"https://leakcheck.io/api/public?check={email}"
        headers = {
            "User-Agent": "OSINT-Recon-Tool"
        }
        response = requests.get(url, headers=headers, timeout=10)
        data = response.json()

        if data.get("success"):
            found = data.get("found", 0)
            sources = data.get("sources", [])

            if found > 0:
                return {
                    "email": email,
                    "breached": True,
                    "breach_count": found,
                    "breaches": [s.get("name", "Unknown") for s in sources]
                }
            else:
                return {
                    "email": email,
                    "breached": False,
                    "breach_count": 0,
                    "breaches": []
                }
        else:
            return {"error": data.get("error", "Unknown error from LeakCheck")}

    except Exception as e:
        return {"error": str(e)}

def check_email_format(email):
    """Basic email format validation"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def extract_domain_from_email(email):
    """Extract domain from email for further recon"""
    try:
        return email.split("@")[1]
    except:
        return None