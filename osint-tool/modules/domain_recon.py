# modules/domain_recon.py

import dns.resolver
import requests
import socket

def get_whois(domain):
    """Get WHOIS information using multiple fallback APIs"""
    
    # Method 1: whoisjson free API
    try:
        url = f"https://whoisjson.com/api/v1/whois?domain={domain}"
        headers = {"User-Agent": "OSINT-Recon-Tool"}
        response = requests.get(url, timeout=10)
        data = response.json()

        if data.get("registrar"):
            return {
                "domain": domain,
                "registrar": data.get("registrar", "N/A"),
                "creation_date": str(data.get("creation_date", "N/A"))[:10],
                "expiration_date": str(data.get("expiration_date", "N/A"))[:10],
                "name_servers": data.get("name_servers", []),
                "country": data.get("registrant_country", "N/A")
            }
    except Exception:
        pass

    # Method 2: who-dat free API
    try:
        url2 = f"https://who-dat.as93.net/{domain}"
        headers = {"User-Agent": "OSINT-Recon-Tool"}
        response2 = requests.get(url2, timeout=10)
        data2 = response2.json()

        registrar = data2.get("registrar", {}).get("name", "N/A")
        dates = data2.get("registry_data", {})
        nameservers = data2.get("nameservers", [])

        return {
            "domain": domain,
            "registrar": registrar,
            "creation_date": str(dates.get("created_date", "N/A"))[:10],
            "expiration_date": str(dates.get("expiration_date", "N/A"))[:10],
            "name_servers": nameservers if isinstance(nameservers, list) else [],
            "country": data2.get("registrant", {}).get("country", "N/A")
        }
    except Exception:
        pass

    # Method 3: fallback using IP lookup
    try:
        ip = socket.gethostbyname(domain)
        url3 = f"http://ip-api.com/json/{ip}?fields=country,isp,org"
        response3 = requests.get(url3, timeout=10)
        data3 = response3.json()

        return {
            "domain": domain,
            "registrar": data3.get("org", "N/A"),
            "creation_date": "N/A",
            "expiration_date": "N/A",
            "name_servers": [],
            "country": data3.get("country", "N/A")
        }
    except Exception as e:
        return {"error": str(e)}


def get_dns_records(domain):
    """Get DNS records (A, MX, TXT, NS, CNAME)"""
    records = {}
    record_types = ["A", "MX", "TXT", "NS", "CNAME"]
    
    for record_type in record_types:
        try:
            answers = dns.resolver.resolve(domain, record_type)
            records[record_type] = [str(r) for r in answers]
        except:
            records[record_type] = []
    
    return records


def get_subdomains(domain):
    """Find subdomains using crt.sh"""
    try:
        url = f"https://crt.sh/?q=%.{domain}&output=json"
        response = requests.get(url, timeout=30)
        data = response.json()
        
        subdomains = set()
        for entry in data:
            name = entry["name_value"]
            for sub in name.split("\n"):
                sub = sub.strip()
                if sub and not sub.startswith("*"):
                    subdomains.add(sub)
        
        return list(subdomains)
    except Exception as e:
        print(f"  [!] Subdomain error: {e}")
        return []