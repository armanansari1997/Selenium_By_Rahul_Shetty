import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


def test_drag_and_drop(chrome_driver):
    chrome_driver.get("https://www.learning.npntraining.com/selenium-practice/actions/DragMe.html")
    action = ActionChains(chrome_driver)
    drag = chrome_driver.find_element(By.ID, 'draggable')
    # action.drag_and_drop_by_offset(drag, 20, 200).perform()
    action.click_and_hold(drag).perform()
    action.move_by_offset(200,30).perform()
    time.sleep(2)
    action.release().perform()