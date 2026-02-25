# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

# Ler o salário
salario = float(input('Qual é o salário do Funcionário? R$'))

# Fórmula para dar aumento do salário
real = salario + (salario * 15 / 100)

print (f'Um funcionário que ganhava R${salario:.2f}, com 15% de aumento, passa a receber R${real:.2f}.')