# Exemplo 

# O programa só para quando digito o 0


n = 1 
par = impar = 0
while n != 0:
    n = int(input(" Digite o valor: "))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(" Você digitou {} numeros pares e {} numeros impar! ". format(par, impar))