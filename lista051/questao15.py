"""
Desenvolver um programa que apresente a série de Fibonacci até o décimo quinto termo. A série de Fibonacci é
formada pela sequência 1,1,2,3,5,8,13,21,34, ... etc. Ela se caracteriza pela soma de um termo posterior com seu
anterior subsequente
"""

n1 = 0
n2 = 1
rept = 1

print(n2)

while rept < 15:
    n3 = n1 + n2
    print(n3)
    n1 = n2
    n2 = n3
    rept = rept + 1