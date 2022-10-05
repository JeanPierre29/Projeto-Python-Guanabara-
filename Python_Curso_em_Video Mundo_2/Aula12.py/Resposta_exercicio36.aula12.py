# Escreva um programa para aprovar o empréstimo bancário para a compra de uma
# casa. O programa vai perguntar o " VALOR DA CASA " , o " SALÁRIO ",  do com -
# prador e em " QUANTOS ANOS "  ele vai pagar. 

# calcule o valor da prestação mensal, sabendo que ela não pode exceder" 30 % "
# do salário ou então o emprestimo será negado.

casa = float(input(" Digite o valor da Casa: R$ "))
salario = float(input(" Digite seu salário: R$ "))
anos =float(input(" Quantos anos irá pagar ? "))
prestação = casa / (anos * 12)
minimo = salario * 30 / 100
print(" Para pagar a casa de R${:.2f} em {} anos". format(casa, anos))
print(" a prestação será de R${:.2f}". format(prestação))
if prestação <= minimo:
    print(" emprestimo pode ser CONCEDIDO!")
else:
    print(" Emprestimo NEGADO!")
