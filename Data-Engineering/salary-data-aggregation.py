# This program fetches, scrapes, integrates, and standardizes salary data from Oracle Fusion HCM, Glassdoor, and survey file. 
# The final dataset provides a clean, structured salary report for analysis. 

import requests
from bs4 import BeautifulSoup
import pandas as pd

# Oracle Fusion HCM API Credentials
ORACLE_HCM_BASE_URL = "https://your-oracle-hcm-instance.oraclecloud.com"
ORACLE_HCM_USERNAME = "your_username"
ORACLE_HCM_PASSWORD = "your_password"

# Function to fetch salary data from Oracle Fusion HCM
def fetch_hcm_salaries():
    api_endpoint = f"{ORACLE_HCM_BASE_URL}/hcmRestApi/resources/11.13.18.05/workers"
    
    # Authentication
    response = requests.get(api_endpoint, auth=(ORACLE_HCM_USERNAME, ORACLE_HCM_PASSWORD))
    
    if response.status_code != 200:
        print(f"Failed to fetch data from Oracle HCM: {response.status_code}")
        return pd.DataFrame()
    
    # Parse JSON response
    data = response.json()
    salaries = []

    # Extract relevant salary data
    for worker in data.get("items", []):
        try:
            salaries.append({
                "Source": "Oracle HCM",
                "Job Title": worker.get("WorkTerms", [{}])[0].get("Job", {}).get("Name", "Unknown"),
                "Location": worker.get("WorkTerms", [{}])[0].get("Location", {}).get("Name", "Unknown"),
                "Salary": worker.get("WorkTerms", [{}])[0].get("SalaryAmount", {}).get("Value", "0")
            })
        except Exception as e:
            print(f"Error parsing worker data: {e}")
    
    return pd.DataFrame(salaries)

# Function to scrape Glassdoor salaries
def scrape_glassdoor_salaries(job_title, location):
    url = f"https://www.glassdoor.com/Salaries/{location}-{job_title}-salary-SRCH_IL.0,10_IC1147401_KO11,21.htm"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"Failed to fetch data from Glassdoor: {response.status_code}")
        return pd.DataFrame()
    
    soup = BeautifulSoup(response.text, 'html.parser')
    salaries = []

    salary_elements = soup.find_all("div", class_="col-2 d-none d-md-flex flex-row justify-content-start")
    
    for salary in salary_elements:
        try:
            job = salary.find("a").text.strip()
            pay = salary.find("span", class_="d-block mt-xxsm").text.strip()
            salaries.append({"Source": "Glassdoor", "Job Title": job, "Location": location, "Salary": pay})
        except AttributeError:
            continue  

    return pd.DataFrame(salaries)

# Function to read salary survey data from CSV
def read_survey_data(csv_path):
    try:
        df = pd.read_csv(csv_path)
        df["Source"] = "Survey"
        return df[["Source", "Job Title", "Location", "Salary"]]
    except Exception as e:
        print(f"Error reading survey data: {e}")
        return pd.DataFrame()

# Standardize salary data (convert to numeric)
def standardize_salary(df):
    df["Salary"] = df["Salary"].replace("[^\d]", "", regex=True)  
    df["Salary"] = pd.to_numeric(df["Salary"], errors="coerce")  
    df.dropna(subset=["Salary"], inplace=True)
    return df

# Main function to fetch, aggregate, and clean salary data
def aggregate_salary_data():
    job_title = "Data-Engineer"
    location = "New-York"

    # Fetch salary data from Oracle HCM
    df_hcm = fetch_hcm_salaries()

    # Scrape Glassdoor salaries
    df_glassdoor = scrape_glassdoor_salaries(job_title, location)

    # Read salary survey data
    df_survey = read_survey_data("survey_salaries.csv")

    # Merge all sources
    df_combined = pd.concat([df_hcm, df_glassdoor, df_survey], ignore_index=True)

    # Standardize salary values
    df_cleaned = standardize_salary(df_combined)

    # Save to CSV
    df_cleaned.to_csv("standardized_salaries.csv", index=False)
    print("Standardized salary data saved successfully!")

# Run script
if __name__ == "__main__":
    aggregate_salary_data()

