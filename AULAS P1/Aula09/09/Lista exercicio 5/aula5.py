numero = float(input("Digite um número (inteiro ou real): "))

if numero >= 0:
    print("O número é positivo.")
else:
    print("O número é negativo.")


quantidade_macas = int(input("Digite o número de maçãs compradas: "))

if quantidade_macas < 12:
    preco_por_maca = 1.30
else:
    preco_por_maca = 1.00

custo_total = quantidade_macas * preco_por_maca

print(f"O custo total da compra é R$ {custo_total:.2f}")
