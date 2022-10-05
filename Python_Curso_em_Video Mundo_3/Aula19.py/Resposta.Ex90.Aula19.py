# Faça um programa que leia nome e média de um aluno, guardando também a 
# situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

aluno = dict()
aluno ['nome'] = str(input('Nome: ')) # recebe a str que vem do teclado
aluno ['media'] = float(input(f'Média de {aluno["nome"]}: ')) # vem do teclado

if aluno['media'] >= 7:
    aluno['situação'] = 'Aprovado'

elif 5 <= aluno ['media']< 7:
    aluno['Situção'] = 'Reprovado'

else:
    aluno['situação'] = 'Reprovado'
print('-=' * 30)

for k, v in aluno.items():
    print(f'-{k} é igual a {v}')
    
#print(aluno)  
# k = keys , v = values(valor)

# values para o valor
# keys para a chave 
# items para o conjunto chave e valor 