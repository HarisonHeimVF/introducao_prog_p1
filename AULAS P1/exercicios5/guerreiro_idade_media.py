def verificar_liga(ferro, ouro):
    total = ferro + ouro
    percentual_ferro = (ferro / total) * 100
    return percentual_ferro >= 70

ferro = float(input("Quantidade de ferro (kg): "))
ouro = float(input("Quantidade de ouro (kg): "))
if verificar_liga(ferro, ouro):
    print("A liga tem a quantidade adequada de ferro.")
else:
    print("A liga não tem a quantidade necessária de ferro.")