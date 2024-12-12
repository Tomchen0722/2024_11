import pymysql.cursors
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='072209101126',
                             database='world',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
with connection:
    print(connection)
    print("連線成功")
