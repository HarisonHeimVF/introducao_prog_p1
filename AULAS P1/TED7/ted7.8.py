def decimal_para_binario(n):
    binario = ""
    while n > 0:
        binario = str(n % 2) + binario
        n //= 2
    return binario or "0"

n = int(input("Insira um número decimal: "))
print(f"Binário: {decimal_para_binario(n)}")