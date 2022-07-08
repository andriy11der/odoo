"""libraries"""
import io
import random
import datetime
from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


logs_file = 'tracking_logs.log'
f = open(logs_file, "w")
f.write(f"start, {datetime.datetime.now()}\n")
f.close()
f = open(logs_file, "a")


def browser():
    try:
        chrome_options = webdriver.ChromeOptions()
        #chrome_options = Options()
        #chrome_options.add_argument("--headless")
        #chrome_options.setBinary("/home/andriy/PycharmProjects/mytower/chromedriver_linux64/chromedriver")
        chrome_options.add_argument("start-maximized")
        #chrome_options.add_argument("--blink-settings=imagesEnabled=false")
        chrome = webdriver.Chrome("/home/andriy/PycharmProjects/mytower/chromedriver_linux64/chromedriver")
        return chrome
    except Exception as e:
        print(e)


def open_site(chrome):
    try:
        chrome.switch_to.window(chrome.window_handles[0])
        chrome.get('https://erp.smartteksas.com/web/login#action=593&cids=1&menu_id=422&model=account.analytic.line&view_type=list')
        chrome.implicitly_wait(5)
        f.write(f"successful opened site, {datetime.datetime.now()}\n")
        print('site is opened')
        sleep(4)
        input_element = chrome.find_element_by_name("login")
        input_element.send_keys('andrii.derepashchuk@smartteksas.com')
        input_element = chrome.find_element_by_name("password")
        input_element.send_keys('pjVr79LKrksuiX3')
        sleep(4)
        chrome.execute_script("document.querySelector('#wrapwrap > main > div > form > div.clearfix.oe_login_buttons.text-center.mb-1.pt-3 > button').click()")
        f.write(f"successful logged in, {datetime.datetime.now()}\n")
        print('logged in to the account')
        sleep(5)
    except Exception as e:
        f.write(f"Failed at opening and logging {e}, {datetime.datetime.now()}\n")
        print(e)


def sed_click(chrome):
    chrome.execute_script(
            "window.triggerMouseEvent = function triggerMouseEvent (node, eventType) { var clickEvent = document.createEvent ('MouseEvents'); clickEvent.initEvent (eventType, true, true); node.dispatchEvent (clickEvent); }")


def create_date(chrome):
    try:
        sleep(5)
        chrome.execute_script("document.querySelector('body > div.o_action_manager > div > div.o_control_panel > div.o_cp_bottom > div.o_cp_bottom_left > div > div > button.btn.btn-primary.o_list_button_add > span').click()")
        chrome.implicitly_wait(10)
        sleep(5)
        print("create clicked")
        f.write(f"create clicked, {datetime.datetime.now()}\n")

        try:
            chrome.execute_script("document.querySelector('input[name=\'date\']').value = '08/07/2024';")
        except:
            print("An exception occurred")

        chrome.implicitly_wait(10)
        sleep(5)
        print("date filled")
        f.write(f"date filled, {datetime.datetime.now()}\n")
        #chrome.execute_script("document.querySelector('#datepicker1437 > input').click()")
        #chrome.implicitly_wait(10)
        #sleep(5)
        #chrome.execute_script("document.querySelector('body > div.o_action_manager > div > div.o_content > div > div.table-responsive > table > tbody > tr.o_data_row.o_selected_row > td.o_data_cell.o_field_cell.o_list_many2one.o_required_modifier.o_invalid_cell > div > div > input').click()")
        #chrome.implicitly_wait(10)
        #sleep(5)
        #chrome.execute_script("document.querySelector('#ui-id-15').click()")
        #chrome.implicitly_wait(10)
        sleep(5)
        chrome.execute_script("document.querySelector('body > div.o_action_manager > div > div.o_content > div > div.table-responsive > table > tbody > tr.o_data_row.o_selected_row > td.o_data_cell.o_field_cell.o_list_many2one.o_task_with_hours_cell > div > div > input').click()")
        chrome.implicitly_wait(10)
        sleep(5)
        chrome.execute_script("document.querySelector('#ui-id-29').click()")
        chrome.implicitly_wait(10)
        sleep(5)
        input_element = chrome.find_element_by_name("name")
        input_element.send_keys('testing')
        sleep(5)
        input_element = chrome.find_element_by_name("unit_amount")
        input_element.send_keys('8')
        chrome.execute_script("document.querySelector('body > div.o_action_manager > div > div.o_control_panel > div.o_cp_bottom > div.o_cp_bottom_left > div > div > button.btn.btn-primary.o_list_button_save > span').click()")
        chrome.implicitly_wait(10)
        sleep(5)
        f.write(f"created, {datetime.datetime.now()}\n")
        print("created")
        sleep(10)
    except Exception as e:
        f.write(f"Failed at creating {e},  {datetime.datetime.now()}\n")
        print(e)
        print(f"Failed at creating")

def main():
    chrome = browser()
    open_site(chrome)
    #sed_click(chrome)
    create_date(chrome)


if __name__ == '__main__':
    main()
