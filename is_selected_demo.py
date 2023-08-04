from selenium.webdriver.common.by import By


def test_is_selected_demo(chrome_driver):
    chrome_driver.get("https://www.learning.npntraining.com/selenium-practice/webcontrols/IsSelected.html")
    checkbox = chrome_driver.find_element(By.CSS_SELECTOR, '#agree')
    print(checkbox.is_selected())  # False
    assert not checkbox.is_selected()
    checkbox.click()
    print(checkbox.is_selected())  # True
    assert checkbox.is_selected()