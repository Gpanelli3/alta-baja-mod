import cgi

import mysql.connector
conexion=mysql.connector.connect(host='localhost',
                                 user="probando-bases",
                                 passwd="password",
                                 database="base-datos-2")
cursor1=conexion.cursor()


form = cgi.FieldStorage() 
# Get data from fields

id=form['id'].value
first_name = form['nombre'].value
last_name  = form['apellido'].value


sql="INSERT INTO alumnos(idalumnos,nombre,apellido) VALUES (%s,%s,%s)"
if id == 'idalumnos':
    ("<html>")
    print('error, ya existe ese alumno')
    ("</html>")

else:
    valores=(id,first_name,last_name)
    cursor1.execute(sql,valores)


conexion.commit()

conexion.close()
