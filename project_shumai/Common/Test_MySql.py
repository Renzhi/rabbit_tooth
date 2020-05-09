import pymysql

'''
封装数据库
'''


'''获取数据库连接方法'''
def get_content_db():
    connect = pymysql.connect(host='', port=3306,user='', password='',
                           database='')
    return connect

'''封装数据库查询操作'''
def operation_db(sql):
    conn = get_content_db()  #获取连接
    cur = conn.cursor()      #建立游标
    cur.execute(sql)         #执行数据库操作
    result =cur.fetchall()   #获取查询结果
    cur.close()              #关闭游标
    conn.close()             #关闭数据库连接
    return result

'''封装更改数据库操作'''
def updata_db(sql):
    conn = get_content_db()  # 获取连接
    cur = conn.cursor()      # 建立游标
    try:
        cur.execute(sql)    # 执行sql
        conn.commit()       # 提交更改
    except Exception as e:
        conn.rollback()     # 回滚
    finally:
        cur.close()         # 关闭游标
        conn.close()        # 关闭连接
