"""
Desenvolver um programa que apresente os quadrados dos números inteiros de 15 a 200
"""
import math

contador = 15
while(contador <= 200):
    print(f"contador: {contador} elevado à 2 = {math.pow(contador,2):.0f}")
    print(math.pow(contador, 2))
    contador = contador + 1



