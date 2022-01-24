from selenium import webdriver
import time
import math

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
BASE_URL = "http://suninjuly.github.io/get_attribute.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    driver.get(BASE_URL)

    picture = driver.find_element(By.XPATH, "//img")
    value_attribute = picture.get_attribute("valuex")
    print(value_attribute)
    y = calc(value_attribute)
    print(y)

    input_math = driver.find_element(By.XPATH, "//input[@id = 'answer']")
    input_math.send_keys(y)

    checkbox = driver.find_element(By.ID, "robotCheckbox")
    checkbox.click()

    radiobutton = driver.find_element(By.ID, "robotsRule")
    radiobutton.click()

    submit = driver.find_element(By.XPATH, "// button[text() = 'Submit']")
    submit.click()

finally:
    time.sleep(10)
    driver.quit()
