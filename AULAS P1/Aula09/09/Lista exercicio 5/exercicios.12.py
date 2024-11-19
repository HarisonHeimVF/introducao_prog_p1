from random import randint

espada_atq = randint(20, 120)
espada_dur = randint(20, 120)
arco_atq = randint(20, 120)
arco_dur = randint(20, 120)
lança_atq = randint(20, 120)
lança_dur = randint(20, 120)

print(f'Espada: Ataque = {espada_atq}, Dureza = {espada_dur}')
print(f'Arco Ataque = {arco_atq}, Dureza = {arco_dur}')
print(f'Lança Ataque = {lança_atq}, Dureza = {lança_dur}')


if espada_atq > 50 and espada_dur > 70:
    print('Escolha a Espada')
elif arco_atq > 50 and arco_dur > 70:
    print('Escolha o Arco')
elif lança_atq > 50 and lança_dur > 70:
    print('Escolha a Lança')
else:
    print('Escolha outra Arma')
