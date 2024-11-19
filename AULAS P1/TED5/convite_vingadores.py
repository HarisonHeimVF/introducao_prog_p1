# convite_vingadores.py

def convidar_vingadores():
    # Abrindo o arquivo vingadores.txt para leitura
    with open("vingadores.txt", "r") as arquivo:
        # Lendo todos os nomes do arquivo
        vingadores = arquivo.readlines()
    
    # Removendo espaços em branco e novas linhas
    vingadores = [vingador.strip() for vingador in vingadores]

    # Enviando convite para cada Vingador
    for vingador in vingadores:
        print(f"Olá {vingador}, você está convidado para a festa na minha casa!")

if __name__ == "__main__":
    convidar_vingadores()