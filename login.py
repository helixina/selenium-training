from selenium import webdriver

with webdriver.Chrome(executable_path='/WebDriver/bin/chromedriver') as driver:
    driver.get("http://localhost/litecart/admin/login.php")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_css_selector("button").click()
