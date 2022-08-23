
def test_del_group(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.group.open_group_page()
    app.group.delete()
    app.session.logout()