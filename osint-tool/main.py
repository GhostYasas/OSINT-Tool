# main.py

from modules.domain_recon import get_whois, get_dns_records, get_subdomains
from modules.ip_recon import get_ip_from_domain, get_ip_geolocation, check_ip_reputation
from modules.email_check import check_email_breach, check_email_format
from modules.social_scan import check_username
from modules.report import generate_report
from colorama import Fore, Style, init

init()

def print_banner():
    print(Fore.CYAN + """
    ╔═══════════════════════════════════╗
    ║     OSINT RECON TOOL v1.0         ║
    ║     Built for Investigation       ║
    ╚═══════════════════════════════════╝
    """ + Style.RESET_ALL)

def print_section(title):
    print(Fore.CYAN + f"\n{'='*45}" + Style.RESET_ALL)
    print(Fore.YELLOW + f"  {title}" + Style.RESET_ALL)
    print(Fore.CYAN + f"{'='*45}" + Style.RESET_ALL)

def main():
    print_banner()

    target = input(Fore.YELLOW + "[?] Enter target domain: " + Style.RESET_ALL)

    # ── WHOIS ──
    print_section("WHOIS INFORMATION")
    whois_data = get_whois(target)
    if "error" not in whois_data:
        print(f"  Registrar     : {whois_data['registrar']}")
        print(f"  Country       : {whois_data['country']}")
        print(f"  Created       : {whois_data['creation_date']}")
        print(f"  Expires       : {whois_data['expiration_date']}")
        print(f"  Name Servers  : {', '.join(whois_data['name_servers'][:2]) if whois_data['name_servers'] else 'N/A'}")
    else:
        print(f"  [!] {whois_data['error']}")

    # ── DNS ──
    print_section("DNS RECORDS")
    dns_data = get_dns_records(target)
    for record_type, values in dns_data.items():
        if values:
            print(f"  {record_type:6} : {', '.join(values[:3])}")

    # ── IP RECON ──
    print_section("IP GEOLOCATION")
    ip = get_ip_from_domain(target)
    geo = {}
    rep = {}
    if ip:
        print(f"  Resolved IP   : {ip}")
        geo = get_ip_geolocation(ip)
        if "error" not in geo:
            print(f"  Country       : {geo['country']}")
            print(f"  City          : {geo['city']}, {geo['region']}")
            print(f"  ISP           : {geo['isp']}")
            print(f"  Organization  : {geo['org']}")
            print(f"  Coordinates   : {geo['lat']}, {geo['lon']}")
            print(f"  Timezone      : {geo['timezone']}")

        print_section("IP REPUTATION CHECK")
        rep = check_ip_reputation(ip)
        if "error" not in rep:
            print(f"  Is Proxy/VPN  : {'⚠️  YES' if rep['is_proxy'] else '✅ NO'}")
            print(f"  Is Hosting    : {'⚠️  YES' if rep['is_hosting'] else '✅ NO'}")
            print(f"  Is Mobile     : {'📱 YES' if rep['is_mobile'] else '✅ NO'}")
    else:
        print(f"  [!] Could not resolve IP for {target}")

    # ── SUBDOMAINS ──
    print_section("SUBDOMAINS")
    subdomains = get_subdomains(target)
    if subdomains:
        print(f"  Found {len(subdomains)} subdomains:")
        for sub in subdomains[:10]:
            print(f"    → {sub}")
    else:
        print("  [!] No subdomains found (crt.sh may be slow)")

    # ── EMAIL BREACH CHECK ──
    print_section("EMAIL BREACH CHECK")
    email_result = None
    email = input(Fore.YELLOW + "  [?] Enter email to check (or press Enter to skip): " + Style.RESET_ALL)
    if email.strip():
        if check_email_format(email):
            print(f"  Checking {email}...")
            email_result = check_email_breach(email)
            if "error" in email_result:
                print(Fore.RED + f"  [!] {email_result['error']}" + Style.RESET_ALL)
            elif email_result["breached"]:
                print(Fore.RED + f"  ⚠️  BREACHED! Found in {email_result['breach_count']} breaches:" + Style.RESET_ALL)
                for breach in email_result["breaches"][:5]:
                    print(f"    → {breach}")
            else:
                print(Fore.GREEN + f"  ✅ No breaches found for {email}" + Style.RESET_ALL)
        else:
            print(f"  [!] Invalid email format")
    else:
        print(f"  [i] Skipped")

    # ── SOCIAL MEDIA SCAN ──
    print_section("SOCIAL MEDIA USERNAME SCAN")
    social_results = None
    username = input(Fore.YELLOW + "  [?] Enter username to search (or press Enter to skip): " + Style.RESET_ALL)
    if username.strip():
        print(f"\n  Searching for '{username}' across platforms...\n")
        social_results = check_username(username)
        found_count = 0
        not_found = []
        for platform, data in social_results.items():
            if data["found"]:
                found_count += 1
                print(Fore.GREEN + f"  ✅ FOUND    {platform:15} → {data['url']}" + Style.RESET_ALL)
            else:
                not_found.append(platform)
        if not_found:
            print(Fore.RED + f"\n  ❌ NOT FOUND: {', '.join(not_found)}" + Style.RESET_ALL)
        print(f"\n  📊 Found on {found_count}/{len(social_results)} platforms")
    else:
        print(f"  [i] Skipped")

    # ── PDF REPORT ──
    print_section("GENERATING PDF REPORT")
    try:
        filename = generate_report(
            target, whois_data, dns_data,
            ip, geo, rep, subdomains,
            email_result, social_results
        )
        print(Fore.GREEN + f"  ✅ Report saved: {filename}" + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"  [!] Report error: {e}" + Style.RESET_ALL)

    print(Fore.CYAN + f"\n{'='*45}" + Style.RESET_ALL)
    print(Fore.GREEN + "  ✅ Recon Complete!" + Style.RESET_ALL)
    print(Fore.CYAN + f"{'='*45}\n" + Style.RESET_ALL)

if __name__ == "__main__":
    main()