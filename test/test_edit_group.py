from model.group import Group

def test_edit_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name = "test"))
    app.group.edit(Group(name="Changed name"))


def test_edit_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name = "test"))
    app.group.edit(Group(header="Changed header"))


def test_edit_group_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(name = "test"))
    app.group.edit(Group(footer="Changed footer"))
