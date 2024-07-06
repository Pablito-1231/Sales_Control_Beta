
import MENU_CON_DATABASE as MCDB

def InsertarData(Insertar):
    print()
    Insertar.execute ("INSERT INTO F060116 values (?,?,?)", MCDB.List_Reg)

def ConsultarData(Consultar):

    Consultar.execute("SELECT * FROM tablauno")
    return Consultar.fetchall()