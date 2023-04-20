import requests
from bs4 import BeautifulSoup
import pandas as pd

# Create an empty list to store job data
job_data = []

# Loop through each page of job listings
for page in range(1, 3): # Let's assume we want to extract data from the first 5 pages
    # Send a GET request to the webpage and get its content
    url = f'https://www.remotely.de/jobs?72b20725_page={page}'
    response = requests.get(url)
    html_content = response.content

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all job listings on the page
    job_listings = soup.find_all('div', {'class': 'cms-item-contentbox'})

    # Extract job details and store them in the job_data list
    for job in job_listings:
        title = job.find('a', {'class': 'link col-jobs-link'}).text.strip()
        company = job.find('a', {'class': 'col-job-company'}).text.strip()
        link = job.findNext('a', {'class': 'link col-jobs-link'})['href']
        link = f'https://www.remotely.de{link}'
        job_data.append({'Title': title, 'Company': company, 'Link': link})

# Convert the list of dictionaries to a pandas DataFrame and save it as an Excel sheet
df = pd.DataFrame(job_data)
print(df)
df.to_excel('job_listings.xlsx', index=False)