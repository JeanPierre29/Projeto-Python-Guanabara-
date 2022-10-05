# Melhore o jogo do "DESAFIO 028" onde o computador vai "Pensar" em um número 
# entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, 
# mostrando no final quantos palpites foram necessários para vencer.

from random import randint
from time import sleep

computador = randint(0,10)  # Faz o computador "PENSAR"
print(" \nVou pensar em um número entre 0 e 10. tente adivinhar...")
print(" Sera que você consegue acertar qual foi ?")

acertou = False
palpites = 0
while not acertou:
    jogador = int(input(" Em que número eu pensei? ")) # Jogador tenta advinhar
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print("Mais ... tente mais uma vez.")
        elif jogador > computador:
            print(" Menos... tente mais uma vez.")

sleep(2)   
print(" Processando...")
print("ACERTOU com {} tentativas PARABENS!". format(palpites))

if jogador == computador:
    print(" Parabens! Você conseguiu me vencer!")
else:
    print(" Ganhei! Eu pensei no numero {} e não no {}!". format(computador, jogador))


