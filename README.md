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

# Job Database Management

This `DB_operation.py` script provides a simple implementation of a SQLite database to manage job information. It includes functionality to create a database, insert job data, and prevent duplicate job entries.

## Features
- **Database Creation**: Automatically creates a `jobs.db` SQLite database with a `jobs` table if it doesn't already exist.
- **Job Insertion**: Inserts job details (job title, types, location, salary, and schedule) into the database.
- **Duplicate Prevention**: Ensures no duplicate job titles are added to the database.

## Prerequisites
- Python 3.x
- SQLite (comes pre-installed with Python)

## Table Structure
The `jobs` table has the following columns:

| Column Name    | Data Type | Description                      |
|----------------|-----------|----------------------------------|
| `id`           | INTEGER   | Primary key, auto-incremented.   |
| `job_title`    | TEXT      | Title of the job (required).     |
| `job_types`    | TEXT      | Type of job (e.g., full-time).   |
| `location`     | TEXT      | Location of the job (e.g., USA). |
| `salary`       | TEXT      | Salary details (optional).       |
| `job_schedule` | TEXT      | Job schedule (e.g., remote).     |

## Usage

### 1. Create the Database
To create the database and table, simply run the `create_database` function:

```python
create_database()
```
This creates a SQLite database file named `jobs.db` with the required schema.

### 2. Insert Job Data
To insert job data into the database, use the `insert_job_data` function. For example:

```python
insert_job_data(
    job_title="Software Engineer",
    job_types="Full-Time",
    location="New York",
    salary="$100,000 - $120,000",
    job_schedule="On-site"
)
```

This adds a job entry to the database unless a job with the same title already exists.

### 3. Handle Duplicate Entries
If you attempt to insert a job title that already exists, the program will output:

```
Already Exists
```
This ensures that duplicate job entries are avoided.

## File Descriptions
- `jobs.db`: SQLite database file (created after running the script).
- `create_database`: Function to create the database and table.
- `insert_job_data`: Function to insert job details into the database.

## Example Output
Example output when running the script:

1. Creating the database:
```
Database and table created successfully.
```

2. Inserting a new job:
```
Data inserted: Software Engineer at New York
```

3. Inserting a duplicate job:
```
Already Exists
```

## License
This project is open-source and available under the [MIT License](LICENSE).
