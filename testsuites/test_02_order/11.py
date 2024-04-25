from selenium import webdriver


#1、采购单位登录

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://login.zcygov.cn/login')
name = driver.find_element_by_id('username')
pwd = driver.find_element_by_id('password')
login = driver.find_element_by_xpath('//button[@class="ant-btn login-btn password-login ant-btn-primary"]')
name.clear()
name.send_keys('13222222')
pwd.clear()
pwd.send_keys('test123456')
login.click()
