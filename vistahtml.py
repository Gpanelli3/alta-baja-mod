import cgi
#from base import cursor1


import mysql.connector
conexion=mysql.connector.connect(
    host='localhost',
    user="probando-bases",
    passwd="password",
    database="base-datos-2")


cursor1=conexion.cursor()
cursor1.execute("select * from alumnos")


#headers
print("Content-Type: text/html")
print()

("<html>")

print("<body>")
print("<h1>Tabla de Ejemplo</h1>")

#Inicio de la tabla 
print("<table border=2>")
#Encabezado de la tabla 
print("<tr>")
print("<th>Id alumno</th>")
print("<th>Nombre</th>")
print("<th>Apellido</th>")
print("</tr>")
        
#Filas de datos 
for base in cursor1:


    print("<tr>")

    print("<td>")
    print(base[0])
    print("</td>")
    
    print("<td>")
    print(base[1])
    print("</td>")
    

    print("<td>")
    print(base[2])
    print("</td>")

    print("</tr>")


    
print("</table>")
#Fin de la tabla



print("""<html>

      <body>
            <br>
            <form method="post" action="alta.py">
        	    <p>Ingreso de alumnos</p>
                id: <input type="number" name="id"/> <br/>
                nombre: <input type="text" name="nombre"  /> <br/>
                apellido: <input type="text" name="apellido" /> <br/>
                <button>INGRESAR ALUMNO</button>
            </form>
            
            <form method="post" action="baja.py">
        	    <p>Dar de baja alumnos</p>
                id:<input type="number" name="id" /> <br/>
                <button>DAR DE BAJA ALUMNO</button>
            </form>
      </body>
                
      
    </html>""")
("</body>")
("</html>")
 



conexion.close()
