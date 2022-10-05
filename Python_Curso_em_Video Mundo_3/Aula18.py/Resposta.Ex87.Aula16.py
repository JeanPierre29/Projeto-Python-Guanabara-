# Aprimore o desafio anterior, mostrando no final:      
# A) A soma de todos os valores pares digitados.     
# B) A soma dos valores da terceira coluna.  
# C) O maior valor da segunda linha.

matriz = [[0, 0, 0,],[0,0,0,],[0,0,0,]]
spar = mai = scol = 0             # Acresentou este 
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l},{c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:        # Acressento este
            spar += matriz[l][c]         # Acressento este
    print()
print('-=' * 30)
print(f'A soma dos valores pares é {spar}') # Acressento este  

for l in range(0, 3):           # Acressento este em 2° vez 
    scol += matriz[l][2]        # Acressento este em 2° vez 
print(f'A soma dos valores da terceira coluna e {scol}')  # Acressento este em 2° vez 
    
for c in range(0,3):             # Acressento este em 3° vez 
     if c == 0:                  # Acressento este em 3° vez 
         mai = matriz[1] [c]     # Acressento este em 3° vez 
     elif matriz [1] [c] > mai:  # Acressento este em 3° vez 
        mai = matriz [1] [c]     # Acressento este em 3° vez 
print(f'O maior valor da segunda linha é {mai}.')  # Acressento este em 3° vez 
