def numeros_com_resto_5():
    for numero in range(1000, 2001, 1):  # Percorre os números de 1000 a 2000 (incluindo 2000)
        if numero % 11 == 5:
            print(f'A quantidade é {numero}')

# Chamada da função

print('-----Iniciado o programa-----')

numeros_com_resto_5()

print('-----Encerrando o programa-----')