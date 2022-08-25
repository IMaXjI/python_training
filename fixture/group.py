class GroupHelper:
    def __init__(self, app):
        self.app = app

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def create(self, group):
        wd = self.app.wd
        # Init group creation
        wd.find_element_by_name("new").click()
        self.fill_group_form(group)
        # Submit creation
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def fill_group_form(self, group):
        wd = self.app.wd
        self.filling_condition_check("group_name", group.name)
        self.filling_condition_check("group_header", group.header)
        self.filling_condition_check("group_footer", group.footer)


    def filling_condition_check(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def open_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()


    def delete(self):
        wd = self.app.wd
        self.open_group_page()
        self.select_first_group()
        # Submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def edit(self, new_group_data):
        wd = self.app.wd
        self.open_group_page()
        self.select_first_group()
        # Open modification form
        wd.find_element_by_name("edit").click()
        # Edit group fields
        self.fill_group_form(new_group_data)
        # Submit changes
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()


