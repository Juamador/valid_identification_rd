
def ValidarCedula(numeros):
    lista2 = []
    sumas = []
    digito_verificador = 0
    modulo = 0
    suma_total = 0
    verificador_modulo = 10

    digito_verificador = numeros[len(numeros)-1]
    for i in range(0, len(numeros) -1):
        resultado = 0
        if(i == 0 or i  % 2 == 0):
            resultado = numeros[i] * 1
        else:
            resultado = numeros[i] * 2
        
        lista2.append(resultado)

    for i in range(0, len(lista2)):
        if(lista2[i] > 9):
            sumas.append(lista2[i] - digito_verificador)
        else:
            sumas.append(lista2[i])

    for i in range(0, len(sumas)):
        suma_total += sumas[i]

    modulo = suma_total % verificador_modulo

    if((verificador_modulo - modulo) != digito_verificador):
        return False
    else:
        return True