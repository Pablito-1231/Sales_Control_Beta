
# IMPORTAMOS LAS LIBRERIAS NECESARIAS.
import time
import sqlite3 as SQL
import LIB_FUNCIONES.Binario_menu_registro as bmr
import LIB_FUNCIONES.Insertar_consultar_actualizar_eliminar_DB as icae

# SQL *******************************************************************************************************************************************

# NOS CONECTAMOS A LA BASE DE DATOS DEL MAESTRO DE EMPLEADO.
# CREAMOS EL CURSOR.
# CREAMOS LA TABLA SOLO SI NO EXISTE & ASIGNAMOS LOS CAMPOS.

connextion = SQL.connect("DATABASE.db")
Cuursor = connextion.cursor()
Cuursor.execute('''create table if not exists F060116

(ID integer primary key autoincrement,NOMBRE text, CEDULA integer, EDAD integer, CARGO text, SEXO text, USUARIO text, CONTRASEÑA integer)''')

# SQL *******************************************************************************************************************************************

# INICIA O FINALIZA EL PROGRAMA.
print()
sn = input('''> ¡Hola, Bienvenido!, ¿Deseas abrir el menú de Registro & Consulta de empleados?

) Si.
) No.

Respuesta:> ''')

# LLAMO LA FUNCIÓN BIANRIO PARA QUE ME RETORNE 0 Ó 1.
bmr.binario(sn)

# ENTRADA - SI ES (1) ENTRA, SI ES (0) NO ENTRA.
while bmr.binario(sn) == 1:

    # VISUALIZO EL MENU Y ESCOJO UNA OPCIÓN.
    bmr.menu()

    print()
    opcion = int(input("> Escoja una opción del menú: "))
    print()

    opcion_01 = opcion
    opcion_02 = opcion
    opcion_Exit = opcion

    # OPCIÓN 1 - ENTRA A LA OPCIÓN DE REGISTRO DEL MENU.
    while opcion_01 == 1:

        List_Reg = []

        print()
        print("|_____________________________________________________ REGISTRO DE EMPLEADOS _____________________________________________________|")
        print()

        #NOMBRE
        nombre = input("1.) NOMBRE COMPLETO: ")
        List_Reg.append(nombre)
        print()

        #INDENTIFICACIÓN
        id = int(input("2.) IDENTIFICACIÓN: "))
        List_Reg.append(id)
        print()

        #EDAD
        edad = int(input("3.) EDAD: "))
        List_Reg.append(edad)
        print()

        #SEMESTRE
        cargo = input("4.) CARGO ASIGNADO: ")
        List_Reg.append(cargo)
        print()

        #GENERO
        gen = int(input('''5.) GENERO:
        
        0 - MASCULINO
        1 - FEMENINO
        2 - NO BINARIO
        
        Escoje una opción:> '''))

        listgen = ["MASCULINO","FEMENINO","NO BINARIO"]
        genero = listgen[gen]
        
        print()
        print("- SELECCIONASTE: ",genero)
        List_Reg.append(genero)
        print()

        #USUARIO
        user = input("6.) REGISTRAR USUARIO: ")
        List_Reg.append(user)
        print()

        #CONTRASEÑA
        passw = input("7.) REGISTRAR CONTRASEÑA: ")
        List_Reg.append(passw)

        print()
        print("- Loanding...")
        time.sleep(3)
        print("- ¡Registro exitoso!")

        print()
        print("|___________________________________________________ FIN REGISTRO DE EMPLEADOS ___________________________________________________|")

        print()
        print(List_Reg)#prueba
        print()

        Cuursor.execute ("INSERT INTO F060116 values (?,?,?,?,?,?,?)", List_Reg)
        connextion.commit()
        print()

        sn = input('''
        
> ¿Desea registrar otro empleado?

) Si.
) No.

Respuesta:> ''')

        # RETORNA 0 Ó 1
        bmr.binario(sn)

        #SI LA FUNCIÓN RETORNA 1 REPITE EL CICLO
        if bmr.binario(sn) == 1:

            opcion_01 = 1

        else:

            print()
            print("Volviendo al menú principal...")
            time.sleep(1)
            print()
            break





















    
    # OPCIÓN 2 -
    while opcion_02 == 2:
        
        print()

    # OPCIÓN 0 - SALIDA - SOLO CUADO ESCOJAN LA OPCIÓN (0).
    if opcion_Exit == 0:

        print()
        print("Loanding...")
        time.sleep(2)
        print("Close Complete.")
        break

# SALIDA - SOLO CUANDO DIGAN "No".
if bmr.binario(sn) == 0:

    print()
    print("Loanding...")
    time.sleep(2)
    print("Close Complete.")



