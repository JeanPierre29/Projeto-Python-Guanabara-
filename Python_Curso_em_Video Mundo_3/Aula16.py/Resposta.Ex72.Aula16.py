# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem 
# por extenso, de zero até vinte. Seu programa deverá ler um número pelo 
# teclado (entre 0 e 20) e mostrá-lo por extenso.



cont = ( 'zero', "um", "dois", "três",
        "quatro", "cinco", "seis", "sete","oito",
        "nove", "dez","onze", "doze", "treze", "quatorze", 
        "quinze", "dezesseis", "dezessete", "dezoito",
        "deznove", "vinte")

while True:
    num = int(input(" Digite um numero de 0 a 20: "))
    if 0 <= num <= 20:
        break
        print(' Tente Novamente.', end=' ')
        
    while num != "21":
        resp = str(input('Quer continuar? [s/n] ')).upper().strip()[0]
        resp = ' '
        if resp == 'Nn':
            break
        
print(f"Você digitou o numero {num}")

# DESAFIO FAZER ESSE PROGRAMA CONTINUAR RODANDO 