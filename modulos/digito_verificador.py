def digito_verificador(rut_sin_dv: str) -> str:
    # Recorrer el string para realizar la multiplicacion
    # rut_invertido = reversed(rut_sin_dv)
    ultima_posicion = len(rut_sin_dv) - 1
    multiplicador = 2
    acumulador = 0
    for i in range(ultima_posicion, -1, -1):
        # Acumular los resultados de cada multiplicacion
        acumulador = acumulador + (int(rut_sin_dv[i]) * multiplicador)
        # Usar contador de 2 a N hasta 7 para multiplicar
        if multiplicador < 7:
            multiplicador = multiplicador + 1
        else:
            multiplicador = 2

    # Calcular modulo de 11 sobre el valor acumulado
    modulo = acumulador % 11
    # Restar 11 menos el modulo
    resta = 11 - modulo
    # Comprobar si el resultado es igual a 11, sera 0}
    if resta == 11:
        return 0
    # si es igual que 10 sera K y en caso contrario
    elif resta == 10:
        return "K"
    # ser el resultado de la resta.
    else:
        return resta

def validar_rut(rut: str) -> bool:
    separar = rut.split("-")
    digito = digito_verificador(separar[0])
    if digito == separar[1].upper():
        return True
    else:
        return False
