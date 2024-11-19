# cadastro.py
def cadastro_usuarios():
    usuarios = []
    for _ in range(3):  # Cadastro de 3 usuários
        nome = input("Digite o nome: ")
        idade = input("Digite a idade: ")
        email = input("Digite o email: ")
        usuarios.append({"nome": nome, "idade": idade, "email": email})

    print("\nUsuários cadastrados:")
    for usuario in usuarios:
        print(f"Nome: {usuario['nome']}, Idade: {
              usuario['idade']}, Email: {usuario['email']}")


if __name__ == "__main__":
    cadastro_usuarios()
