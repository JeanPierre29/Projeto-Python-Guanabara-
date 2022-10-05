# Faça um programa que leia um numero inteiro e diga se ele é ou não um numero 
# primo

#  ELE SÓ PODE SER DIVISIVEL POR ELE MESMO OU POR 1 
# EX: 13 - sE ANTES DO 13 ELE FOR DIVISIVEL POR ALGUM NÃO É PRIMO 

num =  int(input(" Digite um número: "))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print("\033[30m", end=' ')
        tot += 1
    else:
        print("\033[31m", end=" ")
    print("{}".format(c), end=" ")
print("\n\033[mOnumero {} foi divisivel {} vezes". format(num, tot))
if tot == 2:
    print("E por isso ele É PRIMO!")
else:
    print("É por isso ele NÃO É PRIMO!")
    
    
