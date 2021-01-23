import pyttsx3
import os,random,sys,time
from selenium.webdriver.common.keys import Keys
from urllib.parse import urlparse
from selenium import webdriver
from bs4 import BeautifulSoup
from countdown import countdown
import pyautogui
import pynput
import threading
from pynput.mouse import Button,Controller

mesin = pyttsx3.init()
file = open("Welcome.txt")
bacafile = file.readlines()
bacabaris1 = input("Masukan nama :")
bacabaris = bacafile[0]
bacabaris2 = bacafile[1]
bacabaris3 = bacafile[2]
bacabaris4 = bacafile[3]
bicara = mesin.say(bacabaris)
bicara1 = mesin.say(bacabaris1)
bicara2 = mesin.say(bacabaris2)
bicara3 = mesin.say(bacabaris3)
bicara4 = mesin.say(bacabaris4)
bicara = mesin.runAndWait()
print(bicara,bicara1,bicara2,bicara3,bicara4)



class waktu():
   def waktumundur():

        menit = 0
        detik = 0
        
        countdown(menit,detik)
class Menubot():
    def menubot():
        print("Menu Botacs Pro\n")
        print()
        print("1.autocheck")
        print("2.followIGDev")
class Autocheck():
    def autocheck(self):
        waktu.waktumundur()
        print("bot berjalan\n")
        browser = webdriver.Chrome('webdriver/chromedriver.exe')
        
        bukalist = open("linkcom.txt")
        bacafile = bukalist.readlines()
        targeturl = bacafile[0]
        browser.get(targeturl)
        browser.get('https://shopee.co.id/buyer/login?from=https%3A%2F%2Fshopee.co.id%2Fproduct-i.20287667.1410993379%3Fsmtt%3D0.218879583-1605157013.9&next=https%3A%2F%2Fshopee.co.id%2Fproduct-i.20287667.1410993379%3Fsmtt%3D0.218879583-1605157013.9&smtt=0.218879583-1605157013.9')
        bukafileakun = open("akun.txt")
        bacaakun = bukafileakun.readlines()
        username = bacaakun[0]
        password = bacaakun[1]
        AkunID = browser.find_element_by_class_name('_56AraZ')
        AkunID.send_keys(username)
        AkunID.send_keys(Keys.TAB,password,Keys.ENTER)
        
    def addkeranjang(self):
        self.driver.get('https://shopee.co.id/Alat-Perajang-Rajang-Penghancur-Pencacah-Cacah-Bawang-Garlic-Chopper-i.39788460.7015534791')
        time.sleep(1)
        addkeranjang_button = self.driver.find_element_by_class_name('btn btn-solid-primary btn--l YtgjXY')
        addkeranjang_button.send_keys(Keys.ENTER)

        print("Berhasil Checkout")

class FollowIGDev():
    def followIGDev(self):
        browser1 = webdriver.Chrome('webdriver/chromedriver.exe')

Menubot.menubot()
auto = Autocheck()
follow = FollowIGDev()

pilih = int(input("Pilih nomor dalam menu Botacs Pro:"))

if pilih==1:
    auto.autocheck()
elif pilih==2:
    follow.followIGDev()
else:
    exit()
