def test_js_executor_demo(chrome_driver):
    chrome_driver.get("")
    chrome_driver.execute_script("window.scrollTo(0,500);")  # Vertically Scrolling
    chrome_driver.execute_script("window.scrollTo(500,0);")  # Horizontally Scrolling
    chrome_driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # Vertically Scrolling





























    chrome_driver.execute_script("window.scrollTo(0,500);")
    chrome_driver.execute_script("window.scrollTo(500,0);")
    chrome_driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
