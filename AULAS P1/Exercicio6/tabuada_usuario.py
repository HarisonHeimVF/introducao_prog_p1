# tabuada_usuario.py
def tabuada_usuario():
    numero = int(input("Digite um número para calcular a tabuada: "))
    with open("tabuada_usuario.txt", "w") as file:
        for i in range(1, 11):
            resultado = numero * i
            file.write(f"{numero} x {i} = {resultado}\n")

if __name__ == "__main__":
    tabuada_usuario()