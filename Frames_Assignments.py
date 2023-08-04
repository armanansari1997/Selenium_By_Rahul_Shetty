import time

from selenium.webdriver.common.by import By


def test_frames_assignments(chrome_driver):
    chrome_driver.get("https://www.learning.npntraining.com/selenium-practice/selenium-api/frames/FrameInsideFrame.html")
    param1 = chrome_driver.find_element(By.CSS_SELECTOR, '#txt1')
    param1.send_keys('Hello Arman')
    time.sleep(3)
    print(param1.get_attribute('value'))

    chrome_driver.switch_to.frame(0)
    param2 = chrome_driver.find_element(By.ID, 'txt2')
    param2.send_keys('Hello Param2')
    print(param2.get_attribute('value'))
    try:
        chrome_driver.switch_to.frame(chrome_driver.find_element(By.XPATH, "//iframe[@src='FrameInside.html']"))
    except Exception as e:
        print(e)
    param3 = chrome_driver.find_element(By.ID, 'txt3')
    param3.send_keys('Hello Param3')
    print(param3.get_attribute('value'))
    chrome_driver.switch_to.parent_frame()
