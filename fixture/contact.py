from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


class ContactHelper:
    def __init__(self, app):
        self.app = app


    def create(self, contact):
        wd = self.app.wd
        # Init contact creation
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        # Submit addition
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.filling_condition_check("firstname", contact.firstname)
        self.filling_condition_check("middlename", contact.middlename)
        self.filling_condition_check("lastname", contact.lastname)
        self.filling_condition_check("nickname", contact.nickname)
        self.filling_condition_check("title", contact.title)
        self.filling_condition_check("company", contact.company)
        self.filling_condition_check("address", contact.address)
        self.filling_condition_check("home", contact.home_phone)
        self.filling_condition_check("mobile", contact.cell_phone)
        self.filling_condition_check("work", contact.work_phone)
        self.filling_condition_check("fax", contact.fax)
        self.filling_condition_check("email", contact.email_1)
        self.filling_condition_check("email2", contact.email_2)
        self.filling_condition_check("email3", contact.email_3)
        self.filling_condition_check("homepage", contact.homepage)
        Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.day)
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.month)
        self.filling_condition_check("byear", contact.year)
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text(contact.a_day)
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(contact.a_month)
        self.filling_condition_check("ayear", contact.year)
        self.filling_condition_check("address2", contact.address2)
        self.filling_condition_check("phone2", contact.secondary_phone)
        self.filling_condition_check("notes", contact.notes)

    def filling_condition_check(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete(self):
        wd = self.app.wd
        # Select first contact
        wd.find_element_by_name("selected[]").click()
        # Submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()


    def edit(self, new_contact_data):
        wd = self.app.wd
        # Edit first contact
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[3]/td[8]/a/img").click()
        self.fill_contact_form(new_contact_data)
        # Submit update
        wd.find_element_by_xpath("//div[@id='content']/form/input[22]").click()


