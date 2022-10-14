
from pytest_bdd import given, when, then
from model.contact import Contact
import random

@given('a contact list', target_fixture='contact_list')
def contact_list(db):
    return db.get_contact_list()

@given('a non-empty contact list', target_fixture='non_empty_contact_list')
def non_empty_contact_list(db, app):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname='New contact'))
    return db.get_contact_list()

@given('a random contact from the list', target_fixture='random_contact')
def random_contact(non_empty_contact_list):
    return random.choice(non_empty_contact_list)

@given('a contact with <id>, <firstname> and <lastname>', target_fixture='new_contact')
def new_contact(firstname, lastname):
    return Contact(firstname=firstname, lastname=lastname)

@when('I delete the group from the list', target_fixture='del_contact')
def del_contact(app, random_contact):
    app.contact.delete_by_id(random_contact.id)


@when('I add new contact to the list', target_fixture='add_new_contact')
def add_new_contact(app, new_contact):
    app.contact.create(new_contact)


@then('the new contact list is equal to the old list with new contact', target_fixture='verify_contact_added')
def verify_contact_added(db, contact_list, new_contact):
    contact_list_old = contact_list
    contact_list_new = db.get_contact_list()
    contact_list_old.append(new_contact)
    assert sorted(contact_list_old, key=Contact.id_or_max) == sorted(contact_list_new, key=Contact.id_or_max)

@then('the new contact list is equal to the old list without deleted contact', target_fixture='verify_contact_deleted')
def verify_contact_deleted(db, non_empty_contact_list, random_contact, app, check_ui):
    contact_list_old = non_empty_contact_list
    contact_list_new = db.get_contact_list()
    contact_list_old.remove(new_contact)
    assert len(contact_list_old) - 1 == app.contact.count()
    contact_list_old.remove(random_contact)
    assert contact_list_old == contact_list_new
    if check_ui:
        assert sorted(contact_list_new, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                         key=Contact.id_or_max)


