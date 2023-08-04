import time

from selenium.webdriver.common.by import By


def test_date_picker(chrome_driver):
    chrome_driver.get("https://www.learning.npntraining.com/selenium-practice/webcontrols/DatePicker.html")
    chrome_driver.find_element(By.XPATH, "//label[text()='Date Of Birth']/following::input").send_keys("05/01/1997")
    time.sleep(5)