"""
Encriptador y desencriptador de Cifrado de Vigenère.
El programa pide un texto y una llave, puede encriptar
o desencriptar el texto con la llave proporcionada.
"""

import os
import sys

"""
============== funciones de encriptación y desencriptación  =================
"""
def encriptar(txt_a_encriptar: str, llave: str):
    """
    (operadores aritméticos, funciones, ciclos)
    Recibe: a_encriptar texto, llave texto
    Cifra/Encripta un texto generando una letra nueva en base
    al valor numérico (unicode) de la letra correspondiente en el texto
    original y en la llave, este proceso se hace individualmente para
    cada letra (caracter) en el texto original.
    Devuelve: texto cifrado.
    """
    txt_encriptado = ""
    i = 0
    while i < len(txt_a_encriptar):
        indice_llave = i % len(llave)
        offset = llave[indice_llave]

        # Función ord(), es la función de la librería estándar
        # que voy a explicar en el README.md
        nueva_letra = ord(txt_a_encriptar[i]) + ord(offset)
        txt_encriptado += chr(nueva_letra)
        i += 1
    return txt_encriptado

def desencriptar(txt_encriptado: str, llave: str):
    """
    (operadores aritméticos, funciones, ciclos)
    Recibe: encriptado texto, llave texto
    Desencripta un texto previamente cifrado generando una letra nueva
    en base al valor numérico (unicode) de la letra correspondiente en
    el texto encriptado y en la llave, este proceso se hace
    individualmente para cada letra (caracter) en el texto encriptado.
    Devuelve: texto descifrado.
    """
    desencriptado = ""
    i = 0
    while i < len(txt_encriptado):
        indice_llave = i % len(llave)
        offset = llave[indice_llave]
        nueva_letra = ord(txt_encriptado[i]) - ord(offset)
        desencriptado += chr(nueva_letra)
        i += 1
    return desencriptado

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
    while True:
        clear()
        print("1.- Agregar texto")
        print("2.- Salir")
        subopcion_str = input("Elige una opción: ")
        subopcion = verificar_int(subopcion_str)
        match(subopcion):
            case 1:
                nuevo_texto, nueva_llave = leer_texto_y_llave()
                textos_originales[0].append(nuevo_texto)
                textos_originales[1].append(nueva_llave)
            case 2:
                textos_modificados: list[str] = []
                for i in range(0,len(textos_originales[0]),1):
                    encriptado = funcion_a_usar(
                        textos_originales[0][i], textos_originales[1][i]
                    )
                    textos_modificados.append(encriptado)

                printable_str = "Texto Original | Texto " + texto_a_mostrar
                i = 0
                while i < len(textos_originales[0]):
                    printable_str += (
                        f"\n{textos_originales[0][i]} | "
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
def verificar_int(texto: str) -> int:
    """
    Recibe: texto a verificar.
    Verifica que un str de un input se pueda pasar a int, en caso
    de que no se pueda, regresa -1 como valor de error.
    Regresa: el texto convertido en int o -1 en caso de error.
    """
    try:
        num = int(texto)
        return num
    except ValueError:
        return -1

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
    texto_encriptar = input("Ingresa el texto a utilizar: ")
    llave = input("Ingresa la llave para utilizar: ")
    return texto_encriptar, llave

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
while True:
    menu_inicial()
    opcion_str = input("Elige una opción: ")
    opcion = verificar_int(opcion_str)
    match(opcion):
        case 1:
            texto_a_encriptar, llave_input = leer_texto_y_llave()
            texto_encriptado = encriptar(texto_a_encriptar, llave_input)
            print_and_wait("Texto encriptado: " + texto_encriptado)
        case 2:
            texto_encriptado, llave_input = leer_texto_y_llave()
            texto_desencriptado = desencriptar(texto_encriptado, llave_input)
            print_and_wait("Texto desencriptado: " + texto_desencriptado)
        case 3:
            multiples_textos(encriptar, "Encriptado")
        case 4:
            multiples_textos(desencriptar, "Desencriptado")
        case 5:
            sys.exit()
        case _:
            print_and_wait("Opción incorrecta")
