# numeros_divisiveis.py
def numeros_resto_5():
    for num in range(1000, 2001):
        if num % 11 == 5:
            print(num)

if __name__ == "__main__":
    numeros_resto_5()