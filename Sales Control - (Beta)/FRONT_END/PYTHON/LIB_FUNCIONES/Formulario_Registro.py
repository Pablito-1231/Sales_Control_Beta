
import time



def Formulario_Reg():
    
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