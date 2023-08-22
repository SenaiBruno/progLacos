"""
Desenvolver um programa que calcule o fatorial do número 5, ou seja, 5!. Desta forma, temos que 5! = 5 . 4 . 3 .
2 . 1 ou 5! = 1 . 2 . 3 . 4 . 5, equivalente a 120.
"""

cont = 5

n1 = 1

while (cont > 0):
    ant = cont * n1
    contador = cont - 1

    print(n1)