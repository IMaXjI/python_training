# -*- coding: utf-8 -*-
from contacts_methods import help_methods
from contact import Contact
import pytest

@pytest.fixture
def app(request):
    fixture = help_methods()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_new_contact(app):
    app.open_test_page()
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="Maxim", middlename="Olegovich", lastname="Vasilyev", nickname="MaXj", title="Genius", company="TechArgos", address="Novodmitrovskaya 2b",
                        home_phone="-", cell_phone="70418041804", work_phone="aslfalf", fax="fjafafasj", email_1="vasiafaf@gmail.com", email_2="fjajfafs@yandex.ru",
                        email_3="kfjajfakfa@rambler.com", homepage="asfakjfla.ru", day="15", month="November", year="1998", a_day="16", a_month="July", a_year="1987",
                        address2="zxvkzlvjz", secondary_phone="afkjalfjaljf", notes="ksdljgslgjksl"))
    app.return_to_home_page()
    app.logout()


