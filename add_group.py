# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

success = True
wd = WebDriver()
wd.implicitly_wait(60)

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

try:
    wd.get("http://localhost/addressbook/group.php")
    wd.find_element_by_name("pass").click()
    wd.find_element_by_name("pass").send_keys("\\undefined")
    wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()
    wd.find_element_by_name("new").click()
    wd.find_element_by_name("group_name").click()
    wd.find_element_by_name("group_name").clear()
    wd.find_element_by_name("group_name").send_keys("rytyrtytry")
    wd.find_element_by_name("group_header").click()
    wd.find_element_by_name("group_header").send_keys("\\89")
    wd.find_element_by_name("group_header").click()
    wd.find_element_by_name("group_header").clear()
    wd.find_element_by_name("group_header").send_keys("trytryrty")
    wd.find_element_by_name("group_footer").click()
    wd.find_element_by_name("group_footer").clear()
    wd.find_element_by_name("group_footer").send_keys()
    wd.find_element_by_name("group_footer").click()
    wd.find_element_by_name("group_footer").clear()
    wd.find_element_by_name("group_footer").send_keys("tryrtytrytry")
    wd.find_element_by_name("submit").click()
    wd.find_element_by_link_text("group page").click()
    wd.find_element_by_link_text("Logout").click()
    wd.find_element_by_name("pass").click()
    wd.find_element_by_name("pass").send_keys("\\undefined")
    wd.find_element_by_name("user").click()
    wd.find_element_by_name("user").send_keys("\\undefined")
finally:
    wd.quit()
    if not success:
        raise Exception("Test failed.")
