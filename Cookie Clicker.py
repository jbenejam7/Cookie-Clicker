# Selenium Tutorial #1
# https://sites.google.com/a/chromium.org/chromdriver/downloads
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#AUTOCHAIN AND AUTOMATION
PATH = "C:\Program Files (x86)\chromdriver.exe"
driver = webdriver.Chrome(service=Service(PATH))
driver.get("https://orteil.dashnet.org/cookieclicker/")



lang_select = ActionChains(driver)
driver.implicitly_wait(5)
language = driver.find_element(By.ID, "langSelect-EN").click()


driver.get("https://orteil.dashnet.org/cookieclicker/")
cookie_count = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#cookies")))
cookie = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#bigCookie")))
#items = [driver.find_element(By.ID, "productPrice" + str(i) for i in range(1,-1,-1))]


for i in range(5000):
    ActionChains(driver).click(cookie).perform()
    # count = int(cookie_count.text.split(" ")[0])
    items = [driver.find_element(By.ID, "productPrice" + str(i)) for i in range(1,-1,-1)]
    for item in items: 
    	count = int(cookie_count.text.split(" ")[0])
    	value = int(item.text.replace(',', ''))
    	if value <= count:
    		upgrade_actions = ActionChains(driver)
    		upgrade_actions.move_to_element(item)
    		upgrade_actions.click()
    		upgrade_actions.perform()



while(True):
	pass


