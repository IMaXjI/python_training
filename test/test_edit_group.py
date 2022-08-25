from model.group import Group

def test_edit_group_name(app):
    app.group.edit(Group(name="Changed name"))


def test_edit_group_header(app):
    app.group.edit(Group(header="Changed header"))


def test_edit_group_footer(app):
    app.group.edit(Group(footer="Changed footer"))
