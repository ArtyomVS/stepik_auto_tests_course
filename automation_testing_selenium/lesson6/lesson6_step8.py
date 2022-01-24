from selenium import webdriver
import time

from selenium.webdriver.common.by import By
browser = webdriver.Chrome()
print("start")
try:
    browser.get("http://suninjuly.github.io/find_xpath_form")
    input1 = browser.find_element(By.NAME, "first_name")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = browser.find_element(By.XPATH, "//button[contains(text(), 'Subm')]")
    button.click()

finally:
    time.sleep(30)
    browser.quit()