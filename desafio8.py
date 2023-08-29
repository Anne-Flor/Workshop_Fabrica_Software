#8 - crie um programa que receba uma quantidade de canetas pretas e azuis. A caneta azul vale R$2.00,
#a caneta preta vale R$2.50. Mostre a quantidade final a ser paga.
print("Caneta Azul R$2.00")
print("Caneta Preta R$2.50")
numero_canetas_azul   = int(input("Quantas canetas azuis você deseja comprar ? "))
numero_canetas_pretas = int(input("Quantas canetas pretas você deseja comprar ? "))
caneta_azul  = numero_canetas_azul * 2
caneta_preta = numero_canetas_pretas * 2.50
total = caneta_azul + caneta_preta
print(f"O valor total da sua conta é {total}")

print("*********************************************************************************************")

