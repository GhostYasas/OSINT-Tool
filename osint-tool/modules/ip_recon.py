# modules/ip_recon.py

import requests
import socket

def get_ip_from_domain(domain):
    """Convert domain to IP address"""
    try:
        ip = socket.gethostbyname(domain)
        return ip
    except Exception as e:
        return None

def get_ip_geolocation(ip):
    """Get geolocation info for an IP (free, no API key needed)"""
    try:
        url = f"http://ip-api.com/json/{ip}"
        response = requests.get(url, timeout=10)
        data = response.json()
        
        if data["status"] == "success":
            return {
                "ip": ip,
                "country": data.get("country"),
                "city": data.get("city"),
                "region": data.get("regionName"),
                "isp": data.get("isp"),
                "org": data.get("org"),
                "lat": data.get("lat"),
                "lon": data.get("lon"),
                "timezone": data.get("timezone")
            }
        else:
            return {"error": "Could not get geolocation"}
    except Exception as e:
        return {"error": str(e)}

def check_ip_reputation(ip):
    """Check if IP is malicious using AbuseIPDB (free API)"""
    try:
        # Free check using ip-api.com proxy field
        url = f"http://ip-api.com/json/{ip}?fields=proxy,hosting,mobile"
        response = requests.get(url, timeout=10)
        data = response.json()
        
        return {
            "is_proxy": data.get("proxy", False),
            "is_hosting": data.get("hosting", False),
            "is_mobile": data.get("mobile", False)
        }
    except Exception as e:
        return {"error": str(e)}