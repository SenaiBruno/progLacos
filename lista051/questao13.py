"""
Desenvolver um programa que imprima a tabuada de 3 a 6.
"""

n1 = 3
cont = 1

while cont <= 10:
    print(f"{n1} * {cont} = {n1 * cont}")
    cont = cont + 1
    if( cont == 11 and n1 < 6):
        cont = 1
        n1 = n1 + 1