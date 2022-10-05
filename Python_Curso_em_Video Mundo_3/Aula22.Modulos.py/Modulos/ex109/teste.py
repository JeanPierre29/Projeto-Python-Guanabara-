#  Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor
#  retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no
#  desafio 108.

from ex109 import moeda

p = float(input('Digite o preço: R$ '))
print(f'A metade de R${moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de R${moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentar 10%, temos R${moeda.aumentar(p, 10)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(p, 13, True)}')



# \t - Ele alinha 