# A confederação Nacional de Natação precisa de um programador que leia o 
# ano de nascimento de um atleta e mostre sua categoria, de acordo com a
# idade:
    
#– Até 9 anos: MIRIM
#– Até 14 anos: INFANTIL
#– Até 19 anos: JÚNIOR
#– Até 25 anos: SÊNIOR
#– Acima de 25 anos: MASTER  

ano = int(input(" Digite o ano de nascimento: "))
idade = (2020 - ano)
print (" Sua idade é {} anos". format(idade))

if idade <= 9:
    print(" sua categoria é MIRIM! ")
elif idade <= 14:
    print(" Sua categoria é INFANTIL! ")
elif idade <= 19:
    print(" Sua categoria é JUNIOR!")
elif idade <= 25:
    print(" Sua categoria é SÊNIOR! ")
else:
    print(" Sua categoria é MASTER! ")
    
