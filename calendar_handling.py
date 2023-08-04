from time import sleep

from selenium.webdriver.common.by import By


def test_calendar_handling(chrome_driver):
    chrome_driver.get("https://www.goibibo.com/")
    chrome_driver.find_element(By.XPATH, "//span[text()='Departure']").click()

    # chrome_driver
    sleep(5)
    chrome_driver.find_element(By.XPATH, "(//p[text()='25'])[2]").click()
    # alldates = chrome_driver.find_elements(By.XPATH, "(//div[@class='DayPicker-Body'])[2]")
    # for dateelement in alldates:
    #     date = dateelement.text
    #     print(date)
    #     if date == '25':
    #         dateelement.click()
    #         break

    sleep(4)
    chrome_driver.find_element(By.XPATH, "//span[text()='Done']").click()
    sleep(4)
