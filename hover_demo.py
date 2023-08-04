import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


def test_hover_demo(chrome_driver):
    chrome_driver.get("https://www.learning.npntraining.com/selenium-practice/actions/MenuOptions.html")
    action = ActionChains(chrome_driver)
    action.move_to_element(chrome_driver.find_element(By.CSS_SELECTOR, '#services')).perform()
    time.sleep(3)
    chrome_driver.find_element(By.LINK_TEXT, 'Web Design').click()
    assert chrome_driver.title == 'Google'