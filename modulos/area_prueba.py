from utilidades.digito_verificador import digito_verificador_v2
from utilidades.digito_verificador import digito_verificador
from utilidades.digito_verificador import validar_rut

rut = 27962409
dv = digito_verificador_v2(rut)

print("El digitivo verificador es:", dv)

rut_completo = "27962409-2"
valido = validar_rut(rut_completo)
print("El rut es valido?", valido)