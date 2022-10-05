# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi
# o maior e o menor peso lidos.

pesomaior =0
pesomenor =0

for p in range(1, 6):
    peso = float(input("Peso da {}° Pessoa: ". format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior: 
            maior = peso
        if peso < menor:
            menor = peso
print("\n O mais pesado é {}\n e o mais leve é {}". format(maior, menor))
        
    

