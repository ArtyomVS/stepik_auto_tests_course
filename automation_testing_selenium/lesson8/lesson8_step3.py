

from selenium import webdriver
import time
import math

from selenium.webdriver.common.by import By
from selenium.webdriver.support import select
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
BASE_URL = "http://suninjuly.github.io/selects1.html"

try:
    driver.get(BASE_URL)
    one = driver.find_element(By.XPATH, "//span[@id = 'num1']")
    two = driver.find_element(By.XPATH, "//span[@id = 'num2']")
    first_number = int(one.text)
    second_number = int(two.text)
    third_number = first_number + second_number
    print(third_number)
    fourth_number = str(third_number)
    print(fourth_number)

    #field_select = driver.find_element(By.ID, "#dropdown").click()
    select = Select(driver.find_element(By.TAG_NAME, "select"))
    select.select_by_value(fourth_number)

    driver.find_element(By.TAG_NAME, "button").click()

finally:
    time.sleep(10)
    driver.quit()