from selenium import webdriver
import time
import math

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
BASE_URL = "http://suninjuly.github.io/alert_accept.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    driver.get(BASE_URL)
    driver.find_element(By.TAG_NAME, "button").click()
    confirm = driver.switch_to.alert
    confirm.accept()

    x_element = driver.find_element(By.XPATH, "//label/span[2]")
    x = x_element.text
    print(x)
    y = calc(x)
    print(y)

    input_math = driver.find_element(By.XPATH, "//input[@id = 'answer']")
    input_math.send_keys(y)

    driver.find_element(By.TAG_NAME, "button").click()
finally:
    time.sleep(7)
    driver.quit()
