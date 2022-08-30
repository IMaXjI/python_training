# -*- coding: utf-8 -*-
from model.group import Group


def test_group_creation(app):
    old_group_list = app.group.get_group_list()
    group = Group(name="group", header="afafasf", footer="aSFAF")
    app.group.create(group)
    assert len(old_group_list) + 1 == app.group.count()
    new_group_list = app.group.get_group_list()
    old_group_list.append(group)
    assert sorted(old_group_list, key = Group.id_or_max) == sorted(new_group_list, key = Group.id_or_max)

# def test_empty_group_creation(app):
#     old_group_list = app.group.get_group_list()
#     group = Group(name="group", header="afafasf", footer="aSFAF")
#     app.group.create(group)
#     new_group_list = app.group.get_group_list()
#     assert len(old_group_list) + 1 == len(app.group.count())
#     old_group_list.append(group)
#     assert sorted(old_group_list, key=Group.id_or_max) == sorted(new_group_list, key=Group.id_or_max)
