#  Faça um programa que mostre a tabuada de vários números, um de cada vez, 
# para cada valor digitado pelo usuário. O programa será interrompido quando 
# o número solicitado for negativo.

while True:
    n = int(input(" Quer ver a taboada de qual valor? "))
    print("-" *30)
    if n < 0:
        break
    for c in range(1, 11):
        print(" {} x {} = {}". format(n, c, n*c) )
    print("-" *30)
print(" PROGRAMA DE TABUADA ENCERRADO! VOLTE SEMPRE!")
    
    


