#!usr/bin/env python
#-*- coding: utf-8 -*-

import os
import sys
import time
import pytesseract
from PIL import Image,ImageEnhance
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

testUrl="https://www.amazon.com/s/ref=sr_pg_2?fst=p90x%3A1&rh=i%3Aaps%2Ck%3AWake-Up+Light+Electronic+Alarm&page=2&keywords=Wake-Up+Light+Electronic+Alarm&ie=UTF8&qid=1509677643"   

class webChrome:
    browser=None
    loopFunc=None
    
    def __init__(self,work):
        print('InIt webdriver....')
        chromedriver = "C:\Python27\chromedriver.exe"
        chromeOptions = webdriver.ChromeOptions()
        chromeOptions.add_argument("--start-maximized")
        os.environ["webdriver.chrome.driver"] = chromedriver
        
        self.browser = webdriver.Chrome(chromedriver,chrome_options=chromeOptions)
        self.loopFunc = work;
        
    def open(self,url):
        print('Open web url: '+url)
        self.browser.get(url)
        
    def loop(self):
        self.loopFunc(self.browser)
        
    def close(self):
        self.browser.quit();


def webLoopTest(browser):
    print('运行测试程序')
    
    #browser.find_element_by_id('dologin').click()
    print (browser.find_element_by_class_name('s-result-item celwidget').get_attribute('id'))

    time.sleep(3)

    print('即将退出程序!!!')
    
    return 0

def webTest(url,func):
    web_browser = webChrome(func)
    web_browser.open(url);
    print('打开Chrome成功')

    web_browser.loop()

    time.sleep(3)
    web_browser.close()

def main():
    global sysCodeType
    
    webTest(testUrl,webLoopTest)

    
if __name__ == "__main__":
    main();

