
# CONVIERTE DE STRING A BINARIO
# ESTA FUNCIÓN ME RETORNA UN NUMERO BINARIO 0 Ó 1 PARA INICIAR EL MENU.
def binario(sn):

    if sn == "Si":
        enter = 1
    if sn == "No":
        enter = 0
    return enter

# VISUALIZA EL MENÚ
def menu():
    
    print('''
      ______________________________
    #|______________________________|#
    #|                              |# 
    #|   MENÚ REGISTRO & CONSULTA   |#
    #|______________________________|#
    #|                              |# 
    #|  1. REGISTRO DE USUARIOS.    |#
    #|  2. CONSULTAR USUARIOS.      |#
    #|  0. SALIR.                   |#
    #|______________________________|#
    #|______________________________|#
    
    ''')
    print()