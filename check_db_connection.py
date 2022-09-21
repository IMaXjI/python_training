import pymysql.cursors
from fixture.orm import ORMFixture
from model.group import Group

db = ORMFixture(host="172.17.41.29", name="addressbook", user="admin", password="secret")
# connection = pymysql.connect(host="172.17.41.29", database="addressbook", user="admin", password="secret")

try:
    l = db.get_contacts_in_group(Group(id="5"))
    for item in l:
        print(item)
    print(len(l))
finally:
    pass # db.destroy()
