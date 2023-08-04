from selenium.webdriver.common.by import By


def test_is_displayed_demo(chrome_driver):
    chrome_driver.get("https://www.learning.npntraining.com/selenium-practice/webcontrols/IsDisplayed.html")
    inp = chrome_driver.find_element(By.CSS_SELECTOR, '#t1')
    inp.send_keys('Hello Arman')
    assert inp.is_displayed()
    chrome_driver.find_element(By.CSS_SELECTOR, '#btn1').click()
    assert not inp.is_displayed()
    chrome_driver.find_element(By.CSS_SELECTOR, '#btn1').click()
    assert inp.is_displayed()
