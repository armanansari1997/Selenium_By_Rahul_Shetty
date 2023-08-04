import time

from selenium import webdriver


def test_chrome_options_demo():
    option = webdriver.ChromeOptions()
    option.add_argument("--start-maximized")
    option.add_argument("headless")

    driver = webdriver.Chrome(executable_path='D://Drivers/chromedriver.exe')
    driver.get("https://www.google.com")
    time.sleep(3)