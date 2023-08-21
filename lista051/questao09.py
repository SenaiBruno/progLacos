"""
Elaborar um programa que apresente no final a soma dos valores pares existentes na faixa de 0 até 500. Utilize
um laço que efetue a variação de 2 em 2.
"""

cont = 0

while(cont <= 500):
    par = cont % 2

    if(par == 0 ):
        print(f"Esses números são pares: {cont}")

    cont = cont + 2