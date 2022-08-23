

def test_del_contact(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.contact.delete()
    app.session.logout()