import time

from selenium.webdriver.common.by import By


def test_simple_login_demo(chrome_driver):
    chrome_driver.get("https://www.learning.npntraining.com/selenium-practice/misc/SimpleLogin.html")
    username = chrome_driver.find_element(By.NAME, 'userid')
    username.send_keys('Arman.Ansari')
    print(username.get_attribute('value'))
    password = chrome_driver.find_element(By.NAME, 'pswrd')
    password.send_keys("arman@123")
    print(password.get_attribute('value'))
    time.sleep(2)
    chrome_driver.find_element(By.CSS_SELECTOR, '#login').click()
    # chrome_driver.find_element(By.XPATH, "//input[@type='reset']")