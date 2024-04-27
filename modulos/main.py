import utilidades
import utilidades.digito_verificador

rut = input("Ingrese su rut con guion y digito verificador: ")
validar = utilidades.digito_verificador.validar_rut

if validar:
    print("Tu rut es valido.")
else:
    print("Tu rut no es valido.")
