from selenium import webdriver
import time
import math
import os

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
BASE_URL = "http://suninjuly.github.io/file_input.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    driver.get(BASE_URL)
    #Заполнение полей ввода
    driver.find_element(By.XPATH, "//input[@name = 'firstname']").send_keys("Artyom")
    driver.find_element(By.XPATH, "//input[@name = 'lastname']").send_keys("Artyom")
    driver.find_element(By.XPATH, "//input[@name = 'email']").send_keys("Artyom@test.com")

    #Загрузка файла
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "file_example.txt"
    file_path = os.path.join(current_dir, file_name)
    element = driver.find_element(By.CSS_SELECTOR, "[type='file']")
    element.send_keys(file_path)

    driver.find_element(By.TAG_NAME, "button").click()

finally:
    time.sleep(7000)
    driver.quit()
