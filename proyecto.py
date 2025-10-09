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

def menu_inicial():
    print("")
    print("1.- Encriptar texto")
    print("2.- Desencriptar texto")
    print("3.- Encriptrar múltiples textos")
    print("4.- Desencriptar múltiples textos")
    print("5.- Salir")

def leer_texto_y_llave():
    texto_a_encriptar = input("Ingresa el texto a encriptar: ")
    llave = input("Ingresa la llave para encriptar: ")
    return texto_a_encriptar, llave

while (True):
    menu_inicial()
    opcion = int(input("Elige una opción: "))
    match(opcion):
        case 1:
            texto_a_encriptar, llave = leer_texto_y_llave()
            texto_encriptado = encriptar(texto_a_encriptar, llave)
            print("Texto encriptado: " + texto_encriptado)
        case 2:
            texto_encriptado = input("Ingresa el texto a desencriptar: ")
            llave = input("Ingresa la llave usada para encriptar: ")
            texto_desencriptado = desencriptar(texto_encriptado, llave)
            print("Texto desencriptado: " + texto_desencriptado)
        case 3:
            textos = [[], []]
            while (True):
                print("")
                print("1.- Agregar texto")
                print("2.- Salir")
                opcion_2 = int(input("Elige una opción: "))
                match(opcion_2):
                    case 1:
                        nuevo_texto, nueva_llave = leer_texto_y_llave()
                        textos[0].append(nuevo_texto)
                        textos[1].append(nueva_llave)
                    case 2:
                        print(textos)
                        textos_encriptados = []
                        for i in range(0,len(textos),1):
                            texto_encriptado = encriptar(textos[0][i-1], textos[1][i-1])
                            textos_encriptados.append(texto_encriptado)
                        print(textos_encriptados)
                        break
                    case _:
                        print("Opción incorrecta")
        case 5:
            exit()
        case _:
            print("Opción incorrecta")
