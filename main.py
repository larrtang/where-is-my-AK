#!/usr/bin/python3

from bs4 import BeautifulSoup
import requests
from lxml import html
from selenium import webdriver
import os
from TwilioClient import TwilioClient
from WebScraper import WebScraper
import time

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}
url = "https://palmettostatearmory.com/ar-15/ar15-guns.html"
#url = "https://palmettostatearmory.com/guns/ak-rifles-pistols.html"


def set_viewport_size(driver, width, height):
    window_size = driver.execute_script("""
        return [window.outerWidth - window.innerWidth + arguments[0],
          window.outerHeight - window.innerHeight + arguments[1]];
        """, width, height)
    driver.set_window_size(*window_size)


def main():

    os.environ['webdriver.chrome.driver'] = './chromedriver'
    #twilio = TwilioClient()

    while (True):
        browser = webdriver.Chrome(executable_path="./chromedriver")
        browser.set_window_size(1600, 900) # fu*k reCAPTCHA
        print(browser.execute_script("return [window.innerWidth, window.innerHeight];"))
        browser.get(url)
        
        soup = BeautifulSoup(browser.execute_script("return document.body.innerHTML"), "lxml")
        
        os.system("pkill chromedriver")
        os.system("pkill chrome")
        
        stock = soup.findAll("li", {"class": "item product product-item"})
        print('--------------------------\n\n\n\n\n\n\n--------------------------')
        print("Number of items=", len(stock))
        msg  = "In Stock Now!\n"
        is_anything_in_stock = False

        for item in stock:
            item_soup = BeautifulSoup(str(item), "lxml")
            item_name = item_soup.find("a", {"class" : "product-item-link"}).text.replace("\n", "")
            print(item_name)
            in_stock = item_soup.find("button", {"title" : "Add to Cart"})
            if in_stock is not None:   # in stock
                msg += item_name + "\n"
                is_anything_in_stock = True

        if is_anything_in_stock:  
            print(msg)
            #twilio.sendMessage(msg)
            cmd = "echo '"+msg +"'| mail -s 'Get the fuck onto PSA and buy shit' larrtang@gmail.com"
            print(cmd)
            os.system(cmd)
            time.sleep(60*15)
        else:                   
            time.sleep(60)


if __name__ == "__main__":
    main()

