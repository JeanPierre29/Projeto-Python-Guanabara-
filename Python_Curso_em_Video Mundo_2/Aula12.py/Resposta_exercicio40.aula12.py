# Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagen no final, de acordo com a média atingida:
    
# Média abaixo de 5.0: REPROVADO
# Média entre 5.0 e 6.9: RECUPERAÇÃO
# Média 7.0 ou superior: APROVADO

alu1 = float(input(" digite sua primeira nota: "))
alu2 = float(input(" digite sua segunda nota: "))
media = (alu1 + alu2 ) / 2

if media <= 5.0:
    print(" Infelizmente você está REPROVADO!")
elif media <= 6.9:
    print(" Você está de RECUPERAÇÃO!")
else:
    print(" Parabens você está APROVADO!")
    
print(" Sua média final é {:.1f}". format(media))
    


