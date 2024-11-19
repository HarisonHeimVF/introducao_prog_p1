distancia_dragao_1 = float(input("Digite a distância do primeiro dragão (em metros): "))
tempo_dragao_1 = float(input("Digite o tempo do primeiro dragão (em segundos): "))

distancia_dragao_2 = float(input("Digite a distância do segundo dragão (em metros): "))
tempo_dragao_2 = float(input("Digite o tempo do segundo dragão (em segundos): "))

# Calcula a velocidade de cada dragão
velocidade1 = distancia_dragao_1 / tempo_dragao_1 if tempo_dragao_1 > 0 else 0
velocidade2 = distancia_dragao_2 / tempo_dragao_2 if tempo_dragao_2 > 0 else 0


if velocidade1 > velocidade2:
    print("O primeiro dragão é mais rápido.")
elif velocidade2 > velocidade1:
    print("O segundo dragão é mais rápido.")
else:
    print("Ambos os dragões têm a mesma velocidade.")