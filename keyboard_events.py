from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from time import time, sleep


def test_keyboard_events(chrome_driver):
    chrome_driver.get("https://www.facebook.com")
    action = ActionChains(chrome_driver)
    chrome_driver.find_element(By.ID, 'email').send_keys("Arman")
    action.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
    action.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
    action.send_keys(Keys.TAB)
    action.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
    sleep(5)
    action.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
    sleep(10)










