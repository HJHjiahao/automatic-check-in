from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import time
import random
random.seed(2021)


sites = ['白塔', '全运路', '万达', '奥体', '青年大街']  # fill in the location randomly
site = sites[random.randrange(0, len(sites))]


def submit_file(account, password, site):
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # hide the cmd window
    driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe',  # path of corresponding webdriver
                              options=chrome_options)

    driver.get('https://ehall.neu.edu.cn/db_portal/guide?id=DBEB1E6B-F131-45FE-B7CB-A183AD521912')  # web page of NEU filing
    time.sleep(3 * random.random())
    driver.maximize_window()

    driver.find_element_by_css_selector('input[value="我要办理"]').click()
    time.sleep(5 * random.random())
    driver.switch_to.window(driver.window_handles[-1])

    driver.find_element_by_id('un').send_keys(account)
    driver.find_element_by_id('pd').send_keys(password)
    driver.find_element_by_id('index_login_btn').click()
    time.sleep(5 * random.random())
    hms = time.strftime('%H:%M', time.localtime())
    x = random.randrange(2, 4)
    future = str(int(hms[0:2]) + x) + ':' + '35'
    driver.find_element_by_xpath('//*[@id="V1_CTRL80"]').send_keys(hms)
    time.sleep(2 * random.random())
    driver.find_element_by_xpath('//*[@id="V1_CTRL82"]').send_keys(future)
    time.sleep(2 * random.random())
    driver.find_element_by_xpath('//*[@id="V1_CTRL92_0"]').send_keys(site)
    time.sleep(3 * random.random())
    buttons = driver.find_elements_by_css_selector('a[class="command_button_content"]')
    buttons[1].click()
    time.sleep(3 * random.random())
    driver.find_element_by_css_selector('button[class="dialog_button default rightest fr"]').click()
    time.sleep(3 * random.random())
    driver.find_element_by_css_selector('button[class="dialog_button default rightest fr"]').click()

    driver.quit()

    
