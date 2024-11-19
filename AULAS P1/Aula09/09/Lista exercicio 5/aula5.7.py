def classificar_planta(altura):
    if altura < 1:
        return "Pequena"
    elif 1 <= altura <= 3:
        return "Média"
    else:
        return "Grande"
    
try:
    altura = float(input("Digite a altura da planta em metros: "))
    classificacao = classificar_planta(altura)
    print(f"A planta é classificada como: {classificacao}")
except ValueError:
    print("Por favor, insira um valor numérico válido para a altura.")    