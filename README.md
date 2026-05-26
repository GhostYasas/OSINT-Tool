# 🔍 OSINT Reconnaissance Tool

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)

A powerful open-source OSINT (Open Source Intelligence) investigation tool built for cybersecurity professionals, penetration testers, and digital forensics investigators. Automates reconnaissance tasks and generates professional PDF reports.

---

## 🎯 Features

| Module | Description |
|--------|-------------|
| 🌐 Domain Recon | WHOIS lookup, DNS records (A, MX, TXT, NS), subdomain enumeration |
| 📍 IP Geolocation | IP resolution, geolocation, ISP, coordinates, timezone |
| 🛡️ IP Reputation | Proxy/VPN detection, hosting detection, mobile detection |
| 📧 Email Breach Check | Check emails against breach databases via LeakCheck API |
| 👤 Social Media Scan | Username search across 15 platforms simultaneously |
| 📄 PDF Report | Auto-generates professional investigation report |

---

## 📸 Screenshots
<img width="593" height="749" alt="image" src="https://github.com/user-attachments/assets/eaf2a640-e31b-4ee3-a938-73f7ebb83031" />
<img width="636" height="611" alt="image" src="https://github.com/user-attachments/assets/6dd0f303-7a22-4e17-9fd3-1beed46aa193" />

 ---

## 🛠️ Installation

### Requirements
- Python 3.8 or higher
- pip

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/osint-recon-tool.git
cd osint-recon-tool
```

### 2. Install dependencies

```bash
pip install requests dnspython fpdf2 colorama
```

### 3. Run the tool

```bash
python main.py
```

---

## 📁 Project Structure
```
📁 osint-recon-tool/
│
├── 📄 main.py                 → Main entry point (run this)
├── 📄 requirements.txt        → Python dependencies
├── 📄 README.md               → Project documentation
│
├── 📁 modules/
│   ├── 🌐 domain_recon.py     → WHOIS, DNS, subdomain enumeration
│   ├── 📍 ip_recon.py         → IP geolocation and reputation
│   ├── 📧 email_check.py      → Email breach detection
│   ├── 👤 social_scan.py      → Social media username scanner
│   └── 📄 report.py           → PDF report generator
│
└── 📁 output/
    └── 📊 recon_*.pdf         → Generated investigation reports
```

---

## 🔧 Usage

Run the tool and follow the prompts:

```bash
python main.py
```

1. Enter a **target domain** (e.g. `example.com`)
2. Optionally enter an **email** to check for breaches
3. Optionally enter a **username** to scan social media
4. PDF report is automatically saved to the `output/` folder

---

## 🌐 Platforms Scanned

The social media scanner checks the following platforms:

- GitHub
- Twitter / X
- Instagram
- Reddit
- TikTok
- Pinterest
- Twitch
- YouTube
- LinkedIn
- Medium
- Dev.to
- HackerRank
- LeetCode
- Pastebin
- Telegram

---

## 📦 Dependencies
requests
dnspython
fpdf2
colorama

Install all dependencies with:

```bash
pip install -r requirements.txt
```

---

## ⚠️ Disclaimer

This tool is intended for **educational purposes** and **authorized security testing only**.

- Only use this tool on domains and targets you have **explicit permission** to investigate
- The author is not responsible for any misuse or damage caused by this tool
- Always follow your local laws and regulations regarding cybersecurity investigations

---

## 🔮 Future Improvements

- [ ] Web-based dashboard (React frontend)
- [ ] VirusTotal API integration for domain reputation
- [ ] Shodan API integration for exposed services
- [ ] AbuseIPDB integration for IP threat scoring
- [ ] Export results to JSON and CSV formats
- [ ] Automated scheduled scans
- [ ] Email/Slack alerting system

---

## 👨‍💻 Author

**Yasasvee Dulanjan**
- GitHub: https://github.com/GhostYasas
- LinkedIn: https://www.linkedin.com/in/yasasvee-dulanjan/

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

⭐ **If you found this useful, please give it a star on GitHub!**


