'''
Created on 2012-6-14

@author: jiang
'''
import sqlite3
if __name__ == '__main__':
    conn = sqlite3.connect("d://test.db")
    conn.execute("create table if not exists address(\
                    id integer primary key autoincrement,\
                    name varchar(128),\
                    address varchar(128) )"
    )
    conn.execute("insert into address(name, address) values('tom', 'beijing')")
    #  conn.execute("insert into address(name, address) values('lucy', 'shanghai')")
    
    conn.commit()

    
    cur = sqlite3.Cursor(conn)
    
    help(type(cur))
    cur.execute("select *from address")
    print cur.arraysize
    res = cur.fetchall()
    for line in res:
        print line
    cur.close()
    print len(res)
    
    