from model.contact import Contact

def test_del_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Test"))
        app.session.open_home_page()
    app.contact.delete()
