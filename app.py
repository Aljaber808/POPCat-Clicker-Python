import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(r'PATH-TO-chromedriver.exe')
driver.maximize_window()
driver.get("https://popcat.click/")

action = webdriver.common.action_chains.ActionChains(driver)
counter = 0
while counter < 1:
	element = driver.find_element_by_id('app')
	ActionChains(driver) \
	.key_down(Keys.CONTROL) \
	.click(element) \
	.key_up(Keys.CONTROL) \
	.perform()
	

driver.close()
