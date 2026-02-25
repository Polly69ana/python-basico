# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo ret^sngulo. Calcule e mostre o comprimento da hipotenusa.

#Importação de uma biblioteca
import math

# Entrada de dados
op = float(input('Qual o cateto oposto: '))
ad = float(input('Qual o cateto adjacente: '))

hi = math.hypot(op, ad)
print(f'A hipotenusa vai medir {hi:.2f}')