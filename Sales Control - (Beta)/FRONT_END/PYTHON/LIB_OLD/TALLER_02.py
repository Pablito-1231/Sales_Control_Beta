#ALMACEN DE ESCRITORIOS

ValorEscritorio = int(800000)

UnidadesXesc = int(input("1.) DIGITE LA CANTIDAD DE UNIDADES DESEA COMPRAR: "))

if UnidadesXesc > 0:

    #************************************ 10% DESCUENTO ********************************#
    if UnidadesXesc < 5:
        uniXesc = ValorEscritorio * UnidadesXesc
        Vdescontar = int(uniXesc * 0.1)
    #************************************ 20% DESCUENTO ********************************#
    if UnidadesXesc >= 5 and UnidadesXesc < 10:
        uniXesc = ValorEscritorio * UnidadesXesc
        Vdescontar = int(uniXesc * 0.2)
    #************************************ 40% DESCUENTO ********************************#
    if UnidadesXesc >= 10:
        uniXesc = ValorEscritorio * UnidadesXesc
        Vdescontar = int(uniXesc * 0.4)
    #***********************************************************************************#

    Vpagar = uniXesc - Vdescontar

    print("")
    print("VALOR NETO A PAGAR $ ",uniXesc)
    print("")
    print("VALOR DEL DESCUENTO $",Vdescontar)
    print("")
    print("VALOR A PAGAR $",Vpagar)
    print("")
else:
    print("")
    print("INGRESE MINIMO 1 UNIDAD")
    print("")