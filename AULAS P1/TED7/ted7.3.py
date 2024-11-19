def conta_vogais_consoantes():
    frase = input("Digite uma frase: ").lower()
    vogais = "aeiou"
    consoantes = 0
    cont_vogais = 0
    for letra in frase:
        if letra.isalpha():
            if letra in vogais:
                cont_vogais += 1
            else:
                consoantes += 1
    print(f"Vogais: {cont_vogais}, Consoantes: {consoantes}")

conta_vogais_consoantes()