#13 - utilize estrutura de repeticao for para fazer a tabuada de adição de 0 a 10 de um numero digitado no 
#terminal.
numero = int(input("Digite um número para verificar a tabuada de soma"))
for i in range(11):
    resultado = numero + i
    print(f"{numero} + {i} = {resultado}")
