from model.group import Group
from random import randrange


def test_edit_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name = "test"))
    old_group_list = app.group.get_group_list()
    index = randrange(len(old_group_list))
    group = Group(name="Changes group name")
    group.id = old_group_list[index].id
    app.group.edit_by_index(index, group)
    assert len(old_group_list) == app.group.count()
    new_group_list = app.group.get_group_list()
    old_group_list[index] = group
    assert sorted(old_group_list, key=Group.id_or_max) == sorted(new_group_list, key=Group.id_or_max)


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
