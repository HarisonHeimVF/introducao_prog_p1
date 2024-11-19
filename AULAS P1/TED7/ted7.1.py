# Calculadora de Média de Notas:

def calcular_media():
    notas = []
    while True:
        try:
            nota = float(input('Insira a nota (ou -1 para encerrar): '))
            if nota == -1:
                break
            elif 0 <= nota <= 10:
                nota.append(nota)
            else:
                print('Insira uma nota válida (entre a e 10).')
        except ValueError:
            print('Entrada inválida. Tente novamente.')

    if notas:
        media = sum(notas) / len(notas)
        print(f'A média das notas é: {media:.2f}')
    else:
        print('Nenhuma nota foi inserida.')

if __name__ == '__main__':
    calcular_media()
