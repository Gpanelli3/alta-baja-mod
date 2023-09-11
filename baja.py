import cgi 

import mysql.connector

conexion=mysql.connector.connect(host='localhost',
                                 user='probando-bases',
                                 passwd='password', 
                                 database='base-datos-2',)

cursor1=conexion.cursor()

form = cgi.FieldStorage() 
# Get data from fields

id=form['id'].value

sql=(f"DELETE FROM alumnos where idalumnos = {id}")
cursor1.execute(sql)
conexion.commit()
conexion.close()





