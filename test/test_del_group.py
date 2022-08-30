from model.group import Group


def test_del_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name = "test"))
    old_group_list = app.group.get_group_list()
    app.group.delete()
    assert len(old_group_list) - 1 == app.group.count()
    new_group_list = app.group.get_group_list()
    old_group_list[0:1] = []
    assert old_group_list == new_group_list
