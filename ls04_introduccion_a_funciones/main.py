# -*- coding: utf-8 -*-
import re
from utils import system_pause, clear_screen

"""Leccion 03. Introducción a las funciones

Uso de def.
Es uno de los elementos más importantes en python. Toda función que se define con
la palabra reservada def, retorna un valor. Si no se especifica qué retorna
retorna un None, que es un objeto que representa la 'nada'

Funciones lambda
Las funciones lambda o expresiones lambda es una forma más compacta para 
definir funciones. 
La sintaxis para definir una funcion lambra es
lambda arg1, arg2, ..., argn : valor_a_retornar

Notas:
- La firma de una función es un 'identificador' que incluye el nombre de la
función, los parámetros que recibe junto con sus tipos, el valor que retorna.
Esto permite la sobrecarga, explique por qué.

- Explique por qué suma_primeros_n_enteros retorna un float y no un entero.

- Las funciones se dice que son ciudadanos de primera, que básicamente quiere decir que
son objetos, y como todos los objetos podemos usarlas como si fueran variables.

- Una función se puede definir 'al vuelo' es decir se define y en seguida se invoca. Estas
regularmente se denominan funciones anónimas.
"""


def suma_primeros_n_numeros(n: int) -> int:
    """Retorna la suma 1+2+...+n.
    Se especifica el tipo de dato que recibe, y el tipo de dato
    que devuelve.
    """
    total = 0
    for i in range(1, n+1):
        total += i
    return i


def suma_primeros_n_enteros(n):
    """Retorna la suma 1+2+...+n usando formulazo.
    Es más eficiente que la función suma_primeros_n_numeros.
    """
    return n*(n+1)/2


def sin_retorno(message: str) -> None:
    """Imprime el mensaje y no retorna nada."""
    print(f'Mensaje: {message}')

    # esto se retorna en automático si no se especifica.
    return None


def main():
    """Main Function.
    """

    # se invoca primera y segunda función
    print(f'1 + 2 + ... + 11 + 12 = {suma_primeros_n_numeros(12)}')
    print(f'1 + 2 + ... + 14 + 15 = {suma_primeros_n_enteros(15)}')

    # se invoca y mostramos objeto que se retorna
    la_nada = sin_retorno("Saludes a todes :V")
    print(f'La nada representado por: {la_nada}')

    # al ser las funciones ciudadanos de primer clase, podemos almacenar
    # una funcion en una variable
    saludar = lambda msg: print(f'Hola {msg}')
    saludar('Soy el Rorris...')

    # funcion anonima
    (lambda a, b: print(f'La suma de {a}+{b} es {a+b}'))(5, 6)


# run app
if __name__ == '__main__':
    clear_screen()
    main()
    system_pause()
