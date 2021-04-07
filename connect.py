import os
import sys
import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.options import Options
import yaml

firefox_opt = Options()
firefox_opt.add_argument('--headless')
firefox_opt.add_argument('--disable-gpu')
firefox_opt.add_argument('--window-size=1366,768')
firefox_opt.add_argument("--no-sandbox")

with open('./userinfo.yaml', 'r') as f:
    config_data = yaml.load(f, Loader=yaml.FullLoader)
username = config_data['username']
password = config_data['password']

def connect():
    driver = webdriver.Firefox(options=firefox_opt)
    url = 'http://net.tsinghua.edu.cn/wired/'
    driver.get(url)
    time.sleep(1)

    online = True

    try:
        driver.find_element_by_xpath('/html/body/div/div[5]/button')
        print('already online')
    except:
        print('not online')
        online = False

    if not online:
        try:
            print('connecting...')
            user_name = driver.find_element_by_xpath('//*[@id="uname"]')
            time.sleep(1)
            user_name.send_keys(username)
            passwd = driver.find_element_by_xpath('//*[@id="pass"]')
            time.sleep(1)
            passwd.send_keys(password)
            connect_buttom = driver.find_element_by_xpath('//*[@id="connect"]')
            time.sleep(1)
            connect_buttom.click()
            time.sleep(1)
        except:
            print('Cannot connect')

    print('testing...')
    test_driver = webdriver.Firefox(options=firefox_opt)
    test_driver.get(url)
    time.sleep(1)

    try:
        test_driver.find_element_by_xpath('/html/body/div/div[5]/button')
        print('already online')
    except:
        print('not online')

    driver.quit()
    test_driver.quit()

if __name__ == "__main__":
    if sys.argv[1] == '1':
        connect()
    elif sys.argv[1] == '2':
        while True:
            connect()
            time.sleep(600)
    else:
        print('Use method:\n python auto_login.py 1\t(single login)')
        print(' python auto_login.py 2\t(login every ten minutes)')