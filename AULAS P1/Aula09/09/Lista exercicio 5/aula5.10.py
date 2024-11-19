def escolher_desafio(porta):
    match porta:
        case 1:
            print('Desafio: Enfrentar um dragão de fogo')
        case 2:
            print('Desafio: Resolver o enigma mágico')
        case 3:
              print('Desafio: Atravessar um rio cheio de monstros.')
        case 4:
            print('Desafio: Encontrar o tesouro perdido.')
        case 4:
            print('Desafio: Lutar contra um exército de esqueletos.')

porta = input('Escolha uma porta (1 a 5):')

if porta.isdigit() and 1 <= int(porta) <= 5:
    desafio = escolher_desafio(int(porta))
else:
    print("Por favor, insira um número válido (1 a 5).")