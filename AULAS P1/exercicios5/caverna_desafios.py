def escolher_porta(porta):
    match porta:
        case 1:
            return "Desafio do Labirinto"
        case 2:
            return "Desafio do Dragão"
        case 3:
            return "Desafio da Sombra"
        case 4:
            return "Desafio do Gelo"
        case 5:
            return "Desafio da Terra"
        case _:
            return "Porta inválida"


porta = int(input("Escolha uma porta (1 a 5): "))
desafio = escolher_porta(porta)
print(f"Você enfrentará: {desafio}")
