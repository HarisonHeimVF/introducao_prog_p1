def escolher_feitico(escolha):
    match escolha:
        case 1:
            return "Feitiço de Fogo"
        case 2:
            return "Feitiço de Água"
        case 3:
            return "Feitiço de Terra"
        

# Solicitar a escolha do feitiço ao usuário
try:
    escolha = int(input("Escolha um feitiço (1 para Fogo, 2 para Água, 3 para Terra): "))
    feitico = escolher_feitico(escolha)
    print(f"Você escolheu: {feitico}")
except ValueError:
    print("Por favor, insira um número válido (1, 2 ou 3).")