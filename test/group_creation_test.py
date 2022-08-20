# -*- coding: utf-8 -*-
from model.group import Group

def test_group_creation(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.group.open_group_page()
    app.group.create(Group(name="group", header="afafasf", footer="aSFAF"))
    app.session.logout()


def test_empty_group_creation(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.group.open_group_page()
    app.group.create(Group(name=" ", header=" ", footer=" "))
    app.session.logout()

