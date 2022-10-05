# Achar o Santos dentro da tupla


times = ("Corinthias", "São Paulo", "Palmeiras", "Santos", "Chapecoense")
print('##########################################################')
print(f'O São Paulo está na {times.index("São Paulo")+1}° Posição')


# Mostrar os 3 primeiros times
print('##########################################################')
print(f'Os 3 primeiros times são {times[0:3]}')



# Mostrar os ultimos 2 
print('##########################################################')
print(f'Os ultimos 2 são {times[-2:]}')



# Colocar em ordem alfabetica
print('##########################################################')
print(f'Lista Organizado {sorted(times)}')