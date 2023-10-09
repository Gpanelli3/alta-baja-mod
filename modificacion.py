import cgi 
import mysql.connector


conexion=mysql.connector.connect(host='localhost',
                                 user="probando-bases",
                                 passwd="password",
                                 database="base-datos-2")
cursor1=conexion.cursor()
form = cgi.FieldStorage() 

id=form['id'].value
name = form['nombre'].value
last= form['apellido'].value

sql=f'update alumnos set nombre={name}, apellido={last} where idalumnos={id}'

cursor1.execute(sql)
conexion.commit()
conexion.close()