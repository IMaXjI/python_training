# -*- coding: utf-8 -*-
from model.group import Group
import allure


def test_group_creation(app, db, json_groups):
    group = json_groups
    with allure.step('Given a contact list'):
        old_group_list = db.get_group_list()
    with allure.step('When I add a new contact %s to the list' %group):
        app.group.create(group)
    with allure.step('Then the new contact list is equal to the old list with new contact'):
        new_group_list = db.get_group_list()
        old_group_list.append(group)
        assert sorted(old_group_list, key=Group.id_or_max) == sorted(new_group_list, key=Group.id_or_max)


