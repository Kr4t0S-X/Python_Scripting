from selenium import webdriver

#webdriver.Chrome(executable_path=r'C:\webdriver\chromedriver.exe') # to open the chromebrowser 
#driver.get("https://web.whatsapp.com")

url = 'https://ssp-srm-sso.se.com'
browser = webdriver.Chrome()
browser.get(url)

supplier_db = browser.find_element_by_xpath('//*[@id="shortcut_nav_3999"]')
supplier_db.click()

browser.switch_to.frame(0)
browser.switch_to.frame(0)

search_bar = browser.find_element_by_xpath('//*[@id="qsValueInput"]')
search_bar.send_keys('480873868')

#if x == 0:
search_btn = browser.find_element_by_xpath('//*[@id="qsValue"]/span[2]/a')
#else:
#   search_btn = self.driver.find_element_by_xpath('//*[@id="qsValue"]/span[2]/a[2]')

search_btn.click()

#browser.switch_to_frame(0)
#browser.switch_to.frame(1)
#browser.switch_to.frame(2)
#browser.switch_to.frame(3)
#browser.switch_to.default_content()
#iframe = browser.find_elements_by_name('frmMain')
Table = browser.find_element_by_class_name('listContainer')
print(Table)
#browser.switch_to.frame(iframe)
# select_supplier = browser.find_element_by_xpath('//*[@id="fab2571a414d17c86343e4009bf2235d~c01687b19a643b1616b0b25919e4e400~a2a97846896563c52f2aa234e2200234~a2a97846896563c52f2aa234e2200234~a2a97846896563c52f2aa234e2200234~a2a97846896563c52f2aa234e2200234"]/td[4]')
# select_supplier_2 = browser.find_element_by_xpath('//*[@id="fab2571a414d17c86343e4009bf2235d~c01687b19a643b1616b0b25919e4e400~a2a97846896563c52f2aa234e2200234~a2a97846896563c52f2aa234e2200234~a2a97846896563c52f2aa234e2200234~a2a97846896563c52f2aa234e2200234"]/td[4]/table/tbody/tr/td/table/tbody/tr/td[2]/b')
# select_supplier_3 = browser.find_element_by_xpath('//*[@id="customers"]/tbody/tr')
# select_supplier_4 = browser.find_element_by_xpath('//*[@id="rowActionsExpanded_dbd340cdf9032b4b4f93c765970d88a5~9f503fbd7d120b994d731131b32dfcb0~4ceff34e92f975f81e9679588296b93a~4ceff34e92f975f81e9679588296b93a~4ceff34e92f975f81e9679588296b93a~4ceff34e92f975f81e9679588296b93a"]/li[2]')
# select_supplier_5 = browser.find_element_by_xpath('//*[@id="supplierSearchListForm"]/div[2]/div[5]')
# select_supplier.click()
# select_supplier_2.click()
# select_supplier_3.click()
# select_supplier_4.click()
# select_supplier_5.click()
