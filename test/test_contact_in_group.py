from model.contact import Contact
from model.group import Group
import random

def test_contact_in_group(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="TEST CONTACT"))
    elif len(db.get_group_list()) == 0:
        app.group.create(Group(name = "TEST GROUP"))
    contact_list = db.get_contact_list()
    group_list = db.get_group_list()
    random_contact = random.choice(contact_list)
    random_group = random.choice(group_list)
    app.contact.add_contact_to_group(random_contact.id, random_group.id)
    '''
    Assertion is going to be added here
    '''

