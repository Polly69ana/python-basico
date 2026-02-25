# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

# Importação de biblioteca
from math import tan, sin, cos, radians

# Ler angulo do usuário
an = float(input('Digite o ângulo que você deseja: '))

seno = sin(radians(an))
cosseno = cos(radians(an))
tangente = tan(radians(an))


print(f'O ângulo de {an} tem o SENO de {seno:.2f}')
print(f'O ângulo de {an} tem o COSSENO de {cosseno:.2f}')
print(f'O ângulo de {an} tem a TANGENTE de {tangente:.2f}')