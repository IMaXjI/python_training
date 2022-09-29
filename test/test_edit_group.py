from model.group import Group
import random


def test_edit_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name = "test"))
    old_group_list = db.get_group_list()
    group = random.choice(old_group_list)
    new_data = Group(header="Changes group header")
    app.group.edit_by_id(group.id, new_data)
    new_group_list = db.get_group_list()
    assert len(old_group_list) == app.group.count()
    if check_ui:
        assert sorted(new_group_list, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


# def test_edit_group_header(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name = "test"))
#     old_group_list = app.group.get_group_list()
#     app.group.edit(Group(header="Changed header"))
#     new_group_list = app.group.get_group_list()
#     assert len(old_group_list) == len(new_group_list)


# def test_edit_group_footer(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name = "test"))
#     old_group_list = app.group.get_group_list()
#     app.group.edit(Group(footer="Changed footer"))
#     new_group_list = app.group.get_group_list()
#     assert len(old_group_list) == len(new_group_list)
