def tabuada():
    numero = int(input("Insira um número para ver sua tabuada: "))
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

tabuada()