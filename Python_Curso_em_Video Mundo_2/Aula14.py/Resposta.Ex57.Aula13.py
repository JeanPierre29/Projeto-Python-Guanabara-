# Crie um programa que leia varios números inteiros pelo teclado. No final da
# execução, mostre a MEDIA ENTRE TODOS os valores e qual foi a MAIOR e o MENOR
# valor lidos. O programa deve perguntar ao usuário se ele quer ou não 'CONTINUAR'
# a digitar valores.


num = quant = soma = media = maior = menor =0
resp = "S"


while resp in "Ss":
    num = int(input(" Digite um numero: "))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num


