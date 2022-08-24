from model.contact import Contact

def test_edit_contact_name(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.contact.edit(Contact(firstname="New name"))
    app.open_home_page()
    app.session.logout()


def test_edit_contact_nickname(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.contact.edit(Contact(nickname="New nickname"))
    app.open_home_page()
    app.session.logout()


def test_edit_contact_cell_phone(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.contact.edit(Contact(cell_phone='New phone'))
    app.open_home_page()
    app.session.logout()
