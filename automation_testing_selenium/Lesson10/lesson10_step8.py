from selenium import webdriver
import time
import math

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
BASE_URL = "http://suninjuly.github.io/explicit_wait2.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    driver.get(BASE_URL)
    cost_dollars = WebDriverWait(driver, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    button_book = driver.find_element(By.ID, "book").click()

    x_element = driver.find_element(By.XPATH, "//label/span[2]")
    x = x_element.text
    print(x)
    y = calc(x)
    print(y)

    input_math = driver.find_element(By.XPATH, "//input[@id = 'answer']")
    input_math.send_keys(y)

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    driver.find_element(By.ID, "solve").click()


finally:
    time.sleep(10)
    driver.quit()
