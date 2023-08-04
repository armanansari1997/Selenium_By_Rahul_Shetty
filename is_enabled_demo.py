from selenium.webdriver.common.by import By


def test_is_enabled_demo(chrome_driver):
    chrome_driver.get("https://www.learning.npntraining.com/selenium-practice/webcontrols/IsEnabled.html")
    nextbtn = chrome_driver.find_element(By.ID, 'btn')
    print(nextbtn.is_enabled()) # False
    assert not nextbtn.is_enabled()
    checkbox = chrome_driver.find_element(By.CSS_SELECTOR, '#agree')
    checkbox.click()
    print(nextbtn.is_enabled())  # True
    assert nextbtn.is_enabled()