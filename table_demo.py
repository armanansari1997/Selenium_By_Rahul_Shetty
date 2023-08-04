from selenium.webdriver.common.by import By


def test_table_demo(chrome_driver):
    chrome_driver.get("https://www.learning.npntraining.com/selenium-practice/advance_locators/table.html")
    list = chrome_driver.find_elements(By.CSS_SELECTOR, 'table thead th')
    for item in list:
        print(item.text)

    capgemini = chrome_driver.find_element(By.CSS_SELECTOR, 'table tbody tr:nth-child(5)')
    print(capgemini.text)