# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.
# Ex. Digite um número: 6.127
# O número 6.127 tem a parte inteira 6.

# Importação de uma biblica
from math import trunc

# Ler o valor do usuário
num = float(input('Digite um valor: '))

# Fórmula que remove a parte decimal
parte_inteiro = trunc(num)

print(f'O número {num} tem a parte inteira {parte_inteiro}')