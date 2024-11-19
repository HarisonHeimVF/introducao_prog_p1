def calculadora_media():
    total_notas = 0
    Contador_notas = 0

    while True:
        nota = float(input('Digite uma nota (ou -1 para encerrar): '))

        if nota == -1:
            break

        if 0 <= nota <= 10:
            total_notas += nota
            Contador_notas += 1
        else:
            print('Nota inválida! Por favor, insira uma nota entre 0 e 1.')

    if Contador_notas > 0:
        media = total_notas / Contador_notas
        print(f'A média das notas é {media:.2f}')
    else:
        print('Nenhuma nota válida foi inserida')

if __name__ == '__main__':
    calculadora_media()