from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome('webdriver/chromedriver.exe')
login = "https://shopee.co.id/buyer/login"
item = "https://shopee.co.id/product-i.39788460.7015534791?smtt=0.218879583-1605157013.9"

     
driver.get(login) #this is the link above
#username = driver.find_element_by_id("Username")
#password = driver.find_element_by_id("Password")
username = "saukiahmdd@gmail.com"
password = "12112045Apa"

AkunID = driver.find_element_by_class_name('_56AraZ')

while not driver.find_element_by_class_name('_56AraZ'):
    driver.refresh()

AkunID.send_keys(username)


AkunID.send_keys(Keys.TAB,password,Keys.ENTER)

# while not driver.find_element_by_class_name('_35rr5y _32qX4k _3SWXCx _2iOIqx _2h_2_Y'):
#     time.sleep(10)

# driver.driver.find_element_by_class_name('_35rr5y _32qX4k _3SWXCx _2iOIqx _2h_2_Y').click
# if 'okButton' in globals():
# okButton.click()

    # okButton = driver.find_element_by_class_name('_35rr5y _32qX4k _3SWXCx _2iOIqx _2h_2_Y')
    # okbtn = driver.find_element(By.CLASS_NAME, '_35rr5y _32qX4k _3SWXCx _2iOIqx _2h_2_Y')
# webdriver.ActionChains(driver).click(okbtn).perform()
    

time.sleep(20)

driver.get(item)


beli = wait.until(presence_of_element_located(By.CLASS_NAME, 'btn btn-solid-primary btn--l YtgjXY'))
beli.click()
# driver.find_elements_by_class_name('btn btn-solid-primary btn--l YtgjXY')
# for add in AddKeranjang:
#     add.click()

AddCheckout = driver.find_elements_by_class_name('shopee-button-solid shopee-button-solid--primary')
for addc in AddCheckout:
    addc.click()