# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que 
# tipo de triângulo será formado:

#– EQUILÁTERO: todos os lados iguais

#– ISÓSCELES: dois lados iguais, um diferente

#– ESCALENO: todos os lados diferentes

r1 = float(input(" Digite o comprimeito da reta 1: "))
r2 = float(input(" Digite o comprimento da reta 2: "))
r3 = float(input(" Digite o comprimento da reta 3: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print(" Podem formar um triangulo! ", end='')
    if r1 == r2 == r3:
        print("Equilatero!")
    elif r1 != r2 != r3 != r1:
        print("Escaleno!")
    else:
        print(" Isoceles!")
else:
    print(" Os componentes acima não podem formar triângulo! ")