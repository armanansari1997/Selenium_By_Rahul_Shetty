import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


def test_action_class_demo(chrome_driver):
    # chrome_driver.get("https://www.learning.npntraining.com/selenium-practice/actions/ContextClick.html")
    chrome_driver.get("https://www.learning.npntraining.com/selenium-practice/actions/DoubleClick.html")

    action = ActionChains(chrome_driver)

    # Right Click
    # action.context_click(chrome_driver.find_element(By.ID, 'div-context')).perform()

    # Double Click
    action.double_click(chrome_driver.find_element(By.XPATH, "//button[text()='Click ME !']")).perform()
    time.sleep(2)
    alert = chrome_driver.switch_to.alert
    res = alert.text
    alert.accept()
    assert 'Double Clicked !!' == res


