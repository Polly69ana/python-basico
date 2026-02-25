# Crie um programa que leia quanto dinheiro um pessoa tem na carteira e mostre quantos Doólares ela pode comprar.

# Considere US$ 1,00 = R$ 3,27

#  Ler o número do usuário
real = float(input('Quanto dinheiro você tem na carteira? R$ '))

# Fórmula de conversão
dolar = real / 5.22
euro = real / 5.5
iene = real / 5.7

# Fórmula para deixar com dois números de algarismos
dolar_formatado = f'{dolar:.2f}'
euro_formatado = f'{euro:.2f}'
iene_formatado = f'{iene:.2f}'

print(f'Com R$ {real} na carteira\nVocê pode comprar:\nUS$ {dolar_formatado}\n€ {euro_formatado}\n¥ {iene_formatado}')