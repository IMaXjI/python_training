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
    app.login(username="admin", password="secret")
    app.open_group_page()
    app.create_group(Group(name="group", header="afafasf", footer="aSFAF"))
    app.return_to_groups_page()
    app.logout()

def test_empty_group_creation(app):
    app.open_home_page()
    app.login(username="admin", password="secret")
    app.open_group_page()
    app.create_group(Group(name=" ", header=" ", footer=" "))
    app.return_to_groups_page()
    app.logout()

