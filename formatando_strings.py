nome = 'Edmar'
peso = 65
altura = 1.80
imc = peso / (altura * altura)

#IMC = peso / altura * altura

# f-strings (formatação de strings)
linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'pesa {peso} quilos, e seu IMC é {imc:.2f}'
print(linha_1)
print(linha_2)