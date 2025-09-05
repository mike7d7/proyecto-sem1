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

texto_a_encriptar = input("Ingresa el texto a encriptar: ")
llave = input("Ingresa la llave para encriptar: ")
texto_encriptado = encriptar(texto_a_encriptar, llave)
print("Texto encriptado: " + texto_encriptado)
