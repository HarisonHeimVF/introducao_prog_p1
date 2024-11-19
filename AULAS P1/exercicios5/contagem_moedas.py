def calcular_total(moedas_1_real, moedas_50_centavos, moedas_25_centavos):
    total = (moedas_1_real * 1) + (moedas_50_centavos * 0.50) + (moedas_25_centavos * 0.25)
    return total

moedas_1_real = int(input("Quantidade de moedas de 1 real: "))
moedas_50_centavos = int(input("Quantidade de moedas de 50 centavos: "))
moedas_25_centavos = int(input("Quantidade de moedas de 25 centavos: "))
total = calcular_total(moedas_1_real, moedas_50_centavos, moedas_25_centavos)
print(f"Valor total: R$ {total:.2f}")