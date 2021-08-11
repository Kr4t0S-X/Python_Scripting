import os
import openpyxl
from openpyxl import Workbook
import pandas as pd
import numpy as np
from selenium import webdriver
from time import sleep

tab = ["capgemini", "Fujitsu", "IBM", "infineon", "Tianma micro-electronics", "Amazon Web Services", "ON SEMICONDUCTOR", "Linkbynet", "Tata communications", "Flex", "ACCLIVIS TECHNOLOGIES", "Atos", "AT&T", "Deloitte", "Lenovo", "Mitsubishi electric", "Orange", "Planar systems", "Cognizant Technology", "Polycom", "ANALOG DEVICES", "MONDRAGON", "Dimension Data", "Altran", "Medallia", "Sogeti", "Keyrus", "ADVANTECH", "Econocom", "CGI Consulting", "CGI", "MURATA COMPANY", "Microfocus", "Kinvey", "Akamai", "Akka Technologies", "Autodesk", "GFI Informatique", "RICOH", "Sirva", "Korn/Ferry International", "ManPower", "British Telecom", "Cincinnati Bell"]
#wb = load_workbook('Workbook.xlsx')
#ws = wb.active()

#def first_search(self):
#    search_btn = self.driver.find_element_by_xpath('//*[@id="qsValue"]/span[2]/a')
#    search_btn.click()

#def other_searches(self):
#    search_btn = self.driver.find_element_by_xpath('//*[@id="qsValue"]/span[2]/a[2]')
#    search_btn.click()

#def search_bar_handling(self):
#    try:
#        self.first_search()
#    except Exception:
#        try:
#            self.other_searches()

class ssp():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://ssp-srm-sso.se.com/')

        sleep(15)
        
        #training_btn = self.driver.find_element_by_xpath('//*[@id="ext-gen1062"]/div[19]/div/div[3]/svg')
        #training_btn.click()

        supplier_btn = self.driver.find_element_by_xpath('//*[@id="shortcut_nav_suppliers"]')
        supplier_btn.click()

        sleep(5)

        x = 0

        for i in tab:
            
            self.driver.switch_to.frame(0)
            self.driver.switch_to.frame(0)
        
            sleep(2)

            search_bar = self.driver.find_element_by_xpath('//*[@id="qsValueInput"]')
            search_bar.send_keys(i)

            sleep(2)
            
            if x == 0:
                search_btn = self.driver.find_element_by_xpath('//*[@id="qsValue"]/span[2]/a')
            else:
                search_btn = self.driver.find_element_by_xpath('//*[@id="qsValue"]/span[2]/a[2]')
            search_btn.click()
             
            sleep (15)
            
            x+=1

            export_btn = self.driver.find_element_by_xpath('//*[@id="pageMenuItem_56"]/a/span')
            export_btn.click()

            sleep (5)
            
            base_window = self.driver.window_handles[0]
            self.driver.switch_to.window(self.driver.window_handles[1])

            sleep(2)

            self.driver.switch_to.frame(0)

            sendmail_btn = self.driver.find_element_by_xpath('//*[@id="page"]/div[3]/table/tbody/tr[4]/td[2]/label')
            sendmail_btn.click()

            sleep(2)

            dl_btn = self.driver.find_element_by_xpath('//*[@id="pageMenuItem_1"]/a/span')
            dl_btn.click()

            sleep (15)

            self.driver.switch_to.window(base_window)
            
            self.driver.switch_to.frame(0)
            self.driver.switch_to.frame(0)

            clear_btn = self.driver.find_element_by_xpath('//*[@id="qsValue"]/span[2]/a[1]')
            clear_btn.click()

            self.driver.switch_to.default_content()

bot = ssp()
bot.login()
