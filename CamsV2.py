from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

#PARAMETER

url=""
user=""
passw=""

TextSenin = open("InputSenin.txt","r")
TextSelasa = open("InputSelasa.txt","r")
TextRabu = open("InputRabu.txt","r")
TextKamis = open("InputKamis.txt","r")
TextJumat = open("InputJumat.txt","r")

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

Input=[TextSenin,TextSelasa,TextRabu,TextKamis,TextJumat]
Tgl=['2024-01-29','2024-01-30','2024-01-31','2024-02-01','2024-02-02']
for x,y in zip(Tgl,Input):

    time.sleep(5)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, f"//td[@data-date='{x}']"))).click()

    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID,"aktual-start-time"))).click()
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH,"//div[@class='clockpicker-tick' and text()='8']"))).click()

    # driver.find_element(By.XPATH,"//div[@class='clockpicker-tick' and text()='00']").click()
    driver.find_element(By.XPATH,"//button[@type='button' and text()='Done']").click()

    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID,"aktual-end-time"))).click()
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH,"(//div[@class='clockpicker-tick' and text()='18'])[2]"))).click()

    # driver.find_element(By.XPATH,"//div[@class='clockpicker-tick' and text()='00']").click()
    driver.find_element(By.XPATH,"(//button[@type='button' and text()='Done'])[2]").click()

    IsPro= Select(driver.find_element(By.ID,"ispro"))
    IsPro.select_by_value("2") #2-Non Project

    FWA= Select(driver.find_element(By.ID,"fwa"))
    FWA.select_by_value("2") #2-WFO

    Jns= Select(driver.find_element(By.ID,"jenis"))
    Jns.select_by_value("1") #1-BAU

    Loc= Select(driver.find_element(By.NAME,"location"))
    Loc.select_by_value("1") #1-Talavera

    with y as f:
        lines = [line.strip('\t') for line in f]    
        driver.find_element(By.ID,"deskripsi").send_keys(lines)

    driver.find_element(By.XPATH,"//*[@id='submit']").click()

    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH,"//button[@type='button' and text()='Yes!']"))).click()
