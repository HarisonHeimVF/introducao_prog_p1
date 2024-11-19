import random

def lancar_dados(vezes):
    for _ in range(vezes):
        resultado = random.randint(1, 6)
        print(f"Resultado do dado: {resultado}")

vezes = int(input("Quantas vezes deseja lançar o dado? "))
lancar_dados(vezes)