# coding=utf-8
import pymysql
from pymysql.cursors import DictCursor
 
def insert_data():    #插入数据
    course_id = int(input('编号：'))
    course_name = input('名字:')
    #1、创建数据库连接对象
    con = pymysql.connect(host= 'localhost',port=3306
                          ,database='test',charset= 'utf8'
                          ,user='root',password='root')
    try:
        #通过连接对象获取游标
        with con.cursor() as cursor:
            #3、通过游标执行sql并获得执行结果
            result = cursor.execute(
                'insert into course values(%s,%s) ',(course_id,course_name))
            if result ==1:
                print('添加成功!')
            #操作成功提交事务
            con.commit()
    finally:
        #5、关闭连接释放资源
        con.close()
if __name__ == '__main__':
    insert_data()
