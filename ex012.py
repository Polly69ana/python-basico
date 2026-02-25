# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

# Ler o valor do produto
preco = float(input('Qual é o preço do produto? R$ '))

# Formula para dar desconto ao produto
novo = preco - (preco * 5 / 100)

print (f'O produto que custava R${preco}, na promoção com desconto de 5% vai custar R${novo:.2f}')