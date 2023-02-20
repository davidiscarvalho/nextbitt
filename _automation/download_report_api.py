# não funciona
################################################################
#
# Download report from SQL Server Reporting Services
#
# Author: David Carvlaho
#
# Date: 2023/01/27
#
################################################################

import requests
import pandas as pd
import base64

from credentials import SSRS_PROD_USR, SSRS_PROD_PWD 


URL1 = 'http://nbbiprod.northeurope.cloudapp.azure.com/Reports/Pages/Report.aspx?ItemPath=%2fEDP%2fConfigura%c3%a7%c3%b5es%2fEDP+-+Sincroniza%c3%a7%c3%a3o+-+Mobilidade&ViewMode=Detail'
URL2 = 'http://nbbiprod.northeurope.cloudapp.azure.com/Reports/Pages/Report.aspx?ItemPath=%2fEDP%2fConfigura%c3%a7%c3%b5es%2fEDP+-+Sincroniza%c3%a7%c3%a3o+-+Mobilidade&rs:Format=EXCEL'
username = SSRS_PROD_USR
password = SSRS_PROD_PWD


# Set the URL of the report
url = URL2

# Set the credentials for the report
credentials = (username, password)

# # Send a request to the report and save the response
# response = requests.get(url, auth=credentials)

headers = {'Authorization': 'Basic ' + base64.b64encode(f"{username}:{password}".encode()).decode()}
response = requests.get(url, headers=headers)

print(response)
# Save the response to an Excel file
with open('report.xlsx', 'wb') as f:
    f.write(response.content)

# Read the Excel file into a pandas DataFrame
df = pd.read_excel('report.xlsx')

# Print the first few rows of the DataFrame
print(df.head())