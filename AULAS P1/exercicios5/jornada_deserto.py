def verificar_agua(suficiente, distancia):
    return suficiente >= distancia * 2

agua = float(input("Quantidade de água disponível (litros): "))
distancia = float(input("Distância até o oásis (km): "))
if verificar_agua(agua, distancia):
    print("A quantidade de água é suficiente.")
else:
    print("A quantidade de água não é suficiente.")