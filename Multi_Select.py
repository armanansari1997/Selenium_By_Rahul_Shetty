import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def test_multi_select(chrome_driver):
    chrome_driver.get("https://www.learning.npntraining.com/selenium-practice/actions/DropDown-MultiSelect.html")
    select = Select(chrome_driver.find_element(By.ID, 'multipleDropDown'))
    items = chrome_driver.find_elements(By.CSS_SELECTOR, '#multipleDropDown option')
    print(len(items))
    action = ActionChains(chrome_driver)
    for item in items:
        action.click_and_hold(item)
        time.sleep(2)
