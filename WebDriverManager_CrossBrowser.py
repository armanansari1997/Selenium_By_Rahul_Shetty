from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from webdrivermanager import ChromeDriverManager, GeckoDriverManager, EdgeDriverManager, EdgeChromiumDriverManager

browserName = "edge"

if browserName == "chrome":
    driver = webdriver.Chrome(ChromeDriverManager().install())
elif browserName == "firefox":
    driver = webdriver.Chrome(GeckoDriverManager().install())

elif browserName == "edge":
    driver = webdriver.Chrome(executable_path=EdgeChromiumDriverManager().install())
else:
    print("Please pass the correct browser name : " + browserName)

driver.implicitly_wait(5)
driver.get("https://www.google.com")
driver.find_elemen(By.NAME,'q').send_keys("Python Course")

time.sleep(5)
driver.quit()
