"""
Elaborar um programa que apresente o valor de uma potência de uma base qualquer (Variável b) elevada a um
expoente qualquer (Variável e), ou seja, de be
. (Sem usar Math.pow();
"""

num = int(input("Escolha um número: "))

cont = 5

while(num <= 10):
    pot = cont * num
    print(f"{pot}")

    num = num + 1

