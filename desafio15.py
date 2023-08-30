#15 - utilizando estrutura de repeticao while crie um programa que faça a soma de todos os numeros digitados. 
#o loop so devera parar quando for digitado 0
soma = 0 

while True:
    numero = float(input('Digite um número que deseja somar [0]SAIR : '))
    
    if numero == 0:
        break
    
    soma += numero
print(f"A soma dos números digitados é {soma}")