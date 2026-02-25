# Faça um programa que leia um número de 0 a 9999 que mostre na tela cada um dos dígitos separados.
from encodings.uu_codec import uu_decode

# Lê o número do teclado
num = int(input('Digite um número (0-9999): '))
# Separa os dígitos usando operações matemáticas
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

# Exibe os resultados
print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhares: {m}')