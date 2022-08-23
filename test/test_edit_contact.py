from model.contact import Contact


def test_edit_contact(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.contact.edit(Contact(firstname="Guido", middlename="Van", lastname="Rossum", nickname="Python", title="Genius", company="DropBox", address="Silicon Valley",
                               home_phone="4927492", cell_phone="24724213", work_phone="124714189", fax="418fj1", email_1="vasiafaf@gmail.com", email_2="fjajfafs@yandex.ru",
                               email_3="python@rambler.ru", homepage="akgdkskg.ru", day="15", month="November", year="1998", a_day="16", a_month="July", a_year="1987",
                               address2="zxvkzlvjz", secondary_phone="afkjalfjaljf", notes="ksdljgslgjksl"))
    app.open_home_page()
    app.session.logout()
