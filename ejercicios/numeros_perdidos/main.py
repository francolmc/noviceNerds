'''
 * Dado un array de enteros ordenado y sin repetidos,
 * crea una función que calcule y retorne todos los que faltan entre
 * el mayor y el menor.
 * - Lanza un error si el array de entrada no es correcto.
'''

lista_numeros = [2, 5, 8, 10, 12]

def tiene_valores_repetidos(numeros: list) -> bool:
    for numero in numeros:
        if numeros.count(numero) > 1:
            return True
    return False

def solo_valores_enteros(numeros) -> bool:
    pass

def esta_ordenado(numeros) -> bool:
    pass

def numeros_perdidos(numeros):
    pass

print(tiene_valores_repetidos(lista_numeros))