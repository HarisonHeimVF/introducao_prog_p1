clubes = []
for i in range(5):
    clube = input(f'Digite o nome do clube {i + 1}: ')
    clubes.append(clube)

novo_clube = input('Digite o nome de um clube pra buscar: ')
if novo_clube in clubes:
    print('Achei seu time.')
else:
    print('Seu time não está entre os melhores.')