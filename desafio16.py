#16 - utilizando estrutura de repeticao while crie um programa que leia exclusivamente o sexo como 'F' e 'M' 
#e o loop so deve terminar quando sexo for = sair. ao fim mostre a quantidade e mulheres e homens.
sexo_masculino = 0 
sexo_feminino  = 0 

while True:
    sexo = (input("""[F] feminino [M] Masculino, ou 'sair' : """)).lower()
    
    if sexo == 'f':
        sexo_feminino  += 1

    if sexo == 'm':
        sexo_masculino += 1
    
    if sexo == 'sair':
        break

    else:
        print("Opção inválida. Digite [F] Feminino [M] Masculino, ou 'sair' ")

print(f'Existem {sexo_masculino} pessoas do sexo masculino')
print(f"Existem {sexo_feminino} pessoas do sexo feminino")