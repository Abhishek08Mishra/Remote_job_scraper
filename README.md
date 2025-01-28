# 🚀 Remote Job Scraper

_A Python-powered web scraper that fetches remote job listings from [Remote.co](https://remote.co) and stores them in SQLite 📊_


---

## ✨ Features
- 🔍 **Smart Search** - Find jobs by keyword/role
- 🕸️ **Web Scraper** - Extracts 5 key job details
- 💾 **SQLite Storage** - Local database for results
- 🚫 **Duplicate Prevention** - No repeated entries
- 📆 **Schedule Tracking** - Full-time/Part-time info

---

---

## 🗃️ Database Schema
| Column         | Type      | Description          | Emoji |
|----------------|-----------|----------------------|-------|
| job_title      | TEXT      | Position name        | 📛    |
| job_types      | TEXT      | Full-time/Contract   | 🕒    |
| location       | TEXT      | Geographic info      | 🌍    |
| salary         | TEXT      | Compensation range   | 💰    |
| job_schedule   | TEXT      | Work hours           | 🕑    |


## 🚀 Quick Start

Follow these steps to run the **Remote Job Scraper**:

### 1. **Clone the Repository** (if you haven't already)
If you haven't cloned the repository yet, start by cloning it:


git clone https://github.com/Abhishek08Mishra/remote-job-scraper.git
cd remote-job-scraper

 #### set up your environment
 pip install -r requirements.txt

 #### Run the scraper
 python scraper.py --search "python developer"
 
#### check the result
  > Once the scraper has run successfully, the results will be saved in an SQLite database (jobs.db). To view the first 5 job listing
         >>> sqlite3 jobs.db "SELECT * FROM jobs LIMIT 5;"

# Let's build something amazing together! 🛠️

## 📬 Get in Touch
Got questions? Reach out!

<div align="center">
  <a href="https://linkedin.com/in/abhishek-mishra-120799281/">
    <img src="https://img.shields.io/badge/-LinkedIn-0077B5?logo=linkedin" alt="LinkedIn" width="100"/>
  </a>
  <br>
  <a href="https://github.com/Abhishek08Mishra">
    <img src="https://img.shields.io/badge/-GitHub-181717?logo=github" alt="GitHub" width="100"/>
  </a>
  <br>
  <a href="https://x.com/Abhi__57">
    <img src="https://img.shields.io/badge/-X-1DA1F2?logo=x" alt="X" width="100"/>
  </a>
   <br>
  <a href="mailto:abishekmishra195.com">
    <img src="https://img.shields.io/badge/-Email-D14836?logo=gmail" alt="Email" width="100"/>
  </a>
</div>

---

## ⭐ Show Your Support

If this tool helps you, show some love by giving it a star! ⭐

---
> Made with ❤️ by [Abhishek Mishra] and python🐍
  
> ⚡ **Pro Tip:** Run scraper daily with cron jobs for fresh results!
```
