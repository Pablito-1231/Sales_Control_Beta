
#LOGIN DE USUARIO
#PABLO ANDRES BARRETO MONTERROSA

#USUARIOS QUE ESTAN REGISTRADOS EN EL SISTEMA#
from ast import Break
from threading import BrokenBarrierError

UsuarioR_01 = "PABLO"
UsuarioR_02 = "JEINEL"
UsuarioR_03 = "CSIAT"

#CLAVES REGISTRADAS PARA CADA USURIO#
Clave = int
ClaveUser_01 = "5689"
ClaveUser_02 = "0123"
ClaveUser_03 = "7458"

User = input("1.) INGRESE SU USUARIO:")
 
if User == UsuarioR_01 or User == UsuarioR_02 or User == UsuarioR_03:

    Clave = input("2.) INGRESE SU CONTRASEÑA:")

    if User == UsuarioR_01 and Clave == ClaveUser_01 or User == UsuarioR_02 and Clave == ClaveUser_02 or User == UsuarioR_03 and Clave == ClaveUser_03:
        print("BIENVENIDO")
    else:
        print("CONTRASEÑA INCORRECTA, INTENTE NUEVAMENTE")
else:
    print ("USUARIO NO EXISTE")