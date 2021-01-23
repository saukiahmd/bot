import account

import time

print(account.email)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class CheckOutBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.shopee.co.id/")

    def login(self, email, password):
        self.driver.get("https://shopee.co.id/buyer/login?next=https%3A%2F%2Fshopee.co.id%2F")
        time.sleep(5)
        email_input = self.driver.find_element_by_name("loginKey")
        email_input.clear()
        email_input.send_keys(email)
        pass_input = self.driver.find_element_by_name("password")
        pass_input.clear()
        pass_input.send_keys(password)
        self.driver.find_element_by_class_name("_35rr5y _32qX4k _1ShBrl _3z3XZ9 _2iOIqx _2h_2_Y").click()



if __name__ == "__main__":
    checkout_bot = CheckOutBot()

    checkout_bot.login(account.email, account.password)

    checkout_bot.checkout()
    time.sleep(20)