# Desenvolva um programa que leia as dua notas de um aluno. Calcule e mostre a sua média.

# Nome do usuário
nome = (input('Nome do(a) Aluno(a): '))

# Permite o usuário colocar a primeira nota
nota1 = float(input('Digite a primeira nota: '))

# Permite o usuário colocar a segunda nota
nota2 = float(input('Digite a segunda nota: '))

# O calculo da média
media = (nota1 + nota2) / 2

print (f'A Média de {nome} é entre {nota1} e {nota2} é igual a {media}')