# Faça um programa que leia um numero inteiro qualquer e mostre na tela a sua tabuada.

# Ler o número do usuário
n1 = int(input('Digite o número para ver sua tabuada: '))

for i in range(1, 11):
    print(f'{n1} x {i} = {n1 * i}')