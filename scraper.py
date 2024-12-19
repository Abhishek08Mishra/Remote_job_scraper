import requests
from bs4 import BeautifulSoup
import pandas as pd
from db_operation import insert_job_data # Used to insert job details into a database and create table if not exists

def scrape_remote_jobs(search_term):
    
    url = f"https://remote.co/remote-jobs/search?searchkeyword={search_term}"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    }
    
    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, "html.parser")

    job_listings = soup.find_all('div', class_='sc-14nyru2-2 fmkHkh')
    
    fetched_jobs = []

    for job in job_listings:

        job_title = job.find("a", class_="sc-jv5lm6-13 cMHfum textWrap").text.strip()

        job_types = job.find("li", class_="sc-jv5lm6-9 jxMgfz tag-name").text.strip()

        location = job.find("span", class_="sc-jv5lm6-10 efTTiy allowed-location").text.strip()

        salary = job.find("li", class_="sc-jv5lm6-9 jxMgfz tag-name", id=lambda x: x and "salartRange" in x)
        salary = salary.text.strip() if salary else "Not specified"

        job_schedule = job.find("li", class_="sc-jv5lm6-9 jxMgfz tag-name", id=lambda x: x and "jobschedule" in x)
        job_schedule = job_schedule.text.strip() if job_schedule else "Not specified" 

        fetched_jobs.append({
        "job_title": job_title,
        "job_types": job_types,
        "location": location,
        "salary": salary,
        "job_schedule": job_schedule
    })
        
    for job in fetched_jobs:
        insert_job_data(job['job_title'], job['job_types'], job['location'], job['salary'], job['job_schedule'])
    
    # Display each job's details to ensure the data is correct.
    # for job in fetched_jobs:
    #     print(f"Job title: {job['job_title']},\nJob types: {job['job_types']},\nLocation: {job['location']},\nSalary: {job['salary']},\nJob schedule: {job['job_schedule']}\n")


    df = pd.DataFrame(fetched_jobs) # Convert the list of dictionaries to a pandas DataFrame
    df.to_csv('remote_jobs.csv', index=False) # Write the DataFrame to a CSV file


# Call the function and pass the search term as an argument
scrape_remote_jobs(search_term = input("Enter the job role that you want to search for (e.g., python, data science, digital marketing): ").lower())