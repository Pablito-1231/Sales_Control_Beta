
#CONEXIÓN A BASE DE DATOS DE DAIRY

from shutil import which
import sqlite3 as SQL

database = "Dairy_DataBase.db"

class Dairy_db:
    def exe_consulta (self, consulta, parametros = ()):
        with SQL.connect(database) as conne:
            
            self.Cuursor = conne.cursor()
            self.Cuursor.execute("""create table if not exists F0101 (ID Integer primary key autoincrement, NOMBRE text, DIRECCION text, CORREO text, CELULAR integer, TELEFONO integer)""")
            result = self.Cuursor.execute(consulta, parametros)
            conne.commit()
            return (result)








