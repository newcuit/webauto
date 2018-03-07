#!usr/bin/env python
#-*- coding: utf-8 -*-

import os
import sys
import time
import pytesseract
from PIL import Image,ImageEnhance
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

username='liuchun12255'
password='NEW474892181N'

def ImageIdent(imagePath,imageLang):
    image = Image.open(imagePath)
    '''图片灰度化'''
    image = image.convert('RGBA')
    image = image.convert('L')

    '''
    WHITE, BLACK = 255, 0
    
    threshold=180 
    table=[]
    for  i  in  range(256):
        if  i  <  threshold:
            table.append(1)
        else :
            table.append(0)

    image  =  image.point(table,  '1')
    '''
    
    '''图片增强'''
    image = ImageEnhance.Contrast(image).enhance(4.0)
    image = ImageEnhance.Color(image).enhance(0.0)
    #image.show()

    code= pytesseract.image_to_string(image,lang=imageLang)
    image.close()
    
    return code
    
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
    
    while True:
        try:
            browser.switch_to.frame('x-URS-iframe')
            break
        except :
            print('未找到对应元素,准备重试..')
            time.sleep(1)
    
    browser.find_element_by_name('email').send_keys(username)
    browser.find_element_by_name('password').send_keys(password)
    browser.find_element_by_id('dologin').click()

    browser.save_screenshot('code.png')
    '''
    imgelement = browser.find_element_by_xpath('//img[@src="rand!loginRand.action"]')
    
    location = imgelement.location
    size = imgelement.size
    
    rangle = (int(location['x']),int(location['y']),int(location['x']+size['width']),int(location['y']+size['height']))
    
    Image.open("code.png").crop(rangle).save('code.jpg')
    
    authCode = ImageIdent('code.jpg',"eng")

    os.remove("code.jpg")
    os.remove("code.png")
    
    print ("图像识别验证码为："+authCode)
    '''
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
    
    authCode = ImageIdent('test.jpg',"eng")
    print('图像识别验证码为：'+authCode)

    
    webTest("http://mail.163.com",webLoopTest)

    
if __name__ == "__main__":
    main();

