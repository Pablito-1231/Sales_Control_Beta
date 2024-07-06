
#MENU LISTAS TUPLAS DICCIONARIOS
import time
import LIB_FUNCIONES.Binario_menu_registro as bmr

position = 0
muestraMenu = 0
veces = 1

# INICIO O FINALIZO EL PROCESO
print()
sn = input("- HOLA, BIENVENIDO, ¿DESEA ABRIR EL MENU DE REGISTRO Y CONSULTA DE USUARIOS? ESCRIBA si ó no: ")

bmr.binario(sn)

ListReg = []

# SI ES (1) INICIA SI ES (0) FINALIZA
while bmr.binario(sn) == 1:

    # VISUALIZO EL MENU Y ESCOJO UNA OPCIÓN
    if muestraMenu != 1:
        bmr.menu()

        opcion = int(input("- SELECCIONE UNA OPCIÓN: "))

        opcion01 = opcion
        opcion02 = opcion
        opcionExit = opcion

    # FINALIZA EL CICLO PRINCIPAL
    if opcionExit == 0:

        print()
        print("Loanding...")
        time.sleep(2)
        print("Close Complete.")
        print()
        break

    # ENTRO A LA OPCIÓN DE REGISTRO DEL MENU Y ALMACENO MIS REGISTROS EN UN DICCIONARIO
    while opcion01 == 1 :
        
        print()
        print("|************** REGISTRO DE USUARIOS **************|")
        print()

        IDclave = position

        #NOMBRE
        nombre = input("1.) NOMBRE COMPLETO: ")
        print()

        #INDENTIFICACIÓN
        id = int(input("2.) IDENTIFICACIÓN: "))
        print()

        #EDAD
        edad = int(input("3.) EDAD: "))
        print()

        #SEMESTRE
        semes = int(input("4.) SEMESTRE ACTUAL: "))
        print()

        #GENERO
        genero = int(input("5). GENERO: 0 - MASCULINO, 1 - FEMENINO, 2 - NO BINARIO: "))
        listgen = ["MASCULINO","FEMENINO","NO BINARIO"]
        print()
        print("- SELECCIONASTE: ",listgen[genero])
        print()

        #USUARIO
        user = input("6). REGISTRAR USUARIO: ")
        print()

        #CONTRASEÑA
        passw = input("7). REGISTRAR CONTRASEÑA: ")
        print()

        print("- ¡Registro exitoso!, tu ID asociado es: ","ID_#" + str(IDclave))
        print()

        print("|*********** FIN REGISTRO DE USUARIOS ************|")
        print()

        # DICCIONARIO PARA INDEXAR LOS DATOS DE REGISTRO
        dicc_Reg = {"NOMBRE :":nombre,"IDENTIFICACIÓN :":id,"EDAD :":edad,"SEMESTRE :":semes,"GENERO :":listgen[genero],"USUARIO :":user,"CONTRASEÑA :":passw}
        ListReg.append(dicc_Reg)

        #PREGUNTA SI VUELVE A REPETIR EL CICLO O NO
        sn = input("¿DESEA REALIZAR UN NUEVO REGISTRO? si ó no: ")
                
        # RETORNA 0 Ó 1
        bmr.binario(sn)

        #SI LA FUNCIÓN RETORNA 1 REPITE EL CICLO
        if bmr.binario(sn) == 1:

            position += 1
            opcion01 = 1
            veces +=1

        else:

            print()
            print("Volviendo al menú principal...")
            time.sleep(1)
            print()
            opcion01 = 3
            
    # FIN DEL WHILE - OPCIÓN 1
 
    # INICIA LA OPCIÓN DE CONSULTA POR USUARIO
    while opcion02 == 2:

        print()
        print("|**************** CONSULTAR DATOS POR USUARIO ***************|")
        print()

        ValidaID = int(input("1). INGRESA TU CODIGO ID_# : "))


        #ACCEDEMOS AL ELEMENTO DE LA LISTA CON LA POSICIÓN DEL ID
        for z in range(ValidaID,len(ListReg),veces):

            datos = ListReg[z]

            #ACCEDEMOS A CADA CLAVE Y VALOR DE CADA DICCIONRIO
            for k,v in datos.items():

                print(k,v)

        print()
        print("|************** FIN CONSULTA DE DATOS POR USUARIOS ************|")
        print()

        #PREGUNTA SI VUELVE A REPETIR EL CICLO O NO
        sn = input("¿DESEA REALIZAR UNA NUEVA CONSULTA? si ó no: ")
                
        # RETORNA 0 Ó 1
        bmr.binario(sn)

        #SI LA FUNCIÓN RETORNA 1 REPITE EL CICLO
        if bmr.binario(sn) == 1:

            opcion02 = 2

        else:

            print()
            print("Volviendo al menú principal...")
            time.sleep(1)
            print()
            opcion02 = 3


    bmr.menu()
    sn = "si"
    opcion = int(input("- SELECCIONE UNA OPCIÓN: "))
    print()

    # SALIR TOTALMENTE
    if opcion == 0:
        
        opcionExit = 0
        bmr.binario(sn="no")

    # VUELVE AL LA OPCIÓN 1
    if opcion == 1:

        muestraMenu = 1
        opcion01 = 1
        bmr.binario(sn="si")

    # VUELVE AL LA OPCIÓN 2
    if opcion == 2:

        muestraMenu = 1
        opcion02 = 2
        bmr.binario(sn="si")

# SALIDA
if bmr.binario(sn) == 0:

    print()
    print("Loanding...")
    time.sleep(2)
    print("Close Complete.")

else:

    # SLAIDA PARA QUE NO MUESTRE EL MENSAJE DE SALIDA 2 VECES
    if opcionExit == 0:

        print()

    else:

        print()
        print("Loanding...")
        time.sleep(2)
        print("Close Complete.")