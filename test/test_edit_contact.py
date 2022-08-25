from model.contact import Contact

def test_edit_contact_name(app):
    app.contact.edit(Contact(firstname="New firstname"))
    app.session.open_home_page()


def test_edit_contact_nickname(app):
    app.contact.edit(Contact(nickname="New nickname"))
    app.session.open_home_page()


def test_edit_contact_cell_phone(app):
    app.contact.edit(Contact(cell_phone='New phone'))
    app.session.open_home_page()
