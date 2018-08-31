#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'wangrong'
from selenium import webdriver
import selenium.webdriver.support.ui as ui
from time import sleep
url="http://172.16.80.3/portal-web/#"
driver=webdriver.Chrome()
wait = ui.WebDriverWait(driver,10)
driver.get(url)
#driver.get(r"C:/Users/cc/Desktop/test/bss-web.html")
#print ("dir(driver)",dir(driver.window_handles))
print ("title of current page is %s",driver.title)
print ("url of current page is %s",driver.current_url)
wait.until(lambda driver: driver.find_element_by_xpath("//div[@class='form-group has-feedback']/input[@name='userCode']"))

##driver.find_element_by_id('loginUserCode').click()
driver.find_element_by_xpath("//div[@class='form-group has-feedback']/input[@name='userCode']").send_keys('admin')
wait.until(lambda driver: driver.find_element_by_xpath("//div[@class='form-group has-feedback']/input[@name='password']"))
driver.find_element_by_xpath("//div[@class='form-group has-feedback']/input[@name='password']").click()
driver.find_element_by_xpath("//div[@class='form-group has-feedback']/input[@name='password']").send_keys('123')

driver.find_element_by_xpath("//div[@class='form-group']/button[@type='button']").click()
sleep(2)
#driver.switch_to_window(driver.window_handles[1])
try:
    text=driver.find_element_by_xpath("//*[@id='portalMainHeader']/div/div[2]/div/div[1]/input").text
    print("Login success")
    driver.quit()
except Exception as err:
    print ("Login failed")