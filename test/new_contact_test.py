# -*- coding: utf-8 -*-
from model.contact import Contact
import random
import string
import pytest
import re


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*5
    return  prefix + "".join(filter(lambda x: x != "'",
                                    filter(lambda x: x != "  ",
                                        filter(lambda x: x is not None,
                                               [random.choice(symbols) for i in range(random.randrange(maxlen))]))))

months_list = ["January", "February", "March", "April", "May", "June",
               "July", "August", "September", "October", "November", "December"]


testdata = [Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 10),
                    lastname=random_string("lastname", 10), nickname=random_string("nickname", 10),
                    title=random_string("title", 10), company=random_string("company", 10),
                    address=random_string("address", 10),home_phone=random_string("home", 10),
                    cell_phone=random_string("mobile", 10), work_phone=random_string("work", 10),
                    fax=random_string("fax", 10), email_1=random_string("email1", 10), email_2=random_string("email2", 10),
                    email_3=random_string("email3", 10), homepage=random_string("homepage", 10),
                    day=str(random.randrange(1, 32)), month=random.choice(months_list), year=str(random.randrange(1950, 2023)), a_day=str(random.randrange(1, 32)),
                    a_month=random.choice(months_list), a_year=str(random.randrange(1950, 2023)),
                    address2=random_string("address2", 10), secondary_phone=random_string("phone2", 10),
                    notes=random_string("notes", 10))
    for i in range(5)
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_new_contact(app, contact):
    old_contact_list = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contact_list) + 1 == app.contact.count()
    new_contact_list = app.contact.get_contact_list()
    old_contact_list.append(contact)
    assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)
