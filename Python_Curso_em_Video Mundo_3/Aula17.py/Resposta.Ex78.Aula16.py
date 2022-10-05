# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No
# final, mostre qual foi o maior e o menor valor digitado e as suas 
# respectivas posições na lista.
minhalist = []
for c  in range(0, 5):
    minhalist.append(int(input(f'Digite um valor para a Posição {c}: ')))
    if c == 0:
        mai = men = minhalist[c]
    else:
        if minhalist[c] > mai:
            mai = minhalist[c]
        if minhalist[c] < men:
            men = minhalist[c]

print('=-='*10)
print(f'Você digitou os valores {minhalist}')
print(f'O maior valor digitado foi {mai} nas posições', end='')

for i, v in enumerate(minhalist):
    if v == mai:
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi {men} nas posições', end=' ')
for i, v in enumerate(minhalist):
    if v == men:
        print(f'{i}...', end=' ')
print()




    