from random import randint
from time import sleep

valor_dado = -1
n_lancamento = 0

n = int(input('Digite quantos lançamentos o dado fará: '))

for i in range(n):
    
    vlr_lancamento = randint(1, 6)

    if vlr_lancamento > valor_dado:
        n_lancamento = vlr_lancamento
        n_lancamento = i + 1
    
    print(f'NL = {i+1} e Vlr = {vlr_lancamento}')
    sleep(1)

print('======= O maior lançamento ========')
print(f'Maior => {valor_dado} e o lançamento n{n_lancamento}')