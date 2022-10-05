# Crie um programa que tenha uma tupla única com nomes de produtos e seus
# respectivos preços, na sequência. No final, mostre uma listagem de preços,
# organizando os dados em forma tabular.

listagem = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 25,
            'Livros', 34.90)
print('-' *40)
print(f'{"LISTAGEM DE PREÇO":^40}')
print('-' *40)
for lis in range(0, len(listagem)): # Ele pega do inicio até o fim
    if lis % 2 == 0:     #->        # Par é as str da esquerda
        print(f'{listagem[lis]:.<30}', end='')#:.<30 é os (.)
    else:
        print(f'R${listagem[lis]:>7.2f}')
print('-' *40)

# 