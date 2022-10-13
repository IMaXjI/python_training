
from pytest_bdd import given, when, then
from model.contact import Contact
import random

@given('a contact list')
def contact_list(db):
    return db.get_contact_list()

@given('a non-empty contact list')
def non_empty_contact_list(db, app):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(name='New contact'))
    return db.get_contact_list()

@given('a random contact from the list')
def random_contact(non_empty_contact_list):
    return random.choice(non_empty_contact_list)

@given('a contact with <id>, <firstname> and <lastname>')
def new_contact(id, firstname, lastname):
    return Contact(firstname=firstname, id=id, lastname=lastname)

@when('I delete the group from the list')
def del_contact(app, random_contact):
    app.contact.delete_by_id(random_contact.id)


@when('I add new contact to the list')
def add_new_contact(app, new_contact):
    app.contact.create(new_contact)


@then('the new contact list is equal to the old list with new contact')
def verify_contact_added(db, contact_list, new_contact):
    contact_list_old = contact_list
    contact_list_new = db.get_contact_list()
    contact_list_old.append(new_contact)
    assert sorted(contact_list_old, key=Contact.id_or_max) == sorted(contact_list_new, key=Contact.id_or_max)

@then('the new contact list is equal to the old list without deleted contact')
def verify_contact_deleted(db, non_empty_contact_list, random_contact, app, check_ui):
    contact_list_old = non_empty_contact_list
    contact_list_new = db.get_contact_list()
    contact_list_old.remove(new_contact)
    assert len(contact_list_old) - 1 == app.contact.count()
    contact_list_old.remove(random_contact)
    assert contact_list_old == contact_list_new
    if check_ui:
        assert sorted(contact_list_old, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                         key=Contact.id_or_max)
    assert sorted(contact_list_old, key=Contact.id_or_max) == sorted(contact_list_new, key=Contact.id_or_max)


