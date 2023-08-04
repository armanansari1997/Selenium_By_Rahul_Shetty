import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def test_dropdown_demo(chrome_driver):
    chrome_driver.get("https://www.learning.npntraining.com/selenium-practice/webcontrols/DropDown.html")
    # time.sleep(5)
    dropdown = Select(chrome_driver.find_element(By.CSS_SELECTOR, '#userexp'))
    dropdown.select_by_index(2)
    time.sleep(2)
    dropdown.select_by_value("internet")
    time.sleep(2)
    dropdown.select_by_visible_text("Successfull Calls")
    time.sleep(2)
    res = chrome_driver.find_element(By.XPATH, "//div[@id = 'result']").text
    assert res == '1'
    chrome_driver.get_screenshot_as_file("screen1.png")

