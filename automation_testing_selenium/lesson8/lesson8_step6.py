from selenium import webdriver
import time
import math

from selenium.webdriver.common.by import By
from selenium.webdriver.support import select
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
BASE_URL = "http://suninjuly.github.io/execute_script.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    driver.get("http://suninjuly.github.io/execute_script.html")
    span_str = driver.find_element(By.XPATH, "//span[@id = 'input_value']")
    span_int = span_str.text
    print(span_int)
    task = calc(span_int)
    driver.find_element(By.XPATH, "//input[@id = 'answer']").send_keys(task)
    driver.find_element(By.XPATH, "//input[@id = 'robotCheckbox']").click()
    driver.find_element(By.XPATH, "//input[ @ id = 'robotsRule']").click()

    button = driver.find_element(By.TAG_NAME, "button")
    driver.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    time.sleep(7000)
    driver.quit()
