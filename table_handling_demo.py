from selenium.webdriver.common.by import By


def test_table_handling_demo(chrome_driver):
    chrome_driver.get("https://www.learning.npntraining.com/selenium-practice/webcontrols/Table.html")
    thead = chrome_driver.find_elements(By.CSS_SELECTOR, 'table > thead > tr > th')
    for x in thead:
        print(x.text)

    tbody = chrome_driver.find_elements(By.CSS_SELECTOR, 'tbody > tr')
    for x in tbody:
        print(x.text)