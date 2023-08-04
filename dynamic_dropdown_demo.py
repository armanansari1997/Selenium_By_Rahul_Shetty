import time

from selenium.webdriver.common.by import By


def test_dynamic_dropdown_demo(chrome_driver):
    chrome_driver.get("https://www.learning.npntraining.com/selenium-practice/webcontrols/DropDown.html")
    chrome_driver.find_element(By.ID, 'dropdownMenuButton').click()
    links = chrome_driver.find_elements(By.XPATH, "//ul[@class='dropdown-menu show']/li/a")
    print(len(links))
    for x in links:
        if x.text == 'Contact Us':
            x.click()
            break
    assert "NPN Training" in chrome_driver.title