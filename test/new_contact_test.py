# -*- coding: utf-8 -*-
from model.contact import Contact


def test_new_contact(app):
    old_contact_list = app.contact.get_contact_list()
    contact = Contact(firstname="Maxim", middlename="Olegovich", lastname="Vasilyev", nickname="MaXj", title="Genius",
                      company="TechArgos", address="Novodmitrovskaya 2b",
                      home_phone="-", cell_phone="70418041804", work_phone="aslfalf", fax="fjafafasj",
                      email_1="vasiafaf@gmail.com", email_2="fjajfafs@yandex.ru",
                      email_3="kfjajfakfa@rambler.com", homepage="asfakjfla.ru", day="15", month="November",
                      year="1998", a_day="16", a_month="July", a_year="1987",
                      address2="zxvkzlvjz", secondary_phone="afkjalfjaljf", notes="ksdljgslgjksl")
    app.contact.create(contact)
    assert len(old_contact_list) + 1 == app.contact.count()
    new_contact_list = app.contact.get_contact_list()
    old_contact_list.append(contact)
    assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)
