
def aumentar(preco=0, taxa=0, formato=False):   
    '''
    

    Parameters
    ----------
    preço : TYPE
        DESCRIPTION.
    taxa : TYPE
        DESCRIPTION.
    formato : TYPE, optional
        DESCRIPTION. The default is False.

    Returns
    -------
    TYPE
        DESCRIPTION.

    '''
    res = preco + (preco * taxa/100)  
    return res if formato is False else moeda(res) 


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

def moeda(preco=0, moeda = 'R$'):  # Só acrescentamos este 
    return f'{moeda}{preco:>8.2f}'.replace('.',',') 


  






  
    # no interect help que é aqueles ''' debaixo do primeiro def, que fizemos
    # antes, ele ajuda a organizar, porque quando modularizamos codigos, nós
    # nós não precisamos saber oque acontece, mas ele nos ajuda no auxilio , e 
    # se usarmos em outros projetos
    # Ajuda o programados com as docs strings
    
    