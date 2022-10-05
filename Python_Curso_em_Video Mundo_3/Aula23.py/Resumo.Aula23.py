try: 
    a = int(input('Numerador: '))
    b = int(input('Dominador: '))
    r = a / b 

except (ValueError, TypeError):
    print('Infelizmente tivemos um problema') 

except ZeroDivisionError:
    print('Não é possivel dividir um numero por zero!')

except KeyboardInterrupt:
    print('O usuario preferiu não informar os dados!')

except NameError:
    print(' Favor digitar somente numeros aqui!')

else:
    print(f'O resultado é {r:.1f}')

finally:
    print('Volte sempre! Muito Obrigado!')

