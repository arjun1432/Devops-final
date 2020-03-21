from selenium import webdriver
first = "Arjun"
last = "Dhirwan"
email = "arun.dhirwan@gmail.com"
password = "Arjun1432"
driver = webdriver.Chrome('chromedriver.exe')

driver.get("http://localhost/Devops/facebook/")
driver.find_element_by_id("first").send_keys(first)
driver.find_element_by_id("last").send_keys(last)
driver.find_element_by_id("email_register").send_keys(email)
driver.find_element_by_id("pass_register").send_keys(password)
driver.find_element_by_id("registerbutton").click()
