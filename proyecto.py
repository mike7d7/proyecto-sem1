"""
Encriptador y desencriptador de Cifrado de Vigenère.
El programa pide un texto y una llave, puede encriptar
o desencriptar el texto con la llave proporcionada.
"""

import os
import sys
import base64

"""
============== funciones de encriptación y desencriptación  =================
"""
def encriptar(txt_a_encriptar: str, llave: str):
    """
    (operadores aritméticos, funciones, ciclos, condicionales,
    función librería estándar)
    Recibe: a_encriptar texto, llave texto
    Cifra/Encripta un texto generando una letra nueva en base
    al valor numérico (unicode) de la letra correspondiente en el texto
    original y en la llave, este proceso se hace individualmente para
    cada letra (caracter) en el texto original.
    Una vez cifrado, codifica el texto en base 64 para evitar
    problemas con caracteres Unicode invisibles o de tamaño 0.
    Devuelve: texto cifrado, si los valores son válidos.
    """
    txt_encriptado = ""
    i = 0
    if len(llave) == 0:
        return ("Error en los valores ingresados, la llave"
                + " no puede estar vacía", False)

    while i < len(txt_a_encriptar):
        indice_llave = i % len(llave)
        offset = llave[indice_llave]

        # Función ord(), es la función de la librería estándar
        # que voy a explicar en el README.md
        nueva_letra = suma_verificada(ord(txt_a_encriptar[i]), ord(offset))
        if nueva_letra == -1:
            return ("Error en los valores ingresados, el resultado está"
                    + " fuera de valores Unicode", False)

        txt_encriptado += chr(nueva_letra)
        i += 1
    # Codificamos el texto encriptado en base 64 para evitar problemas con
    # caracteres Unicode invisibles o de tamaño 0
    txt_encriptado2 = base64.b64encode(txt_encriptado.encode('utf-8')) \
                      .decode('utf-8')
    return txt_encriptado2, True

def desencriptar(txt_encriptado: str, llave: str):
    """
    (operadores aritméticos, funciones, ciclos, condicionales,
    funciones librería estándar)
    Recibe: encriptado texto, llave texto
    Desencripta un texto previamente cifrado generando una letra nueva
    en base al valor numérico (unicode) de la letra correspondiente en
    el texto encriptado y en la llave, este proceso se hace
    individualmente para cada letra (caracter) en el texto encriptado.
    Devuelve: texto descifrado, si los valores son válidos.
    """
    try:
        txt_encriptado = base64.b64decode(txt_encriptado).decode('utf-8')
    except ValueError:
        return ("Error en los valores ingresados, el texto encriptado"
                + " no fue generado con este programa", False)
    desencriptado = ""
    i = 0
    while i < len(txt_encriptado):
        indice_llave = i % len(llave)
        offset = llave[indice_llave]

        nueva_letra = resta_verificada(ord(txt_encriptado[i]), ord(offset))
        if nueva_letra == -1:
            return ("Error en los valores ingresados, el resultado está"
                    + " fuera de valores Unicode", False)

        desencriptado += chr(nueva_letra)
        i += 1
    return desencriptado, True

def multiples_textos(funcion_a_usar, texto_a_mostrar: str, texto_input: str):
    """
    (listas, listas anidadas, condicionales, ciclos, funciones)
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
                nuevo_texto, nueva_llave = leer_texto_y_llave(texto_input)
                textos_originales[0].append(nuevo_texto)
                textos_originales[1].append(nueva_llave)
            case 2:
                textos_modificados: list[str] = []
                for i in range(0,len(textos_originales[0]),1):
                    txt_modificado, valido = funcion_a_usar(
                        textos_originales[0][i], textos_originales[1][i]
                    )
                    if not valido:
                        print_and_wait(txt_modificado)
                        break
                    textos_modificados.append(txt_modificado)

                # 'else' solo ejecuta el código si el 'for' terminó de
                # ejecutarse sin usar 'break'
                else:
                    printable_str = ("Texto Original | Texto "
                        + texto_a_mostrar)
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
def suma_verificada(valor1: int, valor2: int):
    """
    (operadores, condicionales)
    Recibe: dos valores enteros a sumar.
    Realiza la suma y verifica que se encuentre dentro de los
    valores Unicode válidos (0x00 a 0x110000).
    Regresa: valor de la suma o -1, dependiendo si el resultado
    es un valor Unicode válido o no.
    """
    UNICODE_MAX_VAL = 0x110000
    suma = valor1 + valor2
    if suma >= UNICODE_MAX_VAL:
        return -1
    else:
        return suma

def resta_verificada(valor1: int, valor2: int):
    """
    (operadores, condicionales)
    Recibe: dos valores enteros a restar.
    Realiza la resta y verifica que se encuentre dentro de los
    valores Unicode válidos (0x00 a 0x110000).
    Regresa: valor de la suma o -1, dependiendo si el resultado
    es un valor Unicode válido o no.
    """
    resta = valor1 - valor2
    if resta < 0:
        return -1
    else:
        return resta

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
    (función de la librería estándar, condicionales)
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
    (funciones)
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

def leer_texto_y_llave(texto_a_mostrar):
    """
    (variables, cadenas)
    No recibe nada.
    Pide al usuario que ingrese un texto y una llave.
    Devuelve: un texto y una llave (ambos son str).
    """
    texto_input_utilizar = "Ingresa el texto a " + texto_a_mostrar + ": "
    texto_input_llave = "Ingresa la llave para " + texto_a_mostrar + ": "

    texto_utilizar = input(texto_input_utilizar)
    llave = input(texto_input_llave)
    return texto_utilizar, llave

def print_and_wait(text: str):
    """
    (funciones)
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
            texto_a_encriptar, llave_input = leer_texto_y_llave("encriptar")
            texto_encriptado, valido = encriptar(texto_a_encriptar,
                                                 llave_input)
            # si la funcion regresa 'valido' como 'False', el mensaje de error
            # está en texto_encriptado
            if not valido:
                print_and_wait(texto_encriptado)
            else:
                print_and_wait("Texto encriptado: " + str(texto_encriptado))
        case 2:
            texto_encriptado, llave_input = leer_texto_y_llave("desencriptar")
            texto_desencriptado, valido = desencriptar(texto_encriptado,
                                                       llave_input)
            # si la funcion regresa 'valido' como 'False', el mensaje de error
            # está en texto_desencriptado
            if not valido:
                print_and_wait(texto_desencriptado)
            else:
                print_and_wait("Texto desencriptado: " + texto_desencriptado)
        case 3:
            multiples_textos(encriptar, "Encriptado", "encriptar")
        case 4:
            multiples_textos(desencriptar, "Desencriptado", "desencriptar")
        case 5:
            sys.exit()
        case _:
            print_and_wait("Opción incorrecta")
