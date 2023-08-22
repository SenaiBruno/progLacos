"""
Desenvolver um programa que peça ao usuário para digitar diversos números reais, e ao final, exibir o maior e o
menor número que foram digitados, além da média entre TODOS os números digitados pelo usuário. A inserção
de números deve parar quando o usuário digitar o número -1, e este número -1 não deve ser considerado nem
como maior, nem como menor, e nem na contagem da média.
"""

n1 = int(input("Escolha o seu número: "))
n2 = 0

if ( n1 != -1 ):
    aux = n1
    maior = n1
    menor = n1

while ( n1 != -1 ):
    n1 = int(input("Informe um número qualquer: "))

    if( n1 != -1):
        aux = aux + n1

    if( n1 != -1):
        n2 = n2 + 1

    if( maior < n1 and n1 != -1):
        maior = n1

    if(menor > n1 and n1 != -1):
        menor = n1

print(f"O maior número é o {maior} e o menor é o {menor}, a média entre eles é de { aux / n2 }")
