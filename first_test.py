from selenium.webdriver import Chrome

driver = Chrome(executable_path='/WebDriver/bin/chromedriver')

driver.get("https://google.com/")

driver.quit()
