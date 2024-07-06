
# AGENDA TELEFONICA CON DATOS PERSONALES 

# =====================================================================================================
#IMPORTADORES

import sys
#import pandas as pd
import Conexiónn as conex
from FrontEnd_Agenda import *

#from PyQt5.QtSql import *
#from PyQt5.QtCore import *
#from PyQt5.QtWidgets import *

#QWidget, QApplication, QVBoxLayout, QPushButton, \
#QTableWidgetItem, QMessageBox, QLineEdit, QLabel, QGridLayout, QListView
# =====================================================================================================

db = conex.Dairy_db()

# CLASE MAESTRA HEREDERA DE TODOS LOS METODOS.
class Agenda_DB (QtWidgets.QMainWindow, Ui_Diary):
    def __init__ (self):
        super().__init__()

        self.mensajes = QMessageBox()
        self.ui = Ui_Diary()
        self.ui.setupUi(self)

        # EXTRAS
        self.ui.Tabla_Consulta.setHorizontalHeaderLabels(['ID','Nombre','Dirección','Correo','Celular','Telefono'])
        self.ui.Tabla_Actualizar.setHorizontalHeaderLabels(['ID','Nombre','Dirección','Correo','Celular','Telefono'])
        self.ui.Campo_Nombre.setPlaceholderText("Escriba el nombre completo")
        self.ui.Campo_Direccion.setPlaceholderText("Av - # - #")
        self.ui.Campo_Correo.setPlaceholderText("example@example.com")
        self.ui.Campo_Celular.setPlaceholderText("Sin espacios")
        self.ui.Campo_Telefono.setPlaceholderText("Sin espacios")

        self.ui.ID_A_Buscar.setPlaceholderText("¿Que ID desea buscar?")
        self.ui.Campo_A_Cambiar.setPlaceholderText("Seleccione el campo y escriba")

        # ORDENES DE CADA BOTON
        self.ui.Boton_Ingresar.clicked.connect(self.Ingresar)
        self.ui.Boton_Ingresar.clicked.connect(self.Limpiar)
        self.ui.Boton_Cargar.clicked.connect(self.Cargar)
        self.ui.Boton_Eliminar.clicked.connect(self.Eliminar)
        self.ui.Boton_Buscar.clicked.connect(self.B)
        self.ui.Boton_BuscaID.clicked.connect(self.BuscarID)
        self.ui.Boton_Actualizar.clicked.connect(self.Actualizar)
        #self.ui.Boton_Exportar.clicked.connect(self.Exportar)

    # METODO PARA INGRESAR REGISTROS EN LA TABLA.
    def Ingresar(self):
        
        id = None
        nombre = self.ui.Campo_Nombre.text()
        direccion = self.ui.Campo_Direccion.text()
        correo = self.ui.Campo_Correo.text()
        celular = int(self.ui.Campo_Celular.text())
        telefono = int(self.ui.Campo_Telefono.text())

        if (len(nombre) > 0 and len(direccion) > 0 and len(correo) > 0):
            sql = ("INSERT INTO F0101(ID,NOMBRE,DIRECCION,CORREO,CELULAR,TELEFONO) VALUES(?,?,?,?,?,?)".format(id, nombre, direccion, correo, celular, telefono))
            parametros = (id,nombre,direccion,correo,celular,telefono)
            db.exe_consulta(sql, parametros)

        self.mensajes.setText("Guardado correctamente.")
        self.mensajes.exec_()

    # METODO PARA LIMPIAR LOS EDITLINES
    def Limpiar(self):

        self.ui.Campo_Nombre.clear()
        self.ui.Campo_Direccion.clear()
        self.ui.Campo_Correo.clear()
        self.ui.Campo_Celular.clear()
        self.ui.Campo_Telefono.clear()

    # METODO PARA REALIZAR BUSQUEDAS.
    def Cargar(self):

        sql = ("SELECT * FROM F0101")

        reg = db.exe_consulta(sql).fetchall()

        if len(reg) > 0:
            fila = 0

            for p in reg:
                columna = 0

                for c in p:

                    celda = QTableWidgetItem(str(c))
                    self.ui.Tabla_Consulta.setItem(fila, columna, celda)
                    row = fila + 1
                    self.ui.Tabla_Consulta.setRowCount(row+1)
                    columna += 1
                
                fila += 1
        else:
            self.mensajes.setText("No existen registros en la base de datos.")
            self.mensajes.exec_()

    # MODULO PARA ELIMINAR REGISTROS DE LA TABLA.
    def Eliminar(self):
        
        selected = self.ui.Tabla_Consulta.currentIndex()
        if not selected.isValid() or len(self.ui.Tabla_Consulta.selectedItems()) < 1:
            return

        ids = self.ui.Tabla_Consulta.selectedItems()[0]
        sql = ("DELETE FROM F0101 WHERE ID =" + ids.text())
        db.exe_consulta(sql)

        self.ui.Tabla_Consulta.removeRow(selected.row())
        self.ui.Tabla_Consulta.setCurrentIndex(QModelIndex())
        self.mensajes.setText("Eliminado correctamente.")
        self.mensajes.exec_()
    
    # METODO PARA FILTRAR POR CUALQUIER CAMPO.
    def B(self):

        # RETORNA EL TEXTO DEL SELECTOR.
        filtro = self.ui.Selector_Filtro.itemText(self.ui.Selector_Filtro.currentIndex())
        # RETORONA LOS DATOS INGRESADOS EN EL EDITLINES.
        info = self.ui.Campo_a_Filtrar.text()

        sql = ("SELECT * FROM F0101 WHERE {} = '{}'").format(filtro, info)
        reg = db.exe_consulta(sql).fetchall()

        if len(reg) > 0:

            self.ui.Tabla_Consulta.clear()
            self.ui.Tabla_Consulta.setHorizontalHeaderLabels(['ID','Nombre','Dirección','Correo','Celular','Telefono'])
            for p in reg:
                columna = 0

                for c in p:

                    celda = QTableWidgetItem(str(c))
                    self.ui.Tabla_Consulta.setItem(0, columna, celda)
                    columna += 1

        else:
            self.mensajes.setText("No existen registros con este filtro.")
            self.mensajes.exec_()

    # METODO PARA BUSCAR EL ID DEL REGISTRO A ACTUALIZAR.
    def BuscarID(self):

        # RETORNA EL ID A BUSCAR
        id = self.ui.ID_A_Buscar.text()

        sql = ("SELECT * FROM F0101 WHERE ID = '{}'").format(id)
        reg = db.exe_consulta(sql).fetchall()
        
        # LE MANDO LA RESPUESTA DE LA CONSULTA A LA TABLA DEL DISEÑO.
        self.ui.Tabla_Actualizar.clear()
        self.ui.Tabla_Actualizar.setHorizontalHeaderLabels(['ID','Nombre','Dirección','Correo','Celular','Telefono'])
        
        if len(reg) > 0:

            fila = 0
            for p in reg:
                columna = 0

                for c in p:

                    celda = QTableWidgetItem(str(c))
                    print(c)
                    self.ui.Tabla_Actualizar.setItem(fila, columna, celda)
                    columna += 1
                pass
            pass
        else:
            self.mensajes.setText("Ingrese un ID valido o existente.")
            self.mensajes.exec_()           

    # METODO ACTUALIZAR LOS DATOS DE LA TABLA
    def Actualizar(self):

        # RETORNA EL CAMPO DEL SELECTOR. 
        campo = self.ui.Selector_Actualizar.itemText(self.ui.Selector_Actualizar.currentIndex())
        info = self.ui.Campo_A_Cambiar.text()
        id = self.ui.ID_A_Buscar.text()

        sql = ("UPDATE F0101 SET {} = '{}' WHERE ID = '{}'").format(campo,info,id)
        res = db.exe_consulta(sql).fetchall()

        if len(res) < 0:

            self.mensajes.setText("Ingrese un ID valido o existente.")
            self.mensajes.exec_()
        else:
            self.mensajes.setText("Registro actualizado correctamente.")
            self.mensajes.exec_()
            self.ui.Campo_A_Cambiar.clear()

    # METODO DE EXPORTACIÓN EN EXCEL.
    def Exportar(self):

        sql = ("SELECT * FROM F0101")
        res = db.exe_consulta(sql).fetchall()

        if len(res) > 0:

            col0 = "ID"
            col1 = "NOMBRE COMPLETO"
            col2 = "DIRECCIÓN"
            col3 = "CORREO"
            col4 = "CELULAR"
            col5 = "TELEFONO"

            for x in res:
                
                data = pd.DataFrame({col0:x,col1:x,col2:x,col3:x,col4:x,col5:x})
                print(data)

            excel = data
            print()
            print(excel)
            excel.to_excel('AGENDA_CONTACTOS.xlsx', sheet_name='DATOS CONTACTOS', index=False)

            self.mensajes.setText("Archivo 'AGENDA_CONTACTOS.xlsx' exportado correctamente, Guardado en la ubicación raiz del programa.")
            self.mensajes.exec_()

                

        else:
            self.mensajes.setText("Erro al exportar, valide si la base de datos tiene información.")
            self.mensajes.exec_()



# EJECUTABLE DEL PROGRAMA.
if __name__ == "__main__":

    app = QtWidgets.QApplication([])
    Ventana_Principal = Agenda_DB()
    Ventana_Principal.show()
    app.exec_()



