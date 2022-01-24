from selenium import webdriver
import time

from selenium.webdriver.common.by import By

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.XPATH, "//label[text() = 'First name*']//following-sibling::input")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.XPATH, "//label[text() = 'Last name*']//following-sibling::input")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.XPATH, "//label[text() = 'Email*']//following-sibling::input")
    input3.send_keys("Smolensk@gmail.com")
    input4 = browser.find_element(By.XPATH, "//label[text() = 'Phone:']//following-sibling::input")
    input4.send_keys("+79505405060")
    input5 = browser.find_element(By.XPATH, "//label[text() = 'Address:']//following-sibling::input")
    input5.send_keys("Russia")
    button = browser.find_element(By.XPATH, "//button[contains(text(), 'Subm')]")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

