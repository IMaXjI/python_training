# -*- coding: utf-8 -*-
from model.group import Group

def test_group_creation(app):
    old_group_list = app.group.get_group_list()
    app.group.create(Group(name="group", header="afafasf", footer="aSFAF"))
    new_group_list = app.group.get_group_list()
    assert len(old_group_list) + 1 == len(new_group_list)

def test_empty_group_creation(app):
    old_group_list = app.group.get_group_list()
    app.group.create(Group(name=" ", header=" ", footer=" "))
    new_group_list = app.group.get_group_list()
    assert len(old_group_list) + 1 == len(new_group_list)

