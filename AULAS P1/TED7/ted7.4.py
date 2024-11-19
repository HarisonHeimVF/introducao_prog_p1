import random

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 100)
    tentativa = 0
    while True:
        palpite = int(input("Adivinhe o número (entre 1 e 100): "))
        tentativa += 1
        if palpite < numero_secreto:
            print("Tente um número maior.")
        elif palpite > numero_secreto:
            print("Tente um número menor.")
        else:
            print(f"Parabéns! Você acertou em {tentativa} tentativas.")
            break

jogo_adivinhacao()