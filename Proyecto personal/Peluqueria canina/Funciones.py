import os
# funciones/
# clientes.py
#  mascotas.py
#  turnos.py
#  servicios.py
#  archivos.py
#  validaciones.py

# funciones/clientes.py
# Alta de clientes.
def agregar_cliente(clientes:list) -> bool:
    id_nombre = input("ID cliente: ")
    nombre = input("Nombre: ")
    telefono = input("Teléfono: ")
    direccion = input("Dirección: ")

    cliente = [nombre, telefono, direccion, id_nombre]

    clientes.append(cliente)

    return True

def leer_cliente_csv(nombre_archivo:str) -> list: # Debo crear para usar en mascotas y turnos
    """Lectura de archivo csv 

    Args:
        nombre_archivo (str): nombre del archivo

    Returns:
        list: al archivo lo convierte en matriz
    """    
    matriz = []

    if type(nombre_archivo) == str and os.path.exists(nombre_archivo):
        with open(nombre_archivo,"r",encoding="utf-8") as archivo:
            archivo.readline() # elimina la primera linea
            for linea in archivo:
                fila = separar_cadena(linea)
                normalizar_datos_clientes(fila) # debo normalizar los numeros que tenga dicho archivo
                matriz.append(fila)
    return matriz

def normalizar_datos_clientes(lista_valores:list) -> None: # Debo realizar para mascotas y turnos
    """Normalizar datos

    Args:
        lista_valores (list): convierte de "123" a 123  de una lista
    """   
    # debo normalizar los numeros del archivo csv 
    if type(lista_valores) == list:
        lista_valores[0] = int(lista_valores[0])
        lista_valores[2] = int(lista_valores[2])

def reemplazar_caracteres(cadena_original:str,caracter_viejo:str,caracter_nuevo:str) -> str:
    """Reemplazar caracteres

    Args:
        cadena_original (str): cadena original
        caracter_viejo (str): caracter que se desea reeplazar
        caracter_nuevo (str): caracter por el cual se desea reemplazar

    Returns:
        str: convierte el caracter que se desea reemplazar por el cual se desea cambiar
    """    
    cadena_nueva = ""
    if type(cadena_original) == str and type(caracter_viejo) == str and type(caracter_nuevo) == str:
        for i in range(len(cadena_original)):
            if cadena_original[i] == caracter_viejo:
                cadena_nueva += caracter_nuevo
            else:
                cadena_nueva += cadena_original[i]
    return cadena_nueva

def separar_cadena(cadena: str, separador: str = ",") -> list:
    """Cadena que se desea separar

    Args:
        cadena (str): cadena original
        separador (str, optional): separa dependiendo en que parte de la cadena se encuentre. Defaults to ",".

    Returns:
        list: separa la cadena de caracteres y lo muestra como lista
    """    
    lista_separada = []
    cadena_nueva = ""

    if type(cadena) == str and (type(separador) == str and len(separador) == 1):
        for i in range(len(cadena)):
            if cadena[i] == separador:
                lista_separada.append(cadena_nueva)
                cadena_nueva = ""
            else:
                cadena_nueva += cadena[i]

        lista_separada.append(cadena_nueva)

    return lista_separada

def guardar_csv_matriz(nombre_archivo:str,cabecera:str,matriz:list) -> bool:
    """Crea un archivo csv de una matriz

    Args:
        nombre_archivo (str): introducir como quiere llamar al archivo
        cabecera (str): introducir que quiere colocar de cabecera
        matriz (list): introducir lista con notas de alumnos

    Returns:
        bool: crea un archivo csv con los datos de la matriz
    """    
    if type(nombre_archivo) == str and type(cabecera) == str and type(matriz) == list:
        retorno = True
        with open(nombre_archivo,"w",encoding="utf-8") as archivo:
            archivo.write(cabecera + "\n")
            
            for fil in range(len(matriz)):
                linea = unir_cadena(matriz[fil])
                if fil == len(matriz) - 1:
                    archivo.write(linea)
                else:
                    archivo.write(linea + "\n")
    else:
        retorno = False

    return retorno

def unir_cadena(lista:list,separador:str = ",") -> str:
    """Unir cadena

    Args:
        lista (list): ingresar lista de datos que se dea unir en una cadena
        separador (str, optional): lo que quiere que halla entre los datos. Defaults to ",".

    Returns:
        str: devuelve una cadena formada por los elementos, separados por el caracter indicado
    """
    cadena_nueva = ""
    if type(lista) == list and type(separador) == str:
        for i in range(len(lista)):
            if i == len(lista) - 1:
                cadena_nueva += f"{lista[i]}"
            else:
                cadena_nueva += f"{lista[i]}{separador}"
            
    return cadena_nueva

# Baja de clientes.
# def eliminar_cliente(lista_nombres:list):
#   input("Nombre del cliente que deseas eliminar: ")

