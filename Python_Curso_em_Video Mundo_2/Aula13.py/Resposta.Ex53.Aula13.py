# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, 
# desconsiderando os espaços. Exemplos de palíndromos:

# APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, 
# ANOTARAM A DATA DA MARATONA.

# join - separa 

# [::-1] - este é para inverter a frase 


frase = str(input('Digite uma frase: ')).strip().upper()
palavra = frase.split()
junto = "*".join(palavra)
inverso =""
print(" Você digitou a frase {}". format(junto))
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print(" O inverso de {} é {}". format (junto,inverso))
if inverso == junto:
    print(" Temos um palíndromo!")
else:
    print(" A frase digitada não é um palíndromo!")
