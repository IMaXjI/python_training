from model.contact import Contact

def test_edit_contact_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Test"))
    old_contact_list = app.contact.get_contact_list()
    contact = Contact(firstname="New firstname", lastname="New lastname")
    contact.id = old_contact_list[0].id
    app.contact.edit(contact)
    new_contact_list = app.contact.get_contact_list()
    assert len(old_contact_list) == len(new_contact_list)
    old_contact_list[0] = contact
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
