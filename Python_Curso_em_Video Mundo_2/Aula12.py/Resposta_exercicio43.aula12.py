# desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu 
# Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela 
# abaixo 

#– IMC abaixo de 18,5: Abaixo do Peso

#– Entre 18,5 e 25: Peso Ideal

#– 25 até 30: Sobrepeso

#– 30 até 40: Obesidade

#– Acima de 40: Obesidade Mórbida

# IMC = 80 kg ÷ (1,80 m × 1,80 m) = 24,69 kg/m2 (Peso ideal)
# IMC = Peso ÷ (Altura × Altura)

p = float(input(" Digite o seu peso: (kg) "))
a = float(input(" Digite o seu altura: (m) "))
c =  p / (a ** 2)
print(" Seu IMC é {:.1f}". format(c))
if c < 18.5:
    print(" Abaixo do Peso ")
elif 18.5 < c < 25:
    print("Peso ideal! Parabéns")
elif 25 <= c < 30:
    print(" Sobrepeso")
elif 31 <= c < 40:
    print(" Obesidade")
else:
    print(" Obesidade Mórbida")



