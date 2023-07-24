import requests
import pandas as pd
import load_to_db

# VARIABLES DECLARATION
url = "https://jsearch.p.rapidapi.com/search"
querystring = {"query":"Data Engineer in Ontario, Canada","page":"1","num_pages":"1","date_posted":"month"}
headers = {
	"X-RapidAPI-Key": "a0139f52d4mshf129fb600694e41p10962ejsnd689f7c88b89",
	"X-RapidAPI-Host": "jsearch.p.rapidapi.com"
}

# LIST OF SKILLS
words = ['ETL','Orchestration', 'modeling', 'python', 
         'sql','pandas','docker','aws','gcp','google cloud',
         'postgres','mongodb','spark','jira','databricks',
         'azure','dbt','amazon','s3','linux','hadoop','kubernetes',
         'hbase','hive','fivetran','mage','airflow','ci/cd','elt']

acronyms = ['sql','dbt','elt','etl','aws','gcp'] # Acronyms from skills list that would need to be made uppercase

# Create a function to extract skills from an input
def extract_skills(c):
    skills = []
    for i in words:
        if i.lower() in c.lower():
            if i.lower() in acronyms:
                skills.append(i.upper())
            else: 
                skills.append(i.title())
    return skills

def get_data_from_api():
    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()
    print(data)  # This will print the API response
    return data


def extract_relevant_records_from_overall_data(data):
    # Initialize lists to store data
    employer_website = []
    job_id = []
    job_employment_type = []
    job_title = []
    job_apply_link=[]
    job_description=[]
    job_city=[]
    job_country =[]
    job_posted_at_date =[]
    employer_company_type =[]

    for i in range(len(data['data'])):
        employer_website.append(data['data'][i]['employer_website'])
        job_id.append(data['data'][i]['job_id'])
        job_employment_type.append(data['data'][i]['job_employment_type'])
        job_title.append(data['data'][i]['job_title'])
        job_apply_link.append(data['data'][i]['job_apply_link'])
        job_description.append(data['data'][i]['job_description'])
        job_city.append(data['data'][i]['job_city'])
        job_country.append(data['data'][i]['job_country'])
        job_posted_at_date.append(data['data'][i]['job_posted_at_datetime_utc'][:10])
        employer_company_type.append(data['data'][i]['employer_company_type'])

    return employer_website, job_id, job_employment_type, job_title, job_apply_link, job_description, job_city, job_country, job_posted_at_date, employer_company_type

def translate_extractions_to_dataframe_and_transform(employer_website, job_id, job_employment_type, job_title, job_apply_link, job_description, job_city, job_country, job_posted_at_date, employer_company_type):
    # Placing values into columns
    rapid_dict = {
                    'job_id': job_id,
                    'employer_website':employer_website,
                    'job_employment_type':job_employment_type,
                    'job_title':job_title,
                    'job_apply_link':job_apply_link,
                    'job_description':job_description,
                    'job_city':job_city,
                    'job_country':job_country,
                    'job_posted_at_date':job_posted_at_date,
                    'employer_company_type':employer_company_type        
                 }
    job_df = pd.DataFrame(rapid_dict) # Convert to dataframe
    
    # Convert date column datatype from string to datetime
    job_df['job_posted_at_date'] = pd.to_datetime(job_df['job_posted_at_date'])
    
    # Add a new column in the dataframe and extract skills from the job_description column
    # Using the job_description column as an input in the extract_skills function
    job_df['skillset'] = job_df['job_description'].apply(lambda x: extract_skills(x))
    
    # Change the position of the skillset column from last to after the job_description column
    # Remove the skillset column and save it in a variable
    skillset_col = job_df.pop('skillset')
    
    # Insert column using insert(position,column_name,skillset_col) function
    job_df.insert(6, 'skillset', skillset_col)
  
    return job_df

# Call process_api_data()
data = get_data_from_api()
employer_website, job_id, job_employment_type, job_title, job_apply_link, job_description, job_city, job_country, job_posted_at_date, employer_company_type = extract_relevant_records_from_overall_data(data)
df = translate_extractions_to_dataframe_and_transform(employer_website, job_id, job_employment_type, job_title, job_apply_link, job_description, job_city, job_country, job_posted_at_date, employer_company_type)

# Create the table
load_to_db.create_table()

# Load the dataframe into the table
load_to_db.load_to_postgres(df)
