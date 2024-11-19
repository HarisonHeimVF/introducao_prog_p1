def calcular_bonus(missoes):
    if missoes > 10:
        return 100
    elif 5 <= missoes <= 10:
        return 50
    else:
        return 10

missoes = int(input("Número de missões completadas: "))
bonus = calcular_bonus(missoes)
print(f"Bônus: {bonus} moedas de ouro")