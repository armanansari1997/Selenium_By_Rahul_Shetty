import time

from selenium.webdriver.common.by import By


def test_dynamic_dropdown(chrome_driver):
    chrome_driver.get("https://www.learning.npntraining.com/selenium-practice/webcontrols/AutoComplete.html")
    input = chrome_driver.find_element(By.CSS_SELECTOR, '.ui-widget > input')
    input.send_keys('e')
    res = chrome_driver.find_elements(By.CSS_SELECTOR, '.ui-menu-item')
    for x in res:
        if x.text == 'Erlang':
            x.click()
            break
