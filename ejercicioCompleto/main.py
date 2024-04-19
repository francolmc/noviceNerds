# Crear una aplicacion que muestre un menu al usuario con 5 opciones:
# 1.- Buscar persona
# 2.- Agregar persona
# 3.- Eliminar persona
# 4.- Editar persona
# 5.- Salir
# Cada una de las opciones debe permitir al usuario realizar las operaciones
# usando listas y diccionarios. Tambien debera repetir el programa hasta
# que el usuario seleccione la opcion 5.

#Lista de personas
lista_personas = []

# Buscar persona por email y ternar el indice
def obtener_indice_por_email(email: str) -> int:
    # Hacemos referencia la variable lista_personas global
    global lista_personas
    # Variable indice para contar la posicion de la busqueda
    indice = 0
    # Ciclo que recorre la lista de peronas y lo asignar a la variable persona
    for persona in lista_personas:
        # Preguntas si la clave email de la personas es igual al email ingresado en la funcion
        # Recordar que la lista_personas es una lista de diccionarios.
        if persona["email"] == email:
            # En caso de encontrar a la persona por su email, retornamos el indice
            return indice
        # En caso de no encontrar y aun quedar elementos en la lista, le suma 1 al indice
        # Es una accion de contador
        indice = indice + 1
    # En caso de no encontrar el elemento en la lista, esto ocurre cuando el ciclo for
    # recorre toda la lista, retornara un -1 haciendo refrencia a que no encontro el valor.
    return -1

def buscar_persona():
    global lista_personas
    print("\nBUSCAR PERSONA\n")
    # Solicitar un email al usuario
    email = input("Ingrese el email de la persona a buscar: ")
    # Buscar el indice
    indice_persona = obtener_indice_por_email(email)
    # En caso de encontrar a la persona, Obtener diccionario e informar
    if indice_persona != -1:
        diccionario_persona = lista_personas[indice_persona]
        print("\nPERSONA ENCONTRADA\n")
        print("Email: \t " + diccionario_persona["email"])
        print("Nombres: \t " + diccionario_persona["nombres"])
        print("Apellidos: \t " + diccionario_persona["apellidos"])
        # En caso de NO encontrar a la persona, informar Error de no encontrado.
    else:
        print("ERROR: La persona no esta registrada.")

# Funcion que transforma los datos de una persona a un diccionario
def obtener_diccionario_persona(email: str, nombres: str, apellidos: str):
    persona = {
        "email": email,
        "nombres": nombres,
        "apellidos": apellidos
    }
    return persona

# Funcion para validar si un email esta disponible
def email_disponible(email: str) -> bool:
    return obtener_indice_por_email(email) == -1

# Funcion para validacion de si o no
def confirmar_operacion(mensaje: str) -> bool:
    opcion = input(mensaje + " [ingresar S o N]: ")
    while opcion.upper() != "S" and opcion.upper() != "N":
        print("ERROR: Debe ingresar una S o N.")
        opcion = input(mensaje + " [ingresar S o N]: ")
    if opcion.upper() == "S":
        return True
    elif opcion.upper() == "N":
        return False

def agregar_persona():
    global lista_personas
    print("\nINGRESAR PERSONA\n")
    # Solcicitar al usuario que ingrese un email
    email = input("Ingrese el email de la persona: ")
    # Validar que el email se encuentre disponible
    # Si el email no se encuentra disponible, informaremos al usuario y
    # volveremos solicitar un nuevo email.
    while not email_disponible(email):
        print("ERROR: El email ingresado ya esta registrado.")

        respuesta = confirmar_operacion("Desea ingresar a la persona?")    
        if respuesta:
            email = input("Ingrese nuevamente el email de la persona: ")
        else:
            print("Ud. ha cancelado el registro de la persona.")
            return
    # En caso que el email si este disponible, solicitaremos el resto de los datos
    nombres = input("Ingrese los nombres de la persona: ")
    apellidos = input("Ingrese los apellidos de la persona: ")
    # Crearemos un diccionario con los datos la persona y lo agregaremos
    # a la lista.
    persona = obtener_diccionario_persona(email, nombres, apellidos)
    lista_personas.append(persona)
    # Informamos al usuario que el proceso fue terminado    
    print("La persona fue registrada exitosamente.")

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
        else:
            break

    print("Ud. ha terminado el programa.")

menu()