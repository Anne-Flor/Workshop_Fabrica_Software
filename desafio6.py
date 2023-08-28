#6 - crie um programa que leia uma velocidade de um carro e multe se passar com velocidade maior que 80km/h. 
#mostre que ele foi multado. a multa é de 7R$ por cada km acima do limite
print("PROGRAMA DE VERIFICAÇÃO DE MULTA")
velocidade        =  float(input("Digite a velocidade do veículo : "))
velocidade_limite = 80 
exedente          = 0

if velocidade > velocidade_limite:
    exedente = (velocidade - velocidade_limite)
    multa    = exedente * 7 
if exedente > 0:
    print(f"Você foi multado em R${multa} pois ultrapassou {exedente} acima da velocidade permitida {velocidade_limite}km/h")
