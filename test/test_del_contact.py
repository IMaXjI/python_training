from model.contact import Contact

def test_del_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Test"))
    old_contact_list = app.contact.get_contact_list()
    app.contact.delete()
    assert len(old_contact_list) - 1 == app.contact.count()
    new_contact_list = app.contact.get_contact_list()
    old_contact_list[0:1] = []
    assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)

