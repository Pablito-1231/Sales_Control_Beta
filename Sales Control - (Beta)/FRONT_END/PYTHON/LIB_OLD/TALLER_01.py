#INTEGRNTES: PABLO ANDRES BARRETO - JEINEL GUTIERREZ

#TARIFAS DE TELEFONIA CELULAR "MOVISTAR"

print("")

Plan_01 = "Plan 1"
Plan_02 = "Plan 2"
Plan_03 = "Plan 3"
Plan_04 = "Plan 4"

Min = 0

NombreC = input("1.) INGRESE EL NOMBRE DEL CLIENTE: ")

if NombreC != "":

    Plan = input("2.) INGRESE EL PLAN ADQUIRIDO: ")

    if Plan != Plan_04 and Plan != Plan_03 and Plan != Plan_02 and Plan != Plan_01:
        print("INGRESE UN PLAN VALIDO Y DEJE DE MAMAR GALLO >:V")
    else:
        Min = float(input("3.) REGISTRE LOS MINUTOS CONSUMIDOS: "))

        Tarifa_01 = int(150)
        Tarifa_02 = int(200)
        Tarifa_03 = int(300)
        Tarifa_04 = int(400)

        if Min > 0:

            #************************************PLAN 1********************************#
            if Plan == Plan_01:
                minXtar = int(Min * Tarifa_01)
            #************************************PLAN 2********************************#
            if Plan == Plan_02:
                minXtar = int(Min * Tarifa_02)
            #************************************PLAN 3********************************#
            if Plan == Plan_03:
                minXtar = int(Min * Tarifa_03)
            #************************************PLAN 4********************************#
            if Plan == Plan_04:
                minXtar = int(Min * Tarifa_04)
            #**************************************************************************#

            Valor_01 = minXtar #LE DA VALOR DE ENTRADA A LA FUNCIÓN

            #==========================FUNCIÓN DESCUENTO================================
            def Descuento (Valor_01):

                Vdescuento = Valor_01 * 0.1
                return Vdescuento

            ValorDescuento = int(Descuento (Valor_01))
            #===========================================================================


            if Min > 100:
                ValorDescuento = Descuento(Valor_01)
                total = minXtar - ValorDescuento
            else:
                ValorDescuento = 0
                total = minXtar

            print("")
            print("**************************************")
            print("* EL NOMBRE DE USUARIO ES: ",NombreC)
            print("* EL PLAN QUE ADQUIRIDO ES: ",Plan)
            print("======================================")
            print("* VALOR NETO $",minXtar)
            print("* EL VALOR DEL DESCUENTO ES DE $",ValorDescuento)
            print("======================================")
            print("* EL TOTAL A PAGAR ES $",total)
            print("**************************************")
            print("")

        else:
            print("INGRESE UN MONTO DE MINUTOS VALIDO")
else:
    print("POR FAVOR REGISTRE SU NOMBRE")