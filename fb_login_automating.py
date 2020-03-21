from selenium import webdriver
email = "arun.dhirwan@gmail.com"
password = "Arjun1432"
driver = webdriver.Chrome('chromedriver.exe')

driver.get("https://www.facebook.com/")
driver.find_element_by_id("email").send_keys(email)
driver.find_element_by_id("pass").send_keys(password)
driver.find_element_by_id("u_0_b").click()
