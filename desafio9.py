#crie um programa que leia o nome de tres pessoas: João Maia, João Abrantes e Pedro. Para os respectivos 
#nomes imprima:'oi eu sou joao maia', 'oi eu sou joao abrantes', 'oi eu sou pedro', e caso o nome nao seja 
#nenhum dos tres imprima 'oi meu nome é {nome}'
nome_conhecidos = ['João Maia', 'João Abrantes', 'Pedro']
nomes_informados = []

for indice in range(1, 4):
    nomes_informados.append(input(f'Digite um nome: {indice}'))

for nome in nomes_informados:
    if nome in nome_conhecidos:
        print(f'Oi, eu sou {nome}')
    else:
        print(f"Oi, meu nome e {nome}")
