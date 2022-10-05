# Refaça o DESAFIO 9 , mostrando a tabuada de um número que o usuario escolher,
# só que agora utilizando um laço for.


num = int(input(" Digite um numero para ver sua tabuada: "))

for c in range(1, 11):
    print('{} x {} = {}'. format(num, c, num*c))