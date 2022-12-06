import digito_verificador as dv

identificacion = input("Introduzca su número de cédula: ")  
try:
    if(len(identificacion.replace(" ","")) == 0):
        print("Por favor introduzca un número de cédula")
    elif(len(identificacion.replace("-","").replace(" ","")) < 11):
        print("El número de cédula no es válido. Por favor introduzca un número de cédula válido")
    elif(len(identificacion.replace(" ","")) > 13):
        print("El número de cédula no es válido. Por favor introduzca un número de cédula válido")
    else:
        identificacion = identificacion.replace("-","").replace(" ","")
        numeros = []
        for i in range(0, len(identificacion)):
            numeros.append(int(identificacion[i]))

        resultado = dv.ValidarCedula(numeros)
        if(resultado):
            print("Cédula válida")
        else:
            print("Cédula inválida")
except ValueError as ex:
    print("El número de cédula no es válido. Por favor introduzca un número de cédula válido")
except Exception as ex:
    print("Ha ocurrido un error inesperado validando la cédula. Asegúrese de digitar un número de cédula válido")