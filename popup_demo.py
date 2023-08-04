import time

from selenium.webdriver.common.by import By


def test_popup_demo(chrome_driver):
    chrome_driver.get("https://www.learning.npntraining.com/selenium-practice/popups/Popup.html")
    # basewindow = chrome_driver.current_window_handle
    # chrome_driver.find_element(By.CSS_SELECTOR, '#help').click()
    # time.sleep(3)
    #
    # handles = chrome_driver.window_handles
    # print(chrome_driver.find_element(By.ID,'tt').text)
    # chrome_driver.switch_to.window(basewindow)

    handles = chrome_driver.window_handles
    size = len(handles)
    parent_handle = chrome_driver.current_window_handle
    for x in range(size):
        if handles[x] != parent_handle:
            chrome_driver.switch_to.window(handles[x])
            print(chrome_driver.title)

            chrome_driver.close()
            break

    chrome_driver.switch_to.window(parent_handle)

    chrome_driver.find_element(By.ID, "link").click()
