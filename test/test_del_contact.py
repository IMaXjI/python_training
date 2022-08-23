

def test_del_contact(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.contact.del_contact()
    app.session.logout()