def fatorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

n = int(input("Insira um número para calcular o fatorial: "))
print(f"Fatorial de {n} é {fatorial(n)}.")