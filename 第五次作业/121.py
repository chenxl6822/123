import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Cxl060822!",
)

cursor = connection.cursor()

cursor.execute("create database IF NOT EXISTS NEXUS")
cursor.execute("USE NEXUS")
cursor.execute("create table circum (subject varchar(20),state varchar(10),QtoA int,phase varchar(20))")
#学科--状态--待解决的问题数--阶段==表名为’情况‘
#ssQp
cursor.execute("ALTER TABLE circum ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
#添加主键
#print("走到这里算运行成功吗,运行成功指的是神马?")
sql = "insert into circum(subject,state,QtoA,phase) values (%s,%s,%s,%s)"
val = ("高数", "地狱", 114, "定积分")
cursor.execute(sql, val)

connection.commit()
#添加一条数据
val = [
    ("线代", "听不懂", 65, "矩阵"),
    ('OJ', '刷不完', 30, "贪心算法"),
    ('English', '四级', 20, '难受'),
]
cursor.executemany(sql, val)

connection.commit()
#添加多条数据
sql = 'update circum set subject="高等数学" WHERE subject="高数"'

cursor.execute(sql)

connection.commit()
#更新数据
sql = "delete from circum where subject ='OJ'"
cursor.execute(sql)
connection.commit()
#删除数据

#-------------------没有分文件写又要少分lia
cursor.execute("select * from circum")
result = cursor.fetchall()
for row in result:
    print(row)
cursor.close()
connection.close()