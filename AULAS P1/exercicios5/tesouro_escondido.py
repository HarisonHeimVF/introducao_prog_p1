def calcular_distancia(x, y):
    return x + y

x = int(input("Número de passos para o norte (X): "))
y = int(input("Número de passos para o leste (Y): "))
distancia = calcular_distancia(x, y)
print(f"Distância total a percorrer: {distancia} passos")