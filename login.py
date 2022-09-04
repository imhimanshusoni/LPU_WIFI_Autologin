import time
from selenium import webdriver
driver = webdriver.Firefox(executable_path='/home/himanshu/Downloads/gk/geckodriver')
driver.get('https://internet.lpu.in/24online/webpages/client.jsp')
time.sleep(1)
name = "ur_username"
passwd = "ur_password"
button1 = driver.find_element("id",'agreepolicy')
button1.click()
usrbox = driver.find_element("name",'username')
passbox = driver.find_element("name",'password')
usrbox.send_keys(name)
passbox.send_keys(passwd)
button = driver.find_element("id",'loginbtn')
button.click()
