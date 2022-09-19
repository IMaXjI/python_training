import pymysql.cursors

connection = pymysql.connect(host="172.17.41.29", database="addressbook", user="admin", password="secret")

try:
    cursor = connection.cursor()
    cursor.execute("select * from group_list")
    for row in cursor.fetchall():
        print(row)
finally:
    connection.close()