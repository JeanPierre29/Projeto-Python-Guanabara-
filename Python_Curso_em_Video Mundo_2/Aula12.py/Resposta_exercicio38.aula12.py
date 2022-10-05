# ESCREVA UM PROGRAMA QUE LEIA 2 NUMEROS INTEIROS E COMPARE - OS, MOSTRANDO NA
# TELA UMA MENSAGEM: 

# Primeiro Valor é maior 
# Segundo Valor é Maior
# Não existe valor maior, os dois são iguais

u1 = int(input(" Digite o primeiro valor: "))
u2 = int(input(" digite o segundo valor: "))

if u1 > u2:
    print(" Primeiro valor é maior!")
elif u1 < u2:
    print(" Segundo valor é o maior")
else:
    print(" Não existe valor maior, os dois valores são iguais!")
