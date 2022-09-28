from model.contact import Contact
import random


def test_edit_contact_name(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Test"))
    old_contact_list = db.get_contact_list()
    contact = random.choice(old_contact_list)
    new_data = Contact(firstname="TEST WORKS", lastname="TEST WORKS")
    app.contact.edit_by_id(contact.id, new_data)
    new_contact_list = db.get_contact_list()
    assert len(old_contact_list) == app.contact.count()
    if check_ui:
        assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)

#
# def test_edit_contact_nickname(app):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(firstname="Test"))
#         app.session.open_home_page()
#     app.contact.edit(Contact(nickname="New nickname"))
#     # app.session.open_home_page()
#
#
# def test_edit_contact_cell_phone(app):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(firstname="Test"))
#         app.session.open_home_page()
#     app.contact.edit(Contact(cell_phone='New phone'))
#     app.session.open_home_page()
