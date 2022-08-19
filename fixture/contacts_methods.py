from selenium import webdriver
from fixture.contact import ContactHelper
from fixture.session import SessionHelper


class help_methods:
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.contact = ContactHelper(self)

    def open_test_page(self):
        wd = self.wd
        wd.get("http://172.17.41.29/addressbook/")

    def return_to_home_page(self):
        wd = self.wd
        wd.find_element_by_link_text("home page").click()

    def destroy(self):
        self.wd.quit()