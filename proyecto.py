def encriptar(texto_a_encriptar, llave):
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

def desencriptar(texto_encriptado, llave):
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

texto_a_encriptar = input("Ingresa el texto a encriptar: ")
llave = input("Ingresa la llave para encriptar: ")
texto_encriptado = encriptar(texto_a_encriptar, llave)
print("Texto encriptado: " + texto_encriptado)

texto_desencriptado = desencriptar(texto_encriptado, llave)
print("Texto desencriptado: " + texto_desencriptado)
