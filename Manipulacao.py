'''
C u r s o   e m   V  i  d  e  o    P  y  t  h  o  n
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
'''
frase = ('Curso em Vídeo Python')

# Fatiamento - Ele irá conseguir identificar dentro da cadeia de caracteres a letra na 10 posição, já como a contagem começa com 0
frase[9]

# Fatiamento - Ele ira pegar as letras que estão do 9 posto ao 12 posto. Ele sempre termina em um antes da marcação final.
frase[9:13]

# Fatiamento - Nessa operação ele ira dar as letras do 9 até a letra 21porem como tem o numero 2 no final ira estar pulando de 2 em 2.
frase[9:21:2]

# Fatiamento - Ira até a letra ou caracter de numeto 5 na frase
frase [:5]

# Fatiamento - Ira da letra ou caracter 15 até o final da frase
frase [15:]

# Fatiamento - Ira mostrar do caracter 9 até o final da frase. Porém ira mostrar somente de 3 em 3.
frase[9::3]

# Análise - Saber algumas informaçãoe sobre o string

# Análise - Qual o comprimento da frase
len(frase)

# Análise - Ele pede para o programa contar quantas vezes aparece a letra 'o' na frase.
frase.count('o')

# Análise - Ira fazer uma contagem mais fatiamento. Ira fazer a contagem de quantos 'o' tem do 0 até o caracter 13
frase.count('o', 0, 13)

# Análise - Ira informar quantas vezes tem e onde está a posição 'deo' em que começou que aparecer o caracteres 'deo' na frase.
frase.find('deo')

# Análise - Ira receber o valor -1. Pois é uma string que não existe.
frase.find('Android')

# Análise - Ira perguntar se existe a palavra. E retornar True se tiver e False se não tiver o string na frase.
'Curso' in frase

# Transformação - Ele ira procurar a string na frase e ira substituir essa string pela a que está ao lado no código. Python para Android
frase.replace('´Python', 'Android')

# Transformação - Colocará a frase inteira em maiúscula
frase.upper()

# Transformação - Colocará a frase inteira em minúsculo
frase.lower()

# Transformação - Ira colocar todas a string em minúscula e somente as primeira em maiúscula
frase.capitalize()

# Transformação - Ira fazer uma análise mais detalhada atraves dos espaços. Colocando uma letra maiuscula em cada vez vez que for o termino de um espaço.
frase.title()

# Transformação - Tira os espaços inuteis no inicio e no final da string.
frase.strip()

# Transformação - Ira remover somente os ultimos espaços da string.
frase.rstrip()

# Transformação - Ira remover somente os primeiro espaços da string
frase.lstrip()

# Divisão - Ele ira fazer uma divisão nos espaços reiniciando a contagem apos cada espaço. Ele ira dividir uma string em uma lista onde cada elemento que será sei stripador.
frase.split()

# Junção - Ele ira juntar todos os elementos de frase e ira usar na separação o acento indicado a ser usar
'-'.join(frase)

''' 
Como ficaria em Portugues a logica da Condições .
se carro.esquerda()
    bloco_V_
senão
    bloco_F_
'''

'''
Como é usado em programação a condição .
if carro.esquerdo():
    bloco True
else:
    bloco False
'''

'''
Condição simplificada (ruim)
tempo = int(input('Quantos anos tem seu carro? '))
print('carro novo' if tempo <=3 else'carro velho')
print('--FIM--')
'''