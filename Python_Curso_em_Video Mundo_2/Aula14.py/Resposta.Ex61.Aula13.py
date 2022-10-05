# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os
# 10 primeiros termos da progressão usando a estrutura while.


''''primeiro = int(input("Primeiro termo: "))
razão = int(input("Razão: "))
decimo = primeiro + (10 - 1) * razão
for c in range(primeiro, decimo + razão, razão):
    print('{}'. format(c), end=' -> ')
print("ACABOU")'''

print(" Gerador de PA")
print("-=" * 10)
primeiro = int(input(" Primeiro termo: "))
razão = int(input(" Razão da PA: "))
termo = primeiro
cont = 1
while cont <= 10:
    print("{} -> ". format(termo), end="")
    termo += razão
    cont += 1
print("FIM")


