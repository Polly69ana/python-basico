# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis sobre ele.
"""Quem tiver assistindo em 2019 depois da versão 3.7 do python não precisa mais usar .format (),
apenas coloque um f antes das aspas " " e escreva o nome da variavel dentro dos colchetes {}
exemplo: print (f'A soma de {n1} e {n2} é {s}')"""

a = input('Digite algo: ')
print (f'É maiuscula? {a.isupper()}')
print (f'Só tem espaços? {a.isspace()}')
print (f'É numérico? {a.isnumeric()}')
print (f'É alfabeto? {a.isalnum()}')
print (f'É alfanumerico? {a.isalpha()}')
print (f'É ASCII? {a.isascii()}')
print (f'É decimal? {a.isdecimal()}')
print (f'É dígito? {a.isdigit()}')
print (f'É um identificador? {a.isidentifier()}')
print (f'É minusculo? {a.islower()}')
print (f'É imprimir? {a.isprintable()}')
print (f'Esta captalizada? {a.istitle()}')