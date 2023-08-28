#7 - crie um programa que leia tres numeros e mostre qual deles e o maior e o menor

n1 = int(input("Digite um número : "))
n2 = int(input("Digite um número : "))
n3 = int(input("Digite um número : "))

if n1 > n2 and n1 > n3: 
    print(f"O maior número entre {n1}, {n2}, e {n3} é {n1}")
    if n2 < n3:
        print(f"O menor número entre {n1}, {n2}, e {n3} é {n2}")
    else:
        print(f"O menor número entre {n1}, {n2}, {n3} é {n3}")
elif n2 > n1 and n2 > n3:
    print(f"O maior número entre {n1}, {n2}, e {n3} é {n2}")
    if n1 < n3:
        print(f"O menor entre {n1}, {n2}, e {n3} é {n1}")
    else:
        print(f"O menor número entre {n1}, {n2}, e {n3} é {n3}")
else: 
    print(f"O maior número entre {n1}, {n2}, e {n3} é {n3}")

