# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma 
# semelhante ‘a função input() do Python, só que fazendo a validação para 
# aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)

def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um numero inteiro válido.\033[m')
        if ok:
            break
    return valor
            
# Programa Principal
n = leiaint('Digite um numero: ')
print(f'Você acabou de digitar o numero {n}')



# O leiaint fez toda a diferença para ficar curto. o def faz função para ficar
# curto o programa