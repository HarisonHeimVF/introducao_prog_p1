agua_disponivel = float(input('Quantidade de água disponível (litros): '))

distancia = float(input('Distancia até o óasis (km): '))

agua_necessaria = distancia * 2

if agua_disponivel >= agua_necessaria:
    print('quantidade de água é suficiente para chegar ao óasis')

else:
    print('A quantidade de água não é suficiente, será necessário mais água')