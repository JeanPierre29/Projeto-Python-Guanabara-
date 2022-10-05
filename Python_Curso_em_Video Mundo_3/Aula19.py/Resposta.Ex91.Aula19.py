# Crie um programa onde 4 jogadores joguem um dado e tenham resultados 
# aleatórios. Guarde esses resultados em um dicionário em Python. No final, 
# coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior 
# número no dado.

from random import randint
from time import sleep
from operator import itemgetter #  PARA O ITEM 0 ELE POE EM ORDEM DE CHAVE 
jogo = { 'jogador1': randint(1, 6), # ITEM 1 ELE POE EM ORDEM DOS NUMEROS ITEMGETTER
         'jogador2': randint(1, 6),
         'jogador3': randint(1, 6),
         'jogador4': randint(1, 6)}

ranking = list()
print('Valores sorteados: ')

for k , v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)# reverse ele 
# organiza do maior pro menor 

print(ranking)
print('-=' *30)
print(' == RANKING DOS JOGADORES ==')

for i, v in enumerate(ranking):
    print(f'{i+1}° lugar: {v[0]} com {v[1]}')
    sleep(1)
    
    



