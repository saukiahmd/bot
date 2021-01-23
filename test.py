from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome('webdriver/chromedriver.exe')
login = "https://id-id.facebook.com/"
item = "https://shopee.co.id/product-i.39788460.7015534791?smtt=0.218879583-1605157013.9"

     
driver.get(login) #this is the link above
#username = driver.find_element_by_id("Username")
#password = driver.find_element_by_id("Password")
beli = WebDriverWait(driver,10).until(EC.elementToBeClickable((By.XPATH, "//button[@type='button' and contains(.,'Sign In')]")))
# beli.click()
time.sleep(5)

# AddCheckout = driver.find_elements_by_class_name('_42ft _4jy0 _6lth _4jy6 _4jy1 selected _51sy')
# AddCheckout.click()
