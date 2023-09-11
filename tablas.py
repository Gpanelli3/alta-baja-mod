import mysql.connector

conexion=mysql.connector.connect(host='localhost',user="probando-bases",passwd="password",database="base-datos-2")
cursor1=conexion.cursor()

cursor1.execute("show tables")


for base in cursor1:
    print(base)
conexion.close()