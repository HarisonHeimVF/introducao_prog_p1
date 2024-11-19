def escolher_feitico(escolha):
    match escolha:
        case 1:
            return "Fogo"
        case 2:
            return "Água"
        case 3:
            return "Terra"
        case _:
            return "Feitiço desconhecido"

escolha = int(input("Escolha um feitiço (1: Fogo, 2: Água, 3: Terra): "))
feitico = escolher_feitico(escolha)
print(f"Feitiço escolhido: {feitico}")