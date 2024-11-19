def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b
    print()

n = int(input("Quantos termos da sequência de Fibonacci você quer ver? "))
fibonacci(n)