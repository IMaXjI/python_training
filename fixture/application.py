from selenium import webdriver
from fixture.session import SessionHelper

class Application:
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)


    def return_to_groups_page(self):
        wd = self.wd
        wd.find_element_by_link_text("groups").click()


    def create_group(self, group):
        wd = self.wd
        # Init group creation
        wd.find_element_by_name("new").click()
        # Fill group info
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # Submit creation
        wd.find_element_by_name("submit").click()

    def open_group_page(self):
        wd = self.wd
        wd.find_element_by_link_text("groups").click()


    def open_home_page(self):
        wd = self.wd
        wd.get("http://172.17.41.29/addressbook/")

    def destroy(self):
        self.wd.quit()
