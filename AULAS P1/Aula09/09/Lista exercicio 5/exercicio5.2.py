ferro = float(input('Digite a quantidade de ferro em Kg: '))
ouro = float(input('Digite a quantidade de ouro em Kg: '))

total = ferro + ouro
porcentagem_ferro = (ferro / total) * 100 if total > 0 else 0

print('A liga é suficiente.' if porcentagem_ferro >= 70 else "A liga não é suficiente.")