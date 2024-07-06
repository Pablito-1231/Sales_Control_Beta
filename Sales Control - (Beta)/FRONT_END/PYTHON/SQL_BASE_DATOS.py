
import sqlite3 as SQL

connextion = SQL.connect("DATABASE.db")
Cuursor = connextion.cursor()

Cuursor.execute("""create table if not exists tablauno (DESCRIPCION text, PRECIO real, CANTIDAD integer)""")

#***********************************************************************************************

varios_productos = ["LIBRO",5000,10]

print("\n", varios_productos[2], "\n")

def InsertarData(C):
    C.execute ("INSERT INTO tablauno values (?,?,?)", varios_productos)

def ConsultarData(C):
    C.execute("SELECT * FROM tablauno")
    return C.fetchall()

#***********************************************************************************************

InsertarData(Cuursor)
productos = ConsultarData(Cuursor)

connextion.commit()
Cuursor.close()
connextion.close()

print(productos)
