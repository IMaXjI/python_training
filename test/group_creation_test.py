# -*- coding: utf-8 -*-
from fixture.application import Application
from model.group import Group
import pytest

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_group_creation(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.group.open_group_page()
    app.group.create(Group(name="group", header="afafasf", footer="aSFAF"))
    app.group.return_to_groups_page()
    app.session.logout()

def test_empty_group_creation(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.group.open_group_page()
    app.group.create(Group(name=" ", header=" ", footer=" "))
    app.group.return_to_groups_page()
    app.session.logout()

