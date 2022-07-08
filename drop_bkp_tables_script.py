# drop tables given any schema which has back up tables named such as backup or date(ex:20220301) or bkp
import mysql.connector
import sys

schema_name = sys.argv[1]
print("args:", schema_name)

mydb = mysql.connector.connect(

host = "xxxx"
user = "admin"
password = "admin"
database = "salesdb"

mycursor = mydb.cursor()

fetch_sql = "select Table_Name from information_schema.tables where Table_schema = '{}' and \
table_name in (select TABLE_NAME from information_schema.tables \
where TABLE_NAME like '%bkup%' or TABLE_NAME like '%20%' or TABLE_NAME like '%bkp%' or TABLE_NAME like '%bck%');".format(schema_name)
print(fetch_sql)

mycursor.execute(fetch_sql)
myresult = mycursor.fetchall()

tables = []
for i in range(len(myresult)):
    tables.append(myresult[i][0])
    
print(tables)

mycursor1 = mydb.cursor()
sql = "drop table {}.".format(schema_name)

for x in tables:
    print(sql + x)
    mycursor1.execute(sql + x)
    
mycursor1.close()
mycursor.close()
mydb.close()