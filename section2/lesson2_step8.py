from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os 

current_dir = os.path.abspath(os.path.dirname(__file__))     
file_path = os.path.join(current_dir, 'file.txt')            

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input_name = browser.find_element(By.NAME, "firstname")
    input_name.send_keys("Shamil")
    
    input_surname = browser.find_element(By.NAME, "lastname")
    input_surname.send_keys("Gumerov")
    
    input_email = browser.find_element(By.NAME, "email")
    input_email.send_keys("shamusg12345@gmail.com")

    upload_button = browser.find_element(By.ID, "file")
    upload_button.send_keys(file_path)
    
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    
    time.sleep(5)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
