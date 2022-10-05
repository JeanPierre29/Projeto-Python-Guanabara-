#Criar uma soma de 1 a 300 , a soma do ultimo com a proxima 

tabuada = 1

while tabuada <= 10:
     numero = 1
     while numero <= 10:
          print(f'{tabuada} x {numero} = {tabuada * numero}')
          numero = numero + 1 
     print("++++++++++++++++++++++++++++++++")
     tabuada = tabuada + 1

