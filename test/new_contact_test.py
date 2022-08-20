# -*- coding: utf-8 -*-
from model.contact import Contact

def test_new_contact(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="Maxim", middlename="Olegovich", lastname="Vasilyev", nickname="MaXj", title="Genius", company="TechArgos", address="Novodmitrovskaya 2b",
                               home_phone="-", cell_phone="70418041804", work_phone="aslfalf", fax="fjafafasj", email_1="vasiafaf@gmail.com", email_2="fjajfafs@yandex.ru",
                               email_3="kfjajfakfa@rambler.com", homepage="asfakjfla.ru", day="15", month="November", year="1998", a_day="16", a_month="July", a_year="1987",
                               address2="zxvkzlvjz", secondary_phone="afkjalfjaljf", notes="ksdljgslgjksl"))
    app.return_to_home_page()
    app.session.logout()