def buscar_cliente(clientes: list, id_cliente: int) -> int:
    """Busca un cliente por su ID.

    Args:
        clientes (list): lista de clientes
        id_cliente (int): ID del cliente que se desea buscar

    Returns:
        int: posición del cliente dentro de la lista. Si no existe, devuelve -1.
    """
    posicion = -1

    if type(clientes) == list and type(id_cliente) == int:
        for i in range(len(clientes)):
            if clientes[i][0] == id_cliente:
                posicion = i
                break

    return posicion

def eliminar_cliente(clientes: list, id_cliente: int) -> bool:
    """Elimina un cliente de la lista.

    Args:
        clientes (list): lista de clientes
        id_cliente (int): ID del cliente a eliminar

    Returns:
        bool: True si se eliminó, False si no se encontró
    """
    retorno = False

    if type(clientes) == list and type(id_cliente) == int:
        posicion = buscar_cliente(clientes, id_cliente)

        if posicion != -1:
            clientes.pop(posicion)
            retorno = True

    return retorno


# Modificación.
# def modificar_cliente(lista_nombre:list):
#   input("nombre del cliente que deas cambiar: ")
def modificar_cliente(clientes: list, id_cliente: int) -> bool:
    retorno = False

    posicion = buscar_cliente(clientes, id_cliente)

    if posicion != -1:

        print("\n¿Qué desea modificar?")
        print("1. Nombre")
        print("2. Apellido")
        print("3. Teléfono")
        print("0. Cancelar")

        opcion = input("Seleccione una opción: ")

        match opcion:
            case "1":
                clientes[posicion][1] = input("Nuevo nombre: ")
                retorno = True

            case "2":
                clientes[posicion][2] = input("Nuevo apellido: ")
                retorno = True

            case "3":
                clientes[posicion][3] = input("Nuevo teléfono: ")
                retorno = True

    return retorno


# Listado.
# def lista_clientes()

# funciones/mascotas.py
# Alta de mascotas.
def agregar_mascota(mascota:list) -> bool:
    id_cliente = input("Nombre del perro: ")
    id_mascota = input("Nombre del perro: ")
    nombre = input("Nombre del perro: ")
    raza = input("Nombre del perro: ")
    tamaño = input("Nombre del perro: ")
    sexo = input("Nombre del perro: ")
    observaciones = input("Nombre del dueño: ")

    mascota = [id_cliente, id_mascota, nombre, raza, tamaño, sexo, observaciones]

    mascota.append(mascota)

    return True
def leer_mascota_csv(nombre_archivo:str) -> list: # Debo crear para usar en mascotas y turnos
    """Lectura de archivo csv 

    Args:
        nombre_archivo (str): nombre del archivo

    Returns:
        list: al archivo lo convierte en matriz
    """    
    matriz = []

    if type(nombre_archivo) == str and os.path.exists(nombre_archivo):
        with open(nombre_archivo,"r",encoding="utf-8") as archivo:
            archivo.readline() # elimina la primera linea
            for linea in archivo:
                fila = separar_cadena(linea)
                normalizar_datos_mascota(fila) # debo normalizar los numeros que tenga dicho archivo
                matriz.append(fila)
    return matriz

def normalizar_datos_mascota(lista_valores:list) -> None: # Debo realizar para mascotas y turnos
    """Normalizar datos

    Args:
        lista_valores (list): convierte de "123" a 123  de una lista
    """   
    # debo normalizar los numeros del archivo csv 
    if type(lista_valores) == list:
        lista_valores[0] = int(lista_valores[0])
        lista_valores[1] = int(lista_valores[1])


# Modificación.
# def modificar_mascota()
# Buscar por dueño.
# def buscar_mascota_dueño

# funciones/turnos.py
# Crear turno.
# def crear_turno()
def leer_turno_csv(nombre_archivo:str) -> list: # Debo crear para usar en mascotas y turnos
    """Lectura de archivo csv 

    Args:
        nombre_archivo (str): nombre del archivo

    Returns:
        list: al archivo lo convierte en matriz
    """    
    matriz = []

    if type(nombre_archivo) == str and os.path.exists(nombre_archivo):
        with open(nombre_archivo,"r",encoding="utf-8") as archivo:
            archivo.readline() # elimina la primera linea
            for linea in archivo:
                fila = separar_cadena(linea)
                normalizar_datos_turnos(fila) # debo normalizar los numeros que tenga dicho archivo
                matriz.append(fila)
    return matriz

def normalizar_datos_turnos(lista_valores:list) -> None: # Debo realizar para mascotas y turnos
    """Normalizar datos

    Args:
        lista_valores (list): convierte de "123" a 123  de una lista
    """   
    # debo normalizar los numeros del archivo csv 
    if type(lista_valores) == list:
        lista_valores[1] = int(lista_valores[1])

# Cancelar turno.
# def cancelar_turno()
# Mostrar agenda.
# def mostrar_agenda()

# funciones/servicios.py
# Servicio completo
# Bano y retoques
# Uñas.
# Precios.

# funciones/archivos.py
# Leer CSV.
# Guardar CSV.
# Buscar registros.

# funciones/validaciones.py
# Validar teléfono.
# def agregar_telefono()
# Validar fecha.
# def agregar_fecha()
# Validar opciones del menú.

