# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest

class NewContactTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_new_contact(self):
        driver = self.driver
        driver.get("http://172.17.41.29/addressbook/")
        driver.find_element_by_name("user").click()
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys("admin")
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys("secret")
        driver.find_element_by_xpath("//input[@value='Login']").click()
        driver.find_element_by_link_text("add new").click()
        driver.find_element_by_name("firstname").click()
        driver.find_element_by_name("firstname").clear()
        driver.find_element_by_name("firstname").send_keys("Maxim")
        driver.find_element_by_name("middlename").clear()
        driver.find_element_by_name("middlename").send_keys("Olegovich")
        driver.find_element_by_name("lastname").clear()
        driver.find_element_by_name("lastname").send_keys("Vasilyev")
        driver.find_element_by_name("nickname").clear()
        driver.find_element_by_name("nickname").send_keys("MaXj")
        driver.find_element_by_name("title").clear()
        driver.find_element_by_name("title").send_keys("Genius")
        driver.find_element_by_name("company").clear()
        driver.find_element_by_name("company").send_keys("TechArgos")
        driver.find_element_by_name("address").clear()
        driver.find_element_by_name("address").send_keys("Novodmitrovskaya 2b")
        driver.find_element_by_name("home").clear()
        driver.find_element_by_name("home").send_keys("-")
        driver.find_element_by_name("mobile").clear()
        driver.find_element_by_name("mobile").send_keys("70418041804")
        driver.find_element_by_name("work").clear()
        driver.find_element_by_name("work").send_keys("aslfalf")
        driver.find_element_by_name("fax").clear()
        driver.find_element_by_name("fax").send_keys("fjafafasj")
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys("vasiafaf@gmail.com")
        driver.find_element_by_name("email2").clear()
        driver.find_element_by_name("email2").send_keys("fjajfafs@yandex.ru")
        driver.find_element_by_name("email2").send_keys(Keys.DOWN)
        driver.find_element_by_name("email2").send_keys(Keys.TAB)
        driver.find_element_by_name("email3").clear()
        driver.find_element_by_name("email3").send_keys("kfjajfakfa@rambler.com")
        driver.find_element_by_name("homepage").clear()
        driver.find_element_by_name("homepage").send_keys("asfakjfla.ru")
        Select(driver.find_element_by_name("bday")).select_by_visible_text("15")
        driver.find_element_by_xpath("//option[@value='15']").click()
        driver.find_element_by_name("bmonth").click()
        Select(driver.find_element_by_name("bmonth")).select_by_visible_text("November")
        driver.find_element_by_xpath("//option[@value='November']").click()
        driver.find_element_by_name("byear").click()
        driver.find_element_by_name("byear").clear()
        driver.find_element_by_name("byear").send_keys("1998")
        driver.find_element_by_name("aday").click()
        Select(driver.find_element_by_name("aday")).select_by_visible_text("16")
        driver.find_element_by_xpath("//div[@id='content']/form/select[3]/option[18]").click()
        driver.find_element_by_name("amonth").click()
        Select(driver.find_element_by_name("amonth")).select_by_visible_text("July")
        driver.find_element_by_xpath("//div[@id='content']/form/select[4]/option[8]").click()
        driver.find_element_by_name("ayear").click()
        driver.find_element_by_name("ayear").clear()
        driver.find_element_by_name("ayear").send_keys("1987")
        driver.find_element_by_name("address2").click()
        driver.find_element_by_name("address2").clear()
        driver.find_element_by_name("address2").send_keys("zxvkzlvjz")
        driver.find_element_by_name("phone2").clear()
        driver.find_element_by_name("phone2").send_keys("afkjalfjaljf")
        driver.find_element_by_name("notes").clear()
        driver.find_element_by_name("notes").send_keys("ksdljgslgjksl")
        driver.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        driver.find_element_by_link_text("home page").click()
        driver.find_element_by_link_text("Logout").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
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
