# MY-Python-Project

# Job Scraper

This project is a web scraper that fetches remote job listings from a specified website [https://remote.co/] and stores the job details in a SQLite database.

## Features
- Scrapes remote job listings based on a search term.
- Extracts job title, job type, location, salary, and job schedule.
- Stores the job details in a SQLite database.

  ## Requirements
  Before running the project, make sure you have Python 3.x installed. You will also need to install the following libraries:
- Python 3.x
- `requests` library
- `beautifulsoup4` library
- `sqlite3` library (comes with Python)

You can install them using `pip`:
like : pip install requests
       pip install beautifulsoup4



## Code Explanation

### `scarper.py`

The `scarper.py` script is responsible for scraping remote job listings from a specified website and storing the job details in a SQLite database. Below is a detailed explanation of how the script works:

1. **Importing Libraries**:
    - `requests`: For making HTTP requests to fetch web pages.
    - `BeautifulSoup` from `bs4`: For parsing HTML content.
    - `insert_job_data` from `DB_operation`: For inserting job details into the database.

    ```python
    import requests
    from bs4 import BeautifulSoup
    from DB_operation import insert_job_data
    ```

2. **Defining the [scrape_remote_jobs](http://_vscodecontentref_/1) Function**:
    - The function takes a [search_term](http://_vscodecontentref_/2) as input to search for specific job roles.

    ```python
    def scrape_remote_jobs(search_term):
    ```

3. **Constructing the URL**:
    - The URL is constructed using the provided search term.

    ```python
    url = f"https://remote.co/remote-jobs/search?searchkeyword={search_term}"
    ```

4. **Setting Up Headers**:
    - Headers are set to copy a web browser.

    ```python
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    }
    ```

5. **Making the HTTP Request**:
    - A GET request is sent to the URL with the headers.

    ```python
    response = requests.get(url, headers=headers)
    ```

6. **Parsing the HTML Response**:
    - The HTML response is parsed using BeautifulSoup.

    ```python
    soup = BeautifulSoup(response.text, "html.parser")
    ```

7. **Finding Job Listings**:
    - All job listings are found using the specified HTML class.

    ```python
    job_listings = soup.find_all('div', class_='sc-14nyru2-2 fmkHkh')
    ```

8. **Extracting Job Details**:
    - For each job listing, the job title, job type, location, salary, and job schedule are extracted.

    ```python
    fetched_jobs = []

    for job in job_listings:
        job_title = job.find("a", class_="sc-jv5lm6-13 cMHfum textWrap").text.strip()
        job_types = job.find("li", class_="sc-jv5lm6-9 jxMgfz tag-name").text.strip()
        location = job.find("span", class_="sc-jv5lm6-10 efTTiy allowed-location").text.strip()
        salary = job.find("li", class_="sc-jv5lm6-9 jxMgfz tag-name", id=lambda x: x and "salartRange" in x)
        salary = salary.text.strip() if salary else "Not specified"
        job_schedule = job.find("li", class_="sc-jv5lm6-9 jxMgfz tag-name", id=lambda x: x and "jobschedule" in x)
        job_schedule = job_schedule.text.strip() if job_schedule else "Not specified"
    ```

9. **Storing Job Details**:
    - The extracted job details are stored in a list called [fetched_jobs](http://_vscodecontentref_/3).

    ```python
        fetched_jobs.append({
            "job_title": job_title,
            "job_types": job_types,
            "location": location,
            "salary": salary,
            "job_schedule": job_schedule
        })
    ```

10. **Inserting Job Details into the Database**:
    - The job details are inserted into the database using the [insert_job_data](http://_vscodecontentref_/4) function.

    ```python
    for job in fetched_jobs:
        insert_job_data(job["job_title"], job["job_types"], job["location"], job["salary"], job["job_schedule"])
    ```

This script effectively scrapes job listings based on a search term and stores the relevant details in a database for further use.



## Code Explanation

### `DB_operation.py`

The `DB_operation.py` script handles database operations for storing job details. Here's a brief overview:

1. **Creating the Database**:
    - The `create_database` function creates a SQLite database named `jobs.db` and a table named `jobs` to store job information.

2. **Inserting Job Data**:
    - The `insert_job_data` function inserts job details into the `jobs` table, ensuring no duplicate entries by checking if a job with the same title already exists.
