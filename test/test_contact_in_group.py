import random

def test_contact_in_group(app, db):
    contact_list = db.get_contact_list()
    group_list = db.get_group_list()
    random_contact = random.choice(contact_list)
    random_group = random.choice(group_list)
    app.contact.add_contact_to_group(random_contact, random_group)
    assert
