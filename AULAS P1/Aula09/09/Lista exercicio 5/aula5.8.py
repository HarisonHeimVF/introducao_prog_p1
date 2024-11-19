# Função para calcular o bônus com base nas missões completadas
def calcular_bonus(missoes):
    if missoes > 10:
        return 100  # Bônus de 100 moedas de ouro
    elif 5 <= missoes <= 10:
        return 50  # Bônus de 50 moedas de ouro
    else:
        return 10  # Bônus de 10 moedas de ouro

# Solicitar o número de missões completadas ao usuário
try:
    missoes = int(input("Digite o número de missões completadas: "))
    print(f'Por {missoes} missões.')
    bonus = calcular_bonus(missoes)
    print(f"O cavaleiro receberá {bonus} moedas de ouro como bônus.")
    
except ValueError:
    print("Por favor, insira um número válido de missões.")