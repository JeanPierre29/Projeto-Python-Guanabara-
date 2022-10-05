# Faça um programa que jogue par ou ímpar com o computador. O jogo só será 
# interrompido quando o jogador perder, mostrando o total de vitórias
#  consecutivas que ele conquistou no final do jogo.

# Esse tipo " " -> é porque ele tera somente 2 opções Par ou Impar

from random import randint
v = 0
while True:
    jogador = int(input(" Diga o valor: "))
    computador = randint(0,10)
    total = jogador + computador
    tipo = " "
    while tipo not in "PpIi":
        tipo = str(input("Par ou impar? [P/I] ")).strip().upper()[0]
    print('Você jogou {} e o computador {}. total de {}'. format(jogador, computador, total,),end="")
    print(" Deu Par" if total % 2 == 0 else " Deu impar")
    
    if tipo == "P":
        if total % 2 == 0:
            print("Você Venceu!")
            v += 1
        else:
            print("Você Perdeu!")
            break
    elif tipo == "I":
        if total % 2 == 1:
            print("Você Venceu!")
            v += 1
        else:
            print("Você Perdeu!")
            break
    
    print("Vamos jogar novamente...")
print('GAME OVER! você venceu {} vezes'. format(v))
    