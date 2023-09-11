#mantenimiento de tablas mysql 
#ABM de tablas mysql
#interfaz web (gui cgi)
#controlador y modelo python 
#MOSTRAR EN EL HTML LOS DATOS DE LA BASE DE DATOS(utilizamos table)

import mysql.connector

conexion=mysql.connector.connect(host='localhost',user="probando-bases",passwd="password")
cursor1=conexion.cursor()
cursor1.execute("show databases")

for base in cursor1:
    print(base)
conexion.close()







