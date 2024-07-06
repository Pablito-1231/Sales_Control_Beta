#CALCULAR EL TIPO, AREA, PERIMETRO.

#PABLO ANDRES BARRETO MONTERROSA
#15/03/2022

#**************TIPO***********************************************************************************************************************************

#Equilátero: Todos sus lados son iguales.
#Isósceles: Dos de sus tres lados son de igual longitud.
#Escaleno: Todos sus lados son de diferente longitud.'''

import math

Lado_01 = float(input("1.) INGRESAR PRIMER LADO: "))
Lado_02 = float(input("2.) INGRESAR SEGUNDO LADO: "))
Lado_03 = float(input("3.) INGRESAR TERCER LADO: "))

def TipoTriangulo (Lado_01, Lado_02, Lado_03):

    if Lado_01 == Lado_02 and Lado_01 == Lado_03 and Lado_02 == Lado_01 and Lado_02 == Lado_03 and Lado_03 == Lado_01 and Lado_03 == Lado_02:
        
        Tipo = "EQUILATERO"
        return Tipo

    else:
        if Lado_01 == Lado_02 != Lado_03 or Lado_01 == Lado_03 != Lado_02 or Lado_02 == Lado_01 != Lado_03 or Lado_02 == Lado_03 != Lado_01 or Lado_03 == Lado_01 != Lado_02 or Lado_03 == Lado_02 != Lado_01:
            Tipo = "ISÓSCELES"
            return Tipo

        else:
            if Lado_01 != Lado_02 and Lado_01 != Lado_03 and Lado_02 != Lado_01 and Lado_02 != Lado_03 and Lado_03 != Lado_01 and Lado_03 != Lado_02:
                
                Tipo = "ESCALENO"
                return Tipo

Resultado = TipoTriangulo (Lado_01, Lado_02, Lado_03)
print(" - EL TRIANGULO ES TIPO: ", Resultado)


#**************AREA***********************************************************************************************************************************

def AreaTriangulo (Lado_01, Lado_02, Lado_03):

    Semiperimetro = float(Lado_01 + Lado_02 + Lado_03)/2
    Area = float((Semiperimetro * (Semiperimetro - Lado_01) * (Semiperimetro - Lado_02) * (Semiperimetro - Lado_03)**1/2))
    return Area

ValorArea = AreaTriangulo (Lado_01, Lado_02, Lado_03)
print(" - EL AREA ES DE: ",ValorArea ,"Mts²")

#*************PERIMETRO*******************************************************************************************************************************

def PerimetroTriangulo (Lado_01, Lado_02, Lado_03):

    Perimetro = float(Lado_01 + Lado_02 + Lado_03)
    return Perimetro

ValorPerimetro = PerimetroTriangulo (Lado_01, Lado_02, Lado_03)
print(" - EL PERIMETRO ES DE: ", ValorPerimetro, "Mts")

#*************FIN*************************************************************************************************************************************
