# convites.py
def enviar_convites():
    convidados = ["Celebridade A", "Celebridade B", "Celebridade C", "Celebridade D", "Celebridade E"]
    print("Convites enviados:")
    for convidado in convidados:
        print(f"Olá {convidado}, você está convidado para o jantar!")

    # Um convidado não poderá ir
    desistente = "Celebridade B"
    print(f"\n{desistente} não poderá comparecer.")

    # Novos convidados
    novos_convidados = ["Celebridade F", "Celebridade G"]
    convidados.remove(desistente)
    convidados.extend(novos_convidados)

    print("\nNovos convites enviados:")
    for convidado in convidados:
        print(f"Olá {convidado}, você está convidado para o jantar!")

if __name__ == "__main__":
    enviar_convites()