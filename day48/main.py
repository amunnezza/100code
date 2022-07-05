from selenium import webdriver 
chrome_driver_path = "C:/Users/ciotola/development/chromedriver/chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.amazon.it")

#driver.close() #close the tab
driver.quit() #shut down the entire browser


