class SessionHelper:

    def __init__(self, app):
        self.app = app


    def open_home_page(self):
        wd = self.app.wd
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
