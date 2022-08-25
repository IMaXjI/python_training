# -*- coding: utf-8 -*-
from model.group import Group

def test_group_creation(app):
    app.group.create(Group(name="group", header="afafasf", footer="aSFAF"))


def test_empty_group_creation(app):
    app.group.create(Group(name=" ", header=" ", footer=" "))

