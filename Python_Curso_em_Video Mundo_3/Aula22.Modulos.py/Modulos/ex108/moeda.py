# ex108 Adapte o código do desafio #107, criando uma função adicional chamada moeda() 
# que consiga mostrar os números como um valor monetário formatado.
 

def aumentar(preço, taxa):
    res = preço + (preço * taxa/100)
    return res


def diminuir(preço, taxa):
     res = preço - (preço * taxa/100)
     return res
    
    
def dobro(preço):
    res = preço * 2
    return res
    
    
def metade(preço):
    res = preço / 2
    return res 

def moeda(preço = 0, moeda = 'R$'):  # Só acrescentamos este 
    return f'{moeda}{preço:>8.2f}'.replace('.',',') 

    
    

