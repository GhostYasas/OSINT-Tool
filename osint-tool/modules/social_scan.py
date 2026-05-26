# modules/social_scan.py

import requests

def check_username(username):
    """
    Check if a username exists on popular platforms
    No API key needed - checks HTTP response codes
    """
    
    platforms = {
        "GitHub":        f"https://github.com/{username}",
        "Twitter/X":     f"https://twitter.com/{username}",
        "Instagram":     f"https://www.instagram.com/{username}",
        "Reddit":        f"https://www.reddit.com/user/{username}",
        "TikTok":        f"https://www.tiktok.com/@{username}",
        "Pinterest":     f"https://www.pinterest.com/{username}",
        "Twitch":        f"https://www.twitch.tv/{username}",
        "YouTube":       f"https://www.youtube.com/@{username}",
        "LinkedIn":      f"https://www.linkedin.com/in/{username}",
        "Medium":        f"https://medium.com/@{username}",
        "DevTo":         f"https://dev.to/{username}",
        "Hackerrank":    f"https://www.hackerrank.com/{username}",
        "Leetcode":      f"https://leetcode.com/{username}",
        "Pastebin":      f"https://pastebin.com/u/{username}",
        "Telegram":      f"https://t.me/{username}",
    }

    results = {}
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }

    for platform, url in platforms.items():
        try:
            response = requests.get(url, headers=headers, timeout=8, allow_redirects=True)
            if response.status_code == 200:
                results[platform] = {"found": True, "url": url}
            else:
                results[platform] = {"found": False, "url": url}
        except Exception:
            results[platform] = {"found": False, "url": url}

    return results