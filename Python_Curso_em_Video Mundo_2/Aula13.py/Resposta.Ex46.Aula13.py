# Faça um programa que mostre na tela uma contagem regressiva para o estouro de 
# fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.


from time import sleep 

e = int(input(" Digite quanto tempo falta : "))

for c in range (e, -1, -1):
    print(c)
    c = sleep (1)
print("BUM")
c = sleep (1)
print('Feliz')
c = sleep (1)
print('Ano')
c = sleep (1)
print("novo!!!")
