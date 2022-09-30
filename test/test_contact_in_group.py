from model.contact import Contact
from model.group import Group
import random


def test_contact_in_group(app, db, orm, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="TEST CONTACT"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="TEST GROUP"))
    contact_list = db.get_contact_list()
    group_list = db.get_group_list()
    random_contact = random.choice(contact_list)
    random_group = random.choice(group_list)
    contacts_in_group_db_old = orm.get_contacts_in_group(Group(id=random_group.id))
    app.contact.add_contact_to_group(random_contact.id, random_group.id)
    contacts_in_group_db_new = orm.get_contacts_in_group(Group(id=random_group.id))
    assert len(contacts_in_group_db_old) + 1 == len(contacts_in_group_db_new)
    assert random_contact in contacts_in_group_db_new
    if check_ui:
        contacts_in_groups_ui = app.contact.get_contact_list_from_group_page(random_group.id)
        assert sorted(contacts_in_group_db_new, key=Contact.id_or_max) == sorted(contacts_in_groups_ui, key=Contact.id_or_max)


def test_contact_not_in_group(app, db, orm):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="TEST CONTACT"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="TEST GROUP"))
    group_list = db.get_group_list()
    random_group = random.choice(group_list)
    contacts_in_group_db_old = orm.get_contacts_in_group(Group(id=random_group.id))
    random_contact = random.choice(contacts_in_group_db_old)
    app.contact.remove_contact_from_group(random_contact.id, random_group.id)
    contacts_in_group_db_new = orm.get_contacts_in_group(Group(id=random_group.id))
    contacts_not_in_group = orm.get_contacts_not_in_group(Group(id=random_group.id))
    assert len(contacts_in_group_db_old) - 1 == len(contacts_in_group_db_new)
    assert random_contact in contacts_not_in_group



