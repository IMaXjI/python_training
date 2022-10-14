
from pytest_bdd import given, when, then
from model.group import Group
import random

@given('a group list', target_fixture='group_list')
def group_list(db):
    return db.get_group_list()

@given('a non-empty group list', target_fixture='non_empty_group_list')
def non_empty_group_list(db, app):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name='New group'))
    return db.get_group_list()

@given('a random group from the list', target_fixture='random_group')
def random_group(non_empty_group_list):
    return random.choice(non_empty_group_list)

@given('a group with <name>, <header> and <footer>', target_fixture='new_group')
def new_group(name, header, footer):
    return Group(name=name, header=header, footer=footer)

@when('I delete the group from the list', target_fixture='del_group')
def del_group(app, random_group):
    app.group.delete_by_id(random_group.id)


@when('I add new group to the list', target_fixture='add_new_group')
def add_new_group(app, new_group):
    app.group.create(new_group)


@then('the new group list is equal to the old list with new group', target_fixture='verify_group_added')
def verify_group_added(db, group_list, new_group):
    group_list_old = group_list
    group_list_new = db.get_group_list()
    group_list_old.append(new_group)
    assert sorted(group_list_old, key=Group.id_or_max) == sorted(group_list_new, key=Group.id_or_max)

@then('the new group list is equal to the old list without deleted group', target_fixture='verify_group_deleted')
def verify_group_deleted(db, non_empty_group_list, random_group, app, check_ui):
    group_list_old = non_empty_group_list
    group_list_new = db.get_group_list()
    group_list_old.remove(new_group)
    assert len(group_list_old) - 1 == app.group.count()
    group_list_old.remove(random_group)
    assert group_list_old == group_list_new
    if check_ui:
        assert sorted(group_list_new, key=Group.id_or_max) == sorted(app.group.get_group_list(),
                                                                         key=Group.id_or_max)

