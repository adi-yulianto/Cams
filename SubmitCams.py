from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import Select
import time
import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


#PARAMETER
url="https://cams.collega.co.id/"
user=""
passw=""


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get(url)
driver.maximize_window()

WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.NAME,"submit")))
driver.find_element(By.NAME,"username").send_keys(user)
driver.find_element(By.NAME,"password").send_keys(passw)
driver.find_element(By.NAME,"password").send_keys(Keys.ENTER)

time.sleep(5)
WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CLASS_NAME, "btn.btn-success.waves-effect.waves-light"))).click()
driver.find_element(By.XPATH,"//*[text()='My Activities']").click()

Tgl=['2024-08-05','2024-08-06','2024-08-07','2024-08-08','2024-08-09']
for x in Tgl:

    time.sleep(5)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, f"//td[@data-date='{x}']"))).click()
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID,"send"))).click()
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH,"//button[@type='button' and text()='Yes!']"))).click()