class SessionHelper:

    def __init__(self, app):
        self.app = app


    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith('/addressbook/') and len(wd.find_elements_by_link_text("Last name")) > 0):
            wd.get("http://172.17.41.29/addressbook/")

    def login(self, username, password):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_id("LoginForm").submit()


    def logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()
        wd.find_element_by_name("user")


    def ensure_logout(self):
        if self.is_logged_in():
            self.logout()

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_link_text("Logout")) > 0

    def is_logged_in_as(self, username):
        wd = self.app.wd
        return wd.find_element_by_xpath("//div[@id = 'top']/form/b").text == "("+username+")"

    def ensure_login(self, username, password):
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)
