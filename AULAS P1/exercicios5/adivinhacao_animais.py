def adivinhar_animal():
    tipo = input("Seu animal favorito é mamífero ou réptil? ").lower()
    if tipo == "mamífero":
        print("Seu animal favorito deve ser um cachorro!")
    elif tipo == "réptil":
        print("Seu animal favorito deve ser uma tartaruga!")
    else:
        print("Tipo desconhecido.")

adivinhar_animal()