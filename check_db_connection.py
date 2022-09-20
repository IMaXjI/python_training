import pymysql.cursors
from fixture.orm import ORMFixture

db = ORMFixture(host="172.17.41.29", name="addressbook", user="admin", password="secret")
# connection = pymysql.connect(host="172.17.41.29", database="addressbook", user="admin", password="secret")

try:
    l = db.get_contact_list()
    for item in l:
        print(item)
    print(len(l))
finally:
    pass # db.destroy()
