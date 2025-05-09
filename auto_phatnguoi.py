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
#lấy hình ảnh mã captcha vềvề
def get_captcha_image(driver):
    img = driver.find_element(By.ID,"imgCaptcha")
    img_url = img.screenshot_as_png
    file_path='captcha.png'
    if os.path.exists(file_path):
        os.remove(file_path)
    #luu file
    with open("captcha.png", "wb") as f:
        f.write(img_url)
#Lấy Text Captcha bằng hình ảnh
def captcha():
    reader = easyocr.Reader(['en'])
    results = reader.readtext('captcha.png',detail=0) #detail=0 --> Trả về chỉ text (dạng chuỗi)
    return results
#Điền vào form để tiến hành tìm kiếm
def fill_form(driver, bien_so, option, captcha_text):
    driver.find_element(By.XPATH, '//*[@id="formBSX"]/div[2]/div[3]/div/input').send_keys(captcha_text)
    driver.find_element(By.XPATH, '//*[@id="formBSX"]/div[2]/div[1]/input').send_keys(bien_so)
    select = driver.find_element(By.TAG_NAME, 'select')
    select.click()
    options = driver.find_elements(By.TAG_NAME, 'option')
    for opt in options:
        if opt.text == option:
            opt.click()
            break

    driver.find_element(By.XPATH, '//*[@id="formBSX"]/div[2]/input[1]').click()
#Lấy text ==  Mã xác nhận sai! nếu mã captcha sai
def is_captcha_correct(driver):
    time.sleep(10)
    error_xpath = '//*[@id="formBSX"]/div[2]/div[4]'
    error_element = driver.find_element(By.XPATH, error_xpath)
    return error_element.text

def work_time():
    bien_so = os.getenv("bien_so")
    option = os.getenv("option")
    driver = webdriver.Chrome()
    while True:
        driver.get("https://www.csgt.vn/tra-cuu-phuong-tien-vi-pham.html")
        get_captcha_image(driver)
        captcha_text = captcha()
        fill_form(driver, bien_so, option, captcha_text)
        #Kiểm tra mã captcha đúng hay sai 
        error = 'Mã xác nhận sai!'
        if error != is_captcha_correct(driver):
            time.sleep(10)
            driver.quit()
            break
    

#Set lich chay
schedule.every().day.at("06:00").do(work_time)
schedule.every().day.at("12:00").do(work_time)
while True:
    schedule.run_pending()
    time.sleep(20)









