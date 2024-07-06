#PROMEDIOS UNIVERSIDAD

print("")
print(" |**************************************************** REGISTRO DE MATRICULA Y VALIDACIÓN DE DESCUENTOS POR PROMEDIOS ACADEMICOS ****************************************************| ")
print("")
print("- Este programa validara su promedio academico y de acuerdo a dicho promedio usted podra matricularse y obtener un porcentaje de descuento en la matricula.")
print("")


print("1.) DILIGENCIE EL SIGUIENTE FORMULARIO.")
print("")
print("-   DATOS INICIALES")
print("")

CredPregrado = int(50000)
CredPosgrado = int(300000)

carrera_01 = "pregrado"
carrera_02 = "posgrado"

Estudiante = input("° REGISTRE SU NOMBRE COMPLETO: ")

if Estudiante != "":


    carrera = input("° ¿USTED ES ESTUDIANTE DE PREGRADO O POSTGRADO?, ESCRIBA 'pregrado' O 'posgrado': ")

    if carrera == carrera_01 or carrera == carrera_02: #VALIDACIÓN

        promedioA = float(input("° DIGITE SU PROMEDIO ACADEMICO: "))

        if promedioA > 0:   #VALIDACIÓN
            #*********************** 28 CREDITOS PREGRADO *****************************#
            if promedioA >= 4.5 and carrera == carrera_01:
                
                Vmatricula = CredPregrado * 28
                VDmatricula = Vmatricula * 0.25
                Vtotal = Vmatricula - VDmatricula
            #*********************** 25 CREDITOS PREGRADO *****************************#
            if promedioA >= 4.0 and promedioA < 4.5 and carrera == carrera_01:

                Vmatricula = CredPregrado * 25
                VDmatricula = Vmatricula * 0.10
                Vtotal = Vmatricula - VDmatricula
            #*********************** 20 CREDITOS PREGRADO *****************************#
            if promedioA > 3.5 and promedioA < 4.0 and carrera == carrera_01:

                Vmatricula = CredPregrado * 20
                VDmatricula = 0
                Vtotal = Vmatricula
            #*********************** 15 CREDITOS PREGRADO *****************************#
            if promedioA >= 2.5 and promedioA < 3.5 and carrera == carrera_01:

                Vmatricula = CredPregrado * 15
                VDmatricula = 0
                Vtotal = Vmatricula
            #********************** SIN MATRICULA PREGRADO ****************************#
            if promedioA < 2.5 and carrera == carrera_01:

                Vmatricula = 0
                VDmatricula = 0
                Vtotal = 0
            #********************** 20 CREDITOS POSGRADO ******************************#
            if promedioA >= 4.5 and carrera == carrera_02:

                Vmatricula = CredPregrado * 20
                VDmatricula = Vmatricula * 0.20
                Vtotal = Vmatricula - VDmatricula
            #********************** 10 CREDITOS POSGRADO ******************************#
            if promedioA < 4.5 and promedioA >= 3.5 and carrera == carrera_02:

                Vmatricula = CredPregrado * 10
                VDmatricula = 0
                Vtotal = Vmatricula - VDmatricula
            #********************** SIN MATRICULA POSGRADO ****************************#
            if promedioA < 3.5 and carrera == carrera_02:

                Vmatricula = 0
                VDmatricula = 0
                Vtotal = 0

            if Vtotal != 0:
                print("")
                print(" ===================== DESPRENDIBLE DE MATRICULA ===================== ")
                print("")
                print("- NOMBRE DEL ESTUDIANTE")
                print("-",Estudiante)
                print(" =================================== ")
                print("- GRADO AL QUE PERTENECE")
                print("-",carrera)
                print(" =================================== ")
                print("- VALOR NETO")
                print("-",Vmatricula)
                print(" =================================== ")
                print("- VALOR DEL DESCUENTO APLICADO")
                print("-",VDmatricula)
                print(" =================================== ")
                print("- VALOR TOTAL A PAGAR")
                print("-",Vtotal)
                print(" ======================================================================")
            else:
                print("CON ESE PROMEDIO NO LO RECLUTA NI LA GUERRILLA JAJAJA")
        else:
            print(" ************* EL PROMEDIO INGRESADO NO ES VALIDO ************* ")
    else:
        print("")
        print(" ************* POR FAVOR INGRESE UN GRADO VALIDO ************* ")
        print("")
else:
    print("POR FAVOR REGISTRE SU NOMBRE")