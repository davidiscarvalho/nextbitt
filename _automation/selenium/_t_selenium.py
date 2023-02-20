import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from credentials import UPK_TEST_URL, UPK_TEST_USR, UPK_TEST_PWD

username = UPK_TEST_USR
password = UPK_TEST_PWD
AMB_URL = UPK_TEST_URL


SELECTION_URL = 'preventive/workorders/selection'


# Start a webdriver (e.g. Chrome)
service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

URL = AMB_URL

# Set the URL of the report
url = URL
print("0")
# Navigate to the report page
driver.get(url)
time.sleep(3) # Sleep for 3 seconds

element = driver.find_element(by=By.ID, value="txtUserName")
element.send_keys(username)
element = driver.find_element(by=By.ID, value="txtPassword")
element.send_keys(password)
submit_button = driver.find_element(by=By.ID, value="btnLogin")
submit_button.click()

test = driver.title
print("1"+test)

test = driver.title
print("2"+test)

time.sleep(3) # Sleep for 3 seconds
# Close the webdriver
driver.quit()
