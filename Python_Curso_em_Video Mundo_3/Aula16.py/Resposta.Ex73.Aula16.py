#  Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do 
# Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

#a) Os 5 primeiros times.
#b) Os últimos 4 colocados.
#c) Times em ordem alfabética.
#d) Em que posição está o time da Chapecoense.

times = ("Corinthians", "Palmeiras", "Santos", "Gremio",
         "Cruzeiro", "Flamengo", "Vasco", "Chapecoense", "Atletico-PR",
         "Bahia", "São Paulo", "Fluminense", "Sport-Recife", 
         'EC Vitória', "Curitiba", "Avaí", "Ponte Preta", 'Atletico - GO')
print("-=" * 15)
print(f'Lista de times {times}')
print("-=" * 15)
print(f'Os 5 primeiros times são {times[0:5]}')
print("-=" * 15)
print(f"Os 4 ultimos são {times[-4:]}")
print("-=" * 15)
print(f'Times em ordem alfabetica: {sorted(times)}')
print('-=' *15)
print(f'O chapecoense está na {times.index("Chapecoense")+1}° posição')



