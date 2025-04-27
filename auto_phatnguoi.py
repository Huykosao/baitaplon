import easyocr
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from urllib.parse import urljoin
import os
import schedule
from dotenv import load_dotenv


load_dotenv()

option = os.getenv("option")
bien_so = os.getenv("bien_so")

def captcha():
    driver = webdriver.Chrome()
    while True:
        driver.get("https://www.csgt.vn/tra-cuu-phuong-tien-vi-pham.html")
        #tim hinh 
        img = driver.find_element(By.ID,"imgCaptcha")
        img_url = img.screenshot_as_png
        file_path='captcha.png'
        if os.path.exists(file_path):
            os.remove(file_path)
        #luu file
        with open("captcha.png", "wb") as f:
            f.write(img_url)
        #xu ly hinh anh lay captcha
        reader = easyocr.Reader(['en'])
        results = reader.readtext('captcha.png',detail=0) #detail=0 --> Trả về chỉ text (dạng chuỗi)
        captcha = results
        #Nhap ma captcha
        captcha_input = '//*[@id="formBSX"]/div[2]/div[3]/div/input'
        element_captcha = driver.find_element(By.XPATH, captcha_input)
        element_captcha.send_keys(captcha)
        #Nhap Bien So
        bien_xpath = '//*[@id="formBSX"]/div[2]/div[1]/input'
        element_bienso = driver.find_element(By.XPATH, bien_xpath)
        element_bienso.send_keys(bien_so)
        #Chon Phuong Tien
        element_select = driver.find_element(By.TAG_NAME, 'select')
        element_select.click()
        element_options = driver.find_elements(By.TAG_NAME,'option')
        for chon in element_options:
            if chon.text == option:
                chon.click()
                break
        #Nhan Nut
        button = '//*[@id="formBSX"]/div[2]/input[1]'
        element_button = driver.find_element(By.XPATH, button)
        element_button.click()
        #Kiem Tra Ma captcha
        time.sleep(10)
        error = 'Mã xác nhận sai!'
        error_xpath = '//*[@id="formBSX"]/div[2]/div[4]'
        element_error = driver.find_element(By.XPATH, error_xpath)
        if error != element_error.text:
            time.sleep(10)
            driver.quit()
            break
#Set lich chay
schedule.every().day.at("06:00").do(captcha)
schedule.every().day.at("12:00").do(captcha)
while True:
    schedule.run_pending()
    time.sleep(20)









