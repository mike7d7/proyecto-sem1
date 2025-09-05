# Cifrado de Vigenère

### Contexto

El [Cifrado de Vigenère](https://es.wikipedia.org/wiki/Cifrado_de_Vigen%C3%A8re) es un método de cifrado por sustitución simple polialfabético. Se basa en el mismo método que el [Cifrado César](https://es.wikipedia.org/wiki/Cifrado_C%C3%A9sar), de "desplazar" el alfabeto para sustituir cada letra por otra que se encuentra a un número fijo de posiciones más adelante en el alfabeto. A diferencia del Cifrado César, que utiliza un solo valor como llave, el Cifrado de Vigenère utiliza una llave más larga, lo cual hace que cada letra tenga su propio alfabeto de sustitución.

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
