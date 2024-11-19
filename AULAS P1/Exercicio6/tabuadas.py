# tabuadas.py

def gerar_tabuadas():
    # Abrindo o arquivo "tabuadas.txt" em modo de escrita
    with open("tabuadas.txt", "w") as file:
        # Loop para os números de 1 a 10
        for i in range(1, 11):
            # Loop para multiplicadores de 1 a 10
            for j in range(1, 11):
                resultado = i * j
                # Escrevendo a tabuada no arquivo
                file.write(f"{i} x {j} = {resultado}\n")

if __name__ == "__main__":
    gerar_tabuadas()