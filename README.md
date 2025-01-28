# 🚀 Remote Job Scraper

_A Python-powered web scraper that fetches remote job listings from [Remote.co](https://remote.co) and stores them in SQLite 📊_

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue?logo=python" alt="Python">
  <img src="https://img.shields.io/badge/License-MIT-green" alt="License">
  <img src="https://img.shields.io/badge/Status-Active-brightgreen" alt="Status">
</div>

---

## ✨ Features
- 🔍 **Smart Search** - Find jobs by keyword/role
- 🕸️ **Web Scraper** - Extracts 5 key job details
- 💾 **SQLite Storage** - Local database for results
- 🚫 **Duplicate Prevention** - No repeated entries
- 📆 **Schedule Tracking** - Full-time/Part-time info

---

## ⚙️ Requirements
```bash
# Install dependencies
pip install requests beautifulsoup4
```

---

## 🗃️ Database Schema
| Column         | Type      | Description          | Emoji |
|----------------|-----------|----------------------|-------|
| job_title      | TEXT      | Position name        | 📛    |
| job_types      | TEXT      | Full-time/Contract   | 🕒    |
| location       | TEXT      | Geographic info      | 🌍    |
| salary         | TEXT      | Compensation range   | 💰    |
| job_schedule   | TEXT      | Work hours           | 🕑    |

---

## 🚀 Quick Start
1. **Run the scraper**
```bash
python scraper.py --search "python developer"
```

2. **Check results**
```bash
sqlite3 jobs.db "SELECT * FROM jobs LIMIT 5;"
```

---

## 🤝 Connect with Creator
Let's build something amazing together! 🛠️

[![GitHub](https://img.shields.io/badge/-GitHub-181717?logo=github)](https://github.com/Abhishek08Mishra)
[![LinkedIn](https://img.shields.io/badge/-LinkedIn-0077B5?logo=linkedin)](https://www.linkedin.com/in/abhishek-mishra-120799281/)
[![Twitter](https://img.shields.io/badge/-Twitter-1DA1F2?logo=twitter)](https://x.com/Abhi__57)
[![Email](https://img.shields.io/badge/-Email-D14836?logo=gmail)](abishekmishra195@gmail.com)

---

## ⭐ Show Your Support

If this tool helps you, show some love by giving it a star! ⭐

---
> Made with ❤️ by [Abhishek Mishra] and python🐍
  
> ⚡ **Pro Tip:** Run scraper daily with cron jobs for fresh results!
```
