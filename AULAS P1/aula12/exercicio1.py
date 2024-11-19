import tkinter as tk
from tkinter import messagebox

# Lista de compras
lista_compras = []

# Função para adicionar item


def adicionar_item():
    nome_item = entry_item.get()
    categoria_item = entry_categoria.get()
    if nome_item and categoria_item:
        lista_compras.append(f'{nome_item} - {categoria_item}')
        messagebox.showinfo('Item adicionado', f'{nome_item} adicionado à lista.')
        entry_item.delete(0, tk.END)
        entry_categoria.delete(0, tk.END)
    else:
        messagebox.showwarning('Erro', 'Preencha ambos os campos')

# Função para remover item


def remover_item():
    nome_item = entry_item.get()
    if nome_item:
        item_encontrado = None
        for item in lista_compras:
            if item.startswith(nome_item):
                item_encontrado = item
                break
        if item_encontrado:
            lista_compras.remove(item_encontrado)
            messagebox.showinfo('Item Removido', f'{nome_item} removido da lista.')
        else:
            messagebox.showwarning(
                'Erro', f'{nome_item} não encontrado na lista.')
        entry_item.delete(0, tk.END)
    else:
        messagebox.showwarning('Erro', 'Digite o nome do item a ser removido.')

# Função para exibir a lista de compras


def exibir_lista():
    if lista_compras:
        lista_formatada = '\n'.join(lista_compras)
        messagebox.showinfo('Lista de compras',
                            f'Lista Atual:\n{lista_formatada}')
    else:
        messagebox.showinfo('Lista de Compras', 'A lista está vazia.')

# Função para sair do programa


def sair_do_programa():
    root.quit()


# Configuração da interface gráfica usando tkinter
root = tk.Tk()
root.title('Lista de Compras Inteligente')
root.geometry("400x300")

# Labels e entradas de texto para o item e a categoria
label_item = tk.Label(root, text="Nome do Item:")
label_item.pack(pady=5)
entry_item = tk.Entry(root, width=40)
entry_item.pack(pady=5)

label_categoria = tk.Label(root, text="Categoria do Item:")
label_categoria.pack(pady=5)
entry_categoria = tk.Entry(root, width=40)
entry_categoria.pack(pady=5)

# Botões para adicionar, remover e exibir itens
btn_adicionar = tk.Button(root, text="Adicionar Item", command=adicionar_item)
btn_adicionar.pack(pady=5)

btn_remover = tk.Button(root, text="Remover Item", command=remover_item)
btn_remover.pack(pady=5)

btn_exibir = tk.Button(root, text="Exibir Lista", command=exibir_lista)
btn_exibir.pack(pady=5)

# Botão para sair do programa
btn_sair = tk.Button(root, text="Sair", command=sair_do_programa)
btn_sair.pack(pady=10)

# Inicia o loop principal da interface gráfica
root.mainloop()
