
def test_del_group(app):
    app.group.delete()
    app.session.open_home_page()