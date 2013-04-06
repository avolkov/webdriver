#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException, \
    ElementNotVisibleException
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def wait_for_el(dr):
    return  len(dr.find_elements_by_class_name('l')) and \
        len(dr.find_elements_by_id('pnnext'))

def next_page(dr):
    next_page = dr.find_element_by_id('pnnext')
    next_page.click()


'''
### Chrome driver doesn't seem to work. Is it because both chrome and chromium
### are installed on the system?
import ipdb; ipdb.set_trace()
options = webdriver.ChromeOptions()
driver = webdriver.Remote(
    command_executor='http://localhost:9515/wd/hub',
    desired_capabilities=options.to_capabilities())

driver = webdriver.Chrome('/home/alex/git/selenium/java/chrome/chromedriver')
'''
driver = webdriver.Firefox()
wait = ui.WebDriverWait(driver,2)
driver.get('http://www.google.com')
element = driver.find_element_by_id("gbqfq")
element.send_keys('hello, world')
element.send_keys(Keys.RETURN)
del element
for count in range(0,800):
    wait.until(wait_for_el)
    print "Current URL: ", driver.current_url
    for element in driver.find_elements_by_class_name('l'):
        try:
            print element.get_attribute('href')
        except (StaleElementReferenceException, ElementNotVisibleException):
            pass

    while True:
        try:
            next_page(driver)
            break
        except (StaleElementReferenceException, ElementNotVisibleException):
            pass


driver.close()