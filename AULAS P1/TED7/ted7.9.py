def desenha_triangulo(n):
    for i in range(1, n + 1):
        print('*' * i)

n = int(input("Quantas linhas o triângulo deve ter? "))
desenha_triangulo(n)