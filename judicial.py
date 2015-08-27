# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Judicial(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://jirs.judicial.gov.tw/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_judicial(self):
        driver = self.driver
        driver.get(self.base_url + "//FJUD/FJUDQRY01_1.aspx")
        Select(driver.find_element_by_name("v_court")).select_by_visible_text(u"臺灣臺北地方法院")
        # ERROR: Caught exception [Error: Dom locators are not implemented yet!]
        driver.find_element_by_name("dy1").clear()
        driver.find_element_by_name("dy1").send_keys("103")
        driver.find_element_by_name("dm1").clear()
        driver.find_element_by_name("dm1").send_keys("1")
        driver.find_element_by_name("dd1").clear()
        driver.find_element_by_name("dd1").send_keys("1")
        driver.find_element_by_name("dy2").clear()
        driver.find_element_by_name("dy2").send_keys("103")
        driver.find_element_by_name("dm2").clear()
        driver.find_element_by_name("dm2").send_keys("5")
        driver.find_element_by_name("dd2").clear()
        driver.find_element_by_name("dd2").send_keys("30")
        driver.find_element_by_name("Button").click()
        driver.find_element_by_link_text(u"103,婚,51").click()
        driver.find_element_by_link_text(u"下一筆").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
