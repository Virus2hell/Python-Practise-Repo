data_science_jobs = [
    {'job_title': 'Data Scientist', 'job_skills': "['Python', 'SQL', 'Machine Learning']", 'job_date': '2023-05-12'},
    {'job_title': 'Machine Learning Engineer', 'job_skills': "['Python', 'TensorFlow', 'Deep Learning']", 'job_date': '2023-05-15'},
    {'job_title': 'Data Analyst', 'job_skills': "['SQL', 'R', 'Tableau']", 'job_date': '2023-05-10'},
    {'job_title': 'Business Intelligence Developer', 'job_skills': "['SQL', 'PowerBI', 'Data Warehousing']", 'job_date': '2023-05-08'},
    {'job_title': 'Data Engineer', 'job_skills': "['Python', 'Spark', 'Hadoop']", 'job_date': '2023-05-18'},
    {'job_title': 'AI Specialist', 'job_skills': "['Python', 'PyTorch', 'AI Ethics']", 'job_date': '2023-05-20'}
]

from datetime import datetime, date
import ast

datetime.now()

test_data = data_science_jobs[0]['job_date']
print(type(test_data)) # This will print the type of test_data, which is <class 'str'> since the job_date is stored as a string in the dictionary.

date_object = datetime.strptime(test_data, '%Y-%m-%d')
print(type(date_object)) # This will print the type of date_object, which is <class 'datetime.datetime'> since we have converted the string to a datetime object using strptime() method.

print(date_object)

for job in data_science_jobs:
    job['job_date'] = datetime.strptime(job['job_date'], '%Y-%m-%d')
    job['job_skills'] = ast.literal_eval(job['job_skills']) # This will convert the string representation of the list back to an actual list using ast.literal_eval() method.

print(data_science_jobs) # This will print the list of dictionaries with the job_date converted to datetime objects.
