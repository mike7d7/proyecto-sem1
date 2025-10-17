# Cifrado de Vigenère

### Contexto

El [Cifrado de Vigenère](https://es.wikipedia.org/wiki/Cifrado_de_Vigen%C3%A8re) es un método de cifrado por sustitución simple polialfabético. Se basa en el mismo método que el [Cifrado César](https://es.wikipedia.org/wiki/Cifrado_C%C3%A9sar), de "desplazar" el alfabeto para sustituir cada letra por otra que se encuentra a un número fijo de posiciones más adelante en el alfabeto. A diferencia del Cifrado César, que utiliza un solo valor como llave, el Cifrado de Vigenère utiliza una llave más larga, lo cual hace que cada letra tenga su propio alfabeto de sustitución.

### Instalación

Descargar el archivo y ejecutar en terminal con:

`python3 proyecto.py`

No usar en Thonny debido a falta de soporte para borrar el output de la consola.

Ingresar el número correspondiente a la opción deseada y seguir las instrucciones del programa.

### Algoritmo

```
EO, cifrar(texto_plano, llave)
  texto_encriptado = ""

  // Utilizar ciclo FOR desde 0 hasta longitud de texto_plano
  Por cada letra en texto_plano
    indice_llave = numero_de_letra % longitud(llave)
    offset = llave[indice_llave]

    // Utilizar valores Unicode
    nueva_letra = texto_plano[numero_de_letra] + offset
    agregar nueva_letra a texto_encriptado

    // incrementar en 1 el numero_de_letra
    // repetir hasta que numero_de_letra sea igual a
    // la longitud de texto_plano
EF, mostrar texto_encriptado
```

```
EO, descifrar(texto_encriptado, llave)
  texto_desencriptado = ""

  // Utilizar ciclo FOR desde 0 hasta longitud de texto_encriptado
  Por cada letra en texto_encriptado
    indice_llave = numero_de_letra % longitud(llave)
    offset = llave[indice_llave]

    // Utilizar valores Unicode
    nueva_letra = texto_encriptado[numero_de_letra] - offset
    agregar nueva_letra a texto_desencriptado

    // incrementar en 1 el numero_de_letra
    // repetir hasta que numero_de_letra sea igual a
    // la longitud de texto_plano
EF, mostrar texto_desencriptado
```

### Función de la librería estándar de Python

Función elegida: `ord()`

La función `ord()` recibe como argumento un caracter, y regresa el número entero que representa al número en el formato Unicode.

Ejemplo:

`ord("π")`
regresa el valor
`960`
el cual podemos verificar que es el valor Unicode de "π" pasando el número a hexadecimal y buscandolo en el [explorador de Unicode](https://www.compart.com/en/unicode/U+03C0).
`960 -> 3C0`

La función es usada para convertir cada caracter de una string, en un valor al cual se le pueda restar y sumar valores.

### Imports

El programa usa dos imports, `os` y `sys`

El primero se utiliza en la función `clear()`, la cual limpia la consola utilizando un comando del sistema.
En esta función se usa el atributo `os.name` para identificar si el sistema operativo utilizado para ejecutar el programa es Windows, si esto es verdadero
se utiliza el comando `cls` para limpiar la consola, en caso de que no sea Windows, se usa el comando `clear`

`sys` es utilizado en Main, en donde es utilizado cuando el usuario ingresa la opción 5, la cual usa la función `sys.exit()` para cerrar el programa.
