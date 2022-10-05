# Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:

# 5! = 5 x 4 x 3 x 2 x 1 = 120

# QUANDO COMEÇAMOS QUALQUER NUMERO COM QUALQUER MULTIPLICAÇÃO DEVEMOS COMEÇAR 
# COM 1 - PORQUE SE COMEÇAR COM '0' ELE SEMPRE ENTENDERÁ QUE SERÁ '0'

'''from math import factorial
num = int(input(" Informe um numero para calcular seu fatorial: "))
f = factorial(num)
print(" O factorial de {} é {}.". format(num, f))'''


num = int(input("Numero para calcular seu fatorial: "))
c = num
f = 1
print(" Calculando {}!\n\n". format(num), end=' ')
while c > 0:
    print("{}". format(c), end= ' ')
    print(" x " if c > 1 else " = ", end=" ")
    f *= c
    c-= 1
print("{}". format(f))

