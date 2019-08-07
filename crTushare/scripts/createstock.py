import pymysql
con = pymysql.connect('127.0.0.1','','','share')
with con:
    cur = con.cursor()
    cur.execute("select * from polls_stock_basic limit 10")
    rows = cur.fetchall()
    for row in rows:
        print(row)