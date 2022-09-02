from selenium.webdriver.support.ui import Select
from model.contact import Contact



class ContactHelper:
    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith('/addressbook/') and len(wd.find_elements_by_link_text("Last name")) > 0):
            wd.get("http://172.17.41.29/addressbook/")

    def create(self, contact):
        wd = self.app.wd
        self.open_home_page()
        # Init contact creation
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        # Submit addition
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.contact_cache = None


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
        self.filling_condition_check("bday", contact.day)
        self.filling_condition_check("bmonth", contact.month)
        self.filling_condition_check("byear", contact.year)
        self.filling_condition_check("aday", contact.a_day)
        self.filling_condition_check("amonth", contact.a_month)
        self.filling_condition_check("ayear", contact.a_year)
        self.filling_condition_check("address2", contact.address2)
        self.filling_condition_check("phone2", contact.secondary_phone)
        self.filling_condition_check("notes", contact.notes)

    def filling_condition_check(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            if field_name == "bday" or \
                    field_name == "bmonth" or \
                    field_name == "aday" or \
                    field_name == "amonth":
                wd.find_element_by_name(field_name).click()
                Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)
                # wd.find_element_by_name(field_name).click()
            else:
                wd.find_element_by_name(field_name).click()
                wd.find_element_by_name(field_name).clear()
                wd.find_element_by_name(field_name).send_keys(text)
        else:
            pass


    def delete(self):
        self.delete_by_index(0)

    def delete_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        self.select_contact_by_index(index)
        # Submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.contact_cache = None

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()


    def edit(self):
        self.edit_by_index(0)

    def edit_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.open_home_page()
        self.find_edit_button_by_index(index)
        self.fill_contact_form(new_contact_data)
        # Submit update
        wd.find_element_by_xpath("//div[@id='content']/form/input[22]").click()
        self.contact_cache = None

    def find_edit_button_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))


    contact_cache = None
    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_css_selector("tr[name = 'entry']"):
                cells = element.find_elements_by_tag_name("td")
                lastname_text = cells[1].text
                firstname_text = cells[2].text
                id = element.find_element_by_name("selected[]").get_attribute("id")
                self.contact_cache.append(Contact(lastname=lastname_text, firstname=firstname_text, id=id))
        return list(self.contact_cache)

