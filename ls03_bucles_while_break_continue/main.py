# -*- coding: utf-8 -*-
from utils import system_pause, clear_screen

"""Lección 03. Bucles

En python basicamente existe el for (que se emplea comúnmente con el objeto range) y
el bucle while.

El while recibe una condición que retorna un booleano (True o False) como en todos
los demás lenguajes. Este se ejecuta mientras la condición se siga cumpliendo.

Dentro de un bucle podemos usar el break y continue de 'toda la vida'. El break
rompe el bucle mientras que el continue termina la iteración y pasa a la siguiente

Notas:
- En este ejemplo y de aquí en adelante se define una función principal nada más por que
estoy acostrumbrado a java :v  en donde hay una clase principal con su respectivo método
main.
"""


def main():
    """Main Function.
    """

    # bucle for
    for i in range(10):
        print(f'Hola Mundo No. {i+1}')
    print()

    # bucle while, muestra el primer multiplo de 7 que sea par y que sea mayor que 50
    i = 1
    while i <= 100:
        if i % 7 == 0 and i % 2 == 0 and i > 50:
            break
        i = i+1
    print(f'El número {i} es par, múltiplo de 7 y mayor que 50')
    print()


# run app
if __name__ == '__main__':
    clear_screen()
    main()
    system_pause()
