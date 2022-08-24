from model.group import Group

def test_edit_group_name(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.group.open_group_page()
    app.group.edit(Group(name="Changed name"))
    app.session.logout()


def test_edit_group_header(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.group.open_group_page()
    app.group.edit(Group(header="Changed header"))
    app.session.logout()


def test_edit_group_footer(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.group.open_group_page()
    app.group.edit(Group(footer="Changed footer"))
    app.session.logout()