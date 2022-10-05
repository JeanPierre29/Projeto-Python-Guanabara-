def leiaDineiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',','.').strip() # Liberar virgula
        if entrada.isapha() or entrada == '':
            print(f'Erro: \"{entrada}\" é um preco invalido!')
        else:
            valido = True
            return float(entrada)
        
        