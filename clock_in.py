from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import time
import random
random.seed(2021)


def clock_in(account, password):
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # hide the cmd window
    driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe',  # path of corresponding webdriver
                              options=chrome_options)

    driver.get('https://ehall.neu.edu.cn/db_portal/guide?id=D06BDA87-2E6E-4324-A14D-3BFAD839F2B9')  # web page of NEU check-in 
    time.sleep(3 * random.random())
    driver.maximize_window()

    driver.find_element_by_css_selector('input[value="我要办理"]').click()
    time.sleep(5 * random.random())
    driver.switch_to.window(driver.window_handles[-1])
    id_input = driver.find_element_by_id('un')
    pd_input = driver.find_element_by_id('pd')
    id_input.send_keys(account)
    pd_input.send_keys(password)
    driver.find_element_by_id('index_login_btn').click()
    time.sleep(5 * random.random())

    driver.find_element_by_xpath('//*[@id="app"]/main/div/form/div[1]/table/tbody/tr/td[1]/div/div/div/label[1]') \
        .click()
    time.sleep(2 * random.random())
    driver.find_element_by_xpath('//*[@id="app"]/main/div/form/div[3]/div[2]/table/tbody/tr[1]/td/div/div/div/label[1]') \
        .click()
    time.sleep(2 * random.random())
    driver.find_element_by_xpath('//*[@id="app"]/main/div/form/div[4]/div[2]/table/tbody/tr[1]/td/div/div/div/label[1]') \
        .click()

    time.sleep(3 * random.random())
    driver.find_element_by_css_selector('button[type="button"][class="el-button el-button--primary"]').click()

    driver.quit()
