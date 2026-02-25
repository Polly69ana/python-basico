# Desenvolva um programa que leia o comprimento de três retas e dig ao usuário

print('-='*20)
print('Analisador de Triângulos')
print('-='*20)

# Entrada dos Lados
r1 = float(input('Digite o primeiro valor: '))
r2 = float(input('Digite o segundo valor: '))
r3 = float(input('Digite o terceiro valor: '))

# Verificação da condição de exixtência
if (r1 + r2 > r3) and (r1 + r3 > r2) and (r2 + r3 > r1):
    print('É possível formar um triângulo.')
    # Classificação opcional
    if r1 == r2 == r3:
        print('Tipo: Equilátero')
    elif r1 != r2 and r2 != r3 and r1 != r3:
        print('Tipo: Escaleno')
    else:
        print('Tipo: Isósceles')
else:
    print('Não é possível formar um triângulo.')