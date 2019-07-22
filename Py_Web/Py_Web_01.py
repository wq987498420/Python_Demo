from time import sleep
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://www.baidu.com")
driver.find_element_by_id("kw").send_keys("python")
driver.find_element_by_id("su").click()
sleep(3)
driver.close()