
from pytest_bdd import given, when, then
from model.contact import Contact

@given('a contact list')
def contact_list(db):
    return db.get_contact_list()

@given('a contact with <id>, <firstname>, <lastname>')
def new_contact(id, firstname, lastname):
    return Contact(firstname=firstname, id=id, lastname=lastname)

@when('I add new contact to the list')
def add_new_contact(app, new_contact):
    app.contact.create(new_contact)


@then('the new contact list is equal to the old list with new contact')
def verify_contact_added(db, contact_list, new_contact):
    contact_list_old = contact_list
    contact_list_new = db.get_contact_list()
    contact_list_old.append(new_contact)
    assert sorted(contact_list_old, key=Contact.id_or_max) == sorted(contact_list_new, key=Contact.id_or_max)

