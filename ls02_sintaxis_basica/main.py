# -*- coding: utf-8 -*-
from utils import system_pause, clear_screen

"""Lección 02. Sintaxis Basica

1) Definiendo Variables
En python el tipo de variable se infiere de acuerdo al tipo de dato que
se le asigna, es decir es de tipado dinámico.
Basta con declarar la variable y asignarle un valor. Pude realizar asignaciones
multiples en una misma linea de codigo.

2) Condicionales
Básicamente se efectuan con el if, else if (que en python es elif) y else de 
toda la vida.

Notas:
- Existen diferentes formas de extrapolar valores dentro de un string. Investigue
por su cuenta.

- El operador aritmético ** usado de la forma n**m, devuelve n elevado a la potencia
m, donde n es la base y m el exponente.

- La función range es un objeto Sequence que se verá más adelante.

- Se agrega un paquete utils que contiene unicamente dos funciones. Más adelante
se verá el como definir módulos (que son scripts de python) y como agruparlos en paquetes.

- Recordar que en python NO hay llaves, es decir, los bloques de código se separan
de acorde a su identación.
"""

# limpiamos consola
clear_screen()

# variable x que almacena un entero
x = 5
print(f'Entero: {x}')

# asignación multiple y operación aritmética
a, b = 1, 2
print("%d + %d = %d\n"%(a, b, a+b))

# cadena (str)
mi_nombre = 'Rodrigoncio'
print('Mi nombre es {}\n'.format(mi_nombre))

# imprimimos la potencia de 1, 2 y 3 de cada entero entreo 1 y 10.
for x in range(1, 11):
    print('%2d %3d %4d'%(x, x**2, x**3))
print()

# hace lo mismo que el for de arriba
for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
print()

# if, elif, else clásico
if a == 1 and b == 3:
    print('"a" es el número 1 y "b" es número 3.')
elif a==1 and b == 2:
    print('"a" es el número 1 y "b" el número 2.')
else:
    print("zzz...")

# end app
system_pause()