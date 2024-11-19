def calcular_velocidade(distancia, tempo):
    return distancia / tempo

distancia1 = float(input("Distância percorrida pelo dragão 1 (km): "))
tempo1 = float(input("Tempo gasto pelo dragão 1 (horas): "))
distancia2 = float(input("Distância percorrida pelo dragão 2 (km): "))
tempo2 = float(input("Tempo gasto pelo dragão 2 (horas): "))

velocidade1 = calcular_velocidade(distancia1, tempo1)
velocidade2 = calcular_velocidade(distancia2, tempo2)

if velocidade1 > velocidade2:
    print("Dragão 1 é mais rápido.")
elif velocidade2 > velocidade1:
    print("Dragão 2 é mais rápido.")
else:
    print("Ambos os dragões têm a mesma velocidade.")