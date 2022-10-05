def diminuir(preco=0, taxa=0, formato=False):
     res = preco - (preco * taxa/100)
     return res if formato is False else moeda(res)
     # Não vai ter formato se formato for falso    
    
def dobro(preco=0, formato=False):
    res = preco * 2
    return res if not formato else moeda(res)
    
    
def metade(preco=0, formato=False):
    res = preco / 2
    return res if not formato else moeda(res)

def moeda(preco=0, moeda='R$'):  # Só acrescentamos este 
    return f'{moeda}{preco:>.2f}'.replace('.',',') 

def resumo(preco=0, taxaa=10, taxar=5):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Pre�o analisando: \t{moeda(preco)}')
    print(f'Dobro do pre�o: \t{dobro(preco, True)}')
    print(f'Metade do Pre�o: \t{metade(preco, True)}')
    print(f'{taxaa}% de aumento: \t{aumentar(preco, taxaa, True)}')
    print(f'{taxar}% de redu��o: \t\t{diminuir(preco, taxar, True)} ')
    print('-'*30)

    
    # no interect help que é aqueles ''' debaixo do primeiro def, que fizemos
    # antes, ele ajuda a organizar, porque quando modularizamos codigos, nós
    # nós não precisamos saber oque acontece, mas ele nos ajuda no auxilio , e 
    # se usarmos em outros projetos
    # Ajuda o programados com as docs strings
    
    