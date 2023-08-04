import time

from selenium.webdriver.common.by import By


def test_frames_demo(chrome_driver):
    chrome_driver.get("https://www.learning.npntraining.com/selenium-practice/selenium-api/1/IFrame-Main.html")

    chrome_driver.switch_to.frame('frame1')
    input1 = chrome_driver.find_element(By.CSS_SELECTOR, '#txtName1')
    input1.send_keys("Hello Arman")
    time.sleep(3)
    chrome_driver.find_element(By.XPATH, "//input[@value='Display']").click()
    time.sleep(3)
    print(input1.get_attribute('value'))
    chrome_driver.switch_to.parent_frame()

    chrome_driver.switch_to.frame(chrome_driver.find_element(By.XPATH, '//iframe[@src="IFrame2.html"]'))
    input2 = chrome_driver.find_element(By.CSS_SELECTOR, '#txtName2')
    input2.send_keys('Hello')
    time.sleep(3)
    chrome_driver.find_element(By.XPATH, "//input[@value='Show']").click()
    print(input2.get_attribute('value'))
    chrome_driver.switch_to.parent_frame()


