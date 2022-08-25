from model.contact import Contact

def test_edit_contact_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Test"))
        app.session.open_home_page()
    app.contact.edit(Contact(firstname="New firstname"))
    app.session.open_home_page()


def test_edit_contact_nickname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Test"))
        app.session.open_home_page()
    app.contact.edit(Contact(nickname="New nickname"))
    app.session.open_home_page()


def test_edit_contact_cell_phone(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Test"))
        app.session.open_home_page()
    app.contact.edit(Contact(cell_phone='New phone'))
    app.session.open_home_page()
