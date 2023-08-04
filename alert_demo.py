import time

from selenium.webdriver.common.by import By


def test_alert_demo(chrome_driver):
    chrome_driver.get("https://www.learning.npntraining.com/selenium-practice/webcontrols/alerts_example.html")
    # chrome_driver.find_element(By.CSS_SELECTOR, '#jsPromptExample button').click()
    # alert = chrome_driver.switch_to.alert
    # alert.send_keys('Arman')
    # alert.accept()
    # res = chrome_driver.find_element(By.XPATH, "//p[@id='userResponse2']").text
    # print(res)
    chrome_driver.find_element(By.CSS_SELECTOR, '#jsConfirmExample button').click()
    alert = chrome_driver.switch_to.alert
    time.sleep(5)
    alert.dismiss()