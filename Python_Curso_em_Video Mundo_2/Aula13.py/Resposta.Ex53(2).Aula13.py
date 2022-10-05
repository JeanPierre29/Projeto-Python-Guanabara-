# Faça um programa que leia um numero inteiro e diga se ele é ou não um numero 
# primo

#  ELE SÓ PODE SER DIVISIVEL POR ELE MESMO OU POR 1 
# EX: 13 - sE ANTES DO 13 ELE FOR DIVISIVEL POR ALGUM NÃO É PRIMO 

# JEITO 2 - MAS CURTO 

# join - separa 

# [::-1] - este é para inverter a frase  


frase = str(input('Digite uma frase: ')).strip().upper()
palavra = frase.split()
junto = "".join(palavra)
inverso = junto[::-1]
print(" O inverso de {} é {}". format (junto,inverso))
if inverso == junto:
    print(" Temos um palíndromo!")
else:
    print(" A frase digitada não é um palíndromo!")
    
    
