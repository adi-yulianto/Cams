from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import Select
import time
import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

#PARAMETER
url=""
user=""
passw=""
start = datetime.date(2023,11,13)
TglSkip='2023-11-14'

TextSenin = open("InputSenin.txt","r")
TextSelasa = open("InputSelasa.txt","r")
TextRabu = open("InputRabu.txt","r")
TextKamis = open("InputKamis.txt","r")
TextJumat = open("InputJumat.txt","r")
 
# initializing K 
RangeDay= 5
res = []
for day in range(RangeDay):
    date = (start + datetime.timedelta(days = day)).isoformat()
    res.append(date)

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

Input=[TextSelasa,TextRabu,TextKamis,TextJumat]
# Tgl=['2023-11-07','2023-11-08','2023-11-09','2023-11-10']
Tgl=res
for x,y in zip(Tgl,Input):
    if x ==  TglSkip:
        print(f"Tanggal di Skip adalah {x}")
        continue

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

    # WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='withOptGroup']/div/div[1]"))).click()
    # WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "(//div[contains(@class,'menu')])[2]")))
    # driver.find_element(By.XPATH, "//*[text()='A root options']").click()
    # if x == "2023-11-04":
    #     break
