# Crie um programa que leia números inteiros pelo teclado. O programa só vai 
# parar quando o usuário digitar o valor 999, que é a condição de parada. 
# No final, mostre quantos números foram digitados e qual foi a soma entre elas
# (desconsiderando o flag).

n = 0
qtd = 0 
soma = 0

n = int(input(" Digite um numero [999 para parar]: "))
while n != 999:
    soma += n
    qtd += 1
    n = int(input(' Digite novamente [999 para parar]: '))
print(" Os numeros Digitados foram {} e a soma deles são {}". format(qtd, soma))       
        