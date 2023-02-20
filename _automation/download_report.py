################################################################
#
# Download report from SQL Server Reporting Services
#
# Author: David Carvlaho
#
# Date: 2023/01/27
#
################################################################

from credentials import SSRS_PROD_USR, SSRS_PROD_PWD 

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# Start a webdriver (e.g. Chrome)
service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

URL1 = 'http://nbbiprod.northeurope.cloudapp.azure.com/Reports/Pages/Report.aspx?ItemPath=%2fEDP%2fConfigura%c3%a7%c3%b5es%2fEDP+-+Sincroniza%c3%a7%c3%a3o+-+Mobilidade&ViewMode=Detail'
URL2 = 'http://nbbiprod.northeurope.cloudapp.azure.com/Reports/Pages/Report.aspx?ItemPath=%2fEDP%2fConfigura%c3%a7%c3%b5es%2fEDP+-+Sincroniza%c3%a7%c3%a3o+-+Mobilidade&rs:Format=EXCEL'
username = SSRS_PROD_USR
password = SSRS_PROD_PWD


# Set the URL of the report
url = URL1

# Set the credentials for the report
credentials = (username, password)



#driver = webdriver.Chrome()

# Navigate to the report page
driver.get(url)
print("****************************************************1")
# Wait for the pop-up to appear
# wait = WebDriverWait(driver, 10)
# wait.until(EC.alert_is_present())
time.sleep(3) # Sleep for 3 seconds
print("****************************************************2")

# Switch to the pop-up and enter the credentials
alert = driver.switch_to.alert
send_keys(username + Keys.TAB + password)
alert.accept()
print("****************************************************3")

# Wait for the report to load
wait.until(EC.presence_of_element_located((By.ID, 'export-to-excel')))

# Click on the "Export to Excel" button
driver.find_element_by_id('export-to-excel').click()

# Wait for the download to complete
# you can use the code below to wait till the download complete
'''
import os
import time

download_dir = "/path/to/downloads"
while len(os.listdir(download_dir)) == 0:
    time.sleep(1)
'''

# Close the webdriver
driver.quit()