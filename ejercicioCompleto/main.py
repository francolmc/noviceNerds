# Crear una aplicacion que muestre un menu al usuario con 5 opciones:
# 1.- Buscar persona
# 2.- Agregar persona
# 3.- Eliminar persona
# 4.- Editar persona
# 5.- Salir
# Cada una de las opciones debe permitir al usuario realizar las operaciones
# usando listas y diccionarios. Tambien debera repetir el programa hasta
# que el usuario seleccione la opcion 5.

def buscar_persona():
    pass

def agregar_persona():
    pass

def eliminar_persona():
    pass

def editar_persona():
    pass

# Funcion que valida si una opcion es correcta
# Si se encuentre etre 1 y 5
def es_opcion_correcta(opcion: str) -> bool:
    opciones = ("1", "2", "3", "4", "5")
    if opcion in opciones:
        return True
    else:
        return False

def menu():
    # Mostrar el menu mientras el usuario lo requiera
    while True:
        # Se muestra el menu al usuario
        print("MENU APLICACION")
        print("1.- Buscar persona")
        print("2.- Agregar persona")
        print("3.- Eliminar persona")
        print("4.- Editar persona")
        print("5.- Salir")
        # Se solicita al usuario que ingrese su opcion
        opcion = input("Ingresa tu opcion: ")
        # Validamos que la opcion sea correcta
        while not es_opcion_correcta(opcion):
            print("Error: Ud. ha ingresado un opcion incorrecta.")
            opcion = input("Ingrese una opcion entre 1 y 5: ")

        # Flujos segun la opcion
        if opcion == "1":
            buscar_persona()
        elif opcion == "2":
            agregar_persona()
        elif opcion == "3":
            eliminar_persona()
        elif opcion == "4":
            editar_persona()
        elif opcion == "5":
            break

    print("Ud. ha terminado el programa.")

menu()