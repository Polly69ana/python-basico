# Crie um progarma que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas.
# O nome com todas minúsculas.
# Quantas letras ao todo (sem considerar espaços).
# Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome completo: '))

print(nome)
print(f'Seu nome em maiúscula é {(nome.upper())}')
print(f'Seu nome em minúscula é {(nome.lower())}')
nome_inteiro = len(nome.replace(' ', ''))
print(f'Seu nome tem ao todo {(nome_inteiro)} letras')
print(f'Seu nome primeiro tem {(len(nome.split()[0]))} letras')