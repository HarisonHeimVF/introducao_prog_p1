def classificar_planta(altura):
    if altura < 1:
        return "Pequena"
    elif altura <= 3:
        return "Média"
    else:
        return "Grande"

altura = float(input("Altura da planta (em metros): "))
classificacao = classificar_planta(altura)
print(f"A planta é classificada como: {classificacao}")