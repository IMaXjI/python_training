from model.group import Group

def test_edit_group(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.group.open_group_page()
    app.group.edit(Group(name="Changed name", header="Changed header", footer="Changed footer"))
    app.session.logout()
