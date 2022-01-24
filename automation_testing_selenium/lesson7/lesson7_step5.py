from selenium import webdriver
import time
import math

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    driver.get("http://suninjuly.github.io/math.html")

    x_element = driver.find_element(By.XPATH, "//label/span[2]")
    x = x_element.text
    print(x)
    y = calc(x)
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


