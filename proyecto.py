"""
Encriptador y desencriptador de Cifrado de Vigenère.
El programa pide un texto y una llave, puede encriptar
o desencriptar el texto con la llave proporcionada.
"""

import os

"""
============== funciones de encriptación y desencriptación  =================
"""
def encriptar(texto_a_encriptar: str, llave: str):
    """
    (operadores aritméticos, funciones, ciclos)
    Recibe: texto_a_encriptar texto, llave texto
    Cifra/Encripta un texto generando una letra nueva en base
    al valor numérico (unicode) de la letra correspondiente en el texto
    original y en la llave, este proceso se hace individualmente para
    cada letra (caracter) en el texto original.
    Devuelve: texto cifrado.
    """
    texto_encriptado = ""
    for i in range(len(texto_a_encriptar)):
        indice_llave = i % len(llave)
        offset = llave[indice_llave]

        # Función ord(), es la función de la librería estándar
        # que voy a explicar en el README.md
        nueva_letra = ord(texto_a_encriptar[i]) + ord(offset)
        texto_encriptado += chr(nueva_letra)
    return texto_encriptado

def desencriptar(texto_encriptado: str, llave: str):
    """
    (operadores aritméticos, funciones, ciclos)
    Recibe: texto_encriptado texto, llave texto
    Desencripta un texto previamente cifrado generando una letra nueva
    en base al valor numérico (unicode) de la letra correspondiente en
    el texto encriptado y en la llave, este proceso se hace
    individualmente para cada letra (caracter) en el texto encriptado.
    Devuelve: texto descifrado.
    """
    texto_desencriptado = ""
    for i in range(len(texto_encriptado)):
        indice_llave = i % len(llave)
        offset = llave[indice_llave]
        nueva_letra = ord(texto_encriptado[i]) - ord(offset)
        texto_desencriptado += chr(nueva_letra)
    return texto_desencriptado

def multiples_textos(funcion_a_usar, texto_a_mostrar: str):
    """
    Recibe: la función que se va a utilizar, un texto a mostrar.
    Permite la entrada de múltiple pares de textos y llaves, luego
    aplica la función que se le pasa como argumento con el texto y
    la llave como argumentos. Facilita la implementación de
    encriptar y desencriptar múltiples textos.
    No devuelve nada.
    """
    textos_originales: list[list[str]] = [[], []]
    # El primer arreglo tiene los textos, el segundo las llaves.
    # textos = [[texto1, texto2, texto3],
    #           [llave1, llave2, llave3]]
    while (True):
        clear()
        print("1.- Agregar texto")
        print("2.- Salir")
        opcion_2 = int(input("Elige una opción: "))
        match(opcion_2):
            case 1:
                nuevo_texto, nueva_llave = leer_texto_y_llave()
                textos_originales[0].append(nuevo_texto)
                textos_originales[1].append(nueva_llave)
            case 2:
                textos_modificados: list[str] = []
                for i in range(0,len(textos_originales[0]),1):
                    texto_encriptado = funcion_a_usar(
                        textos_originales[0][i], textos_originales[1][i]
                    )
                    textos_modificados.append(texto_encriptado)

                printable_str = "Texto Original | Texto " + texto_a_mostrar
                i = 0
                while i < len(textos_originales[0]):
                    printable_str += (
                        f"\n{textos_originales[0][i]} |"
                        f"{textos_modificados[i]}"
                    )
                    i += 1
                print_and_wait(printable_str)
                break
            case _:
                print_and_wait("Opción incorrecta")

"""
============== funciones de ayuda (helper functions)  =================
"""
def clear():
    """
    (función de la librería estándar)
    No recibe argumentos.
    Usa un comando del sistema para limpiar
    la consola.
    No devuelve nada.
    """
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

def menu_inicial():
    """
    No recibe nada.
    Imprime las opciones del menú inicial.
    No devuelve nada.
    """
    clear()
    print("1.- Encriptar texto")
    print("2.- Desencriptar texto")
    print("3.- Encriptrar múltiples textos")
    print("4.- Desencriptar múltiples textos")
    print("5.- Salir")

def leer_texto_y_llave():
    """
    No recibe nada.
    Pide al usuario que ingrese un texto y una llave.
    Devuelve: un texto y una llave (ambos son str).
    """
    texto_a_encriptar = input("Ingresa el texto a utilizar: ")
    llave = input("Ingresa la llave para utilizar: ")
    return texto_a_encriptar, llave

def print_and_wait(text: str):
    """
    Recibe: text (str)
    Imprime un texto y lo mantiene en pantalla hasta que la tecla 'enter'
    sea presionada.
    No devuelve nada.
    """
    clear()
    print(text)
    _ = input("\nPresiona enter para continuar...")


"""
============== Main =================
"""
while (True):
    menu_inicial()
    opcion = int(input("Elige una opción: "))
    match(opcion):
        case 1:
            texto_a_encriptar, llave = leer_texto_y_llave()
            texto_encriptado = encriptar(texto_a_encriptar, llave)
            print_and_wait("Texto encriptado: " + texto_encriptado)
        case 2:
            texto_encriptado, llave = leer_texto_y_llave()
            texto_desencriptado = desencriptar(texto_encriptado, llave)
            print_and_wait("Texto desencriptado: " + texto_desencriptado)
        case 3:
            multiples_textos(encriptar, "Encriptado")
        case 4:
            multiples_textos(desencriptar, "Desencriptado")
        case 5:
            exit()
        case _:
            print_and_wait("Opción incorrecta")
