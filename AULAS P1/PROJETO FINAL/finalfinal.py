import tkinter as tk
from tkinter import messagebox
import requests
from deep_translator import GoogleTranslator

# Função para consumir a API de conselhos


def get_advice():
    try:
        response = requests.get("https://api.adviceslip.com/advice")
        if response.status_code == 200:
            data = response.json()
            advice_id = data['slip']['id']
            advice = data['slip']['advice']
            return advice_id, advice
        else:
            messagebox.showerror("Erro", "Erro ao acessar a API de conselhos.")
            return None, None
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao conectar-se à API: {e}")
        return None, None

# Função para traduzir o conselho para o idioma selecionado


def translate_advice(advice, target_lang):
    try:
        translator = GoogleTranslator(source='pt', target=target_lang)
        translated_advice = translator.translate(advice)
        return translated_advice
    except Exception as e:
        messagebox.showerror("Erro", f"Erro na tradução: {e}")
        return None

# Função para exibir múltiplos conselhos diretamente em português


def show_multiple_advices():
    try:
        num_advices = int(num_advices_entry.get())
    except ValueError:
        messagebox.showwarning("Aviso", "Por favor, insira um número válido.")
        return

    all_advices = []

    for _ in range(num_advices):
        advice_id, advice = get_advice()
        if advice:
            # Traduzir o conselho para português diretamente
            advice_in_portuguese = translate_advice(advice, 'pt')
            if advice_in_portuguese:
                # Adicionar o conselho traduzido à lista
                all_advices.append(f"Conselho {advice_id} (Português): {
                                   advice_in_portuguese}")

    if all_advices:
        result_text.set("\n\n".join(all_advices))




def translate_saved_advice():
    selected_lang = language_var.get() 
    if selected_lang == "Português":
        target_lang = 'pt'
    elif selected_lang == "Alemão":
        target_lang = 'de'
    elif selected_lang == "Espanhol":
        target_lang = 'es'
    else:
        messagebox.showwarning("Aviso", "Selecione um idioma válido.")
        return

    advice_text = result_text.get()
    if advice_text:
        advice_text_pt = advice_text.split("(Português): ")[1]
        translated_advice = translate_advice(advice_text_pt, target_lang)
        if translated_advice:
            result_text.set(f"{advice_text}\n\nTraduzido para {
                            selected_lang}: {translated_advice}")
    else:
        messagebox.showwarning(
            "Aviso", "Nenhum conselho disponível para traduzir.")

# Função para salvar conselhos em um arquivo de texto


def save_advice():
    advice_text = result_text.get()
    if advice_text:
        with open("conselhos_salvos.txt", "a") as file:
            file.write(advice_text + "\n\n")
        messagebox.showinfo("Salvo", "Conselho salvo com sucesso!")
    else:
        messagebox.showwarning(
            "Aviso", "Nenhum conselho disponível para salvar.")

# Função para exibir conselhos salvos


def show_saved_advices():
    try:
        with open("conselhos_salvos.txt", "r") as file:
            saved_advices = file.read()
            if saved_advices:
                result_text.set(saved_advices)
            else:
                result_text.set("Nenhum conselho salvo ainda.")
    except FileNotFoundError:
        result_text.set("Nenhum conselho salvo ainda.")

# Criação da interface gráfica usando tkinter


def create_gui():
    window = tk.Tk()
    window.title("Conselhos da Cachaçaria do Seu Zé")

    # Definir tamanho da janela
    window.geometry("500x500")

    # Fonte maior para os textos
    title_font = ("Helvetica", 14, "bold")
    button_font = ("Helvetica", 12)
    label_font = ("Helvetica", 12)

    # Título com fonte maior e centralizado
    instruction_label = tk.Label(
        window,
        text="Escolha quantos conselhos deseja receber:",
        font=title_font,
        justify="center"
    )
    instruction_label.pack(pady=10)

    # Entrada para o número de conselhos
    global num_advices_entry
    num_advices_entry = tk.Entry(window, font=label_font, justify="center")
    num_advices_entry.pack(pady=10)

    # Botão para receber múltiplos conselhos
    advice_button = tk.Button(
        window,
        text="Receber Conselhos",
        font=button_font,
        command=show_multiple_advices
    )
    advice_button.pack(pady=10)

    # Label para exibir os conselhos e traduções, centralizado
    global result_text
    result_text = tk.StringVar()
    advice_label = tk.Label(
        window,
        textvariable=result_text,
        font=label_font,
        wraplength=450,
        justify="center"
    )
    advice_label.pack(pady=20)

    # Opções de idioma para traduzir o conselho
    global language_var
    language_var = tk.StringVar(value="Português")
    languages = ["Inglês", "Alemão", "Espanhol"]
    language_menu = tk.OptionMenu(window, language_var, *languages)
    language_menu.pack(pady=10)

    # Botão para traduzir o conselho
    translate_button = tk.Button(
        window,
        text="Traduzir Conselho",
        font=button_font,
        command=translate_saved_advice
    )
    translate_button.pack(pady=10)

    # Botão para salvar os conselhos
    save_button = tk.Button(
        window,
        text="Salvar Conselhos",
        font=button_font,
        command=save_advice
    )
    save_button.pack(pady=10)

    # Botão para ver conselhos salvos
    view_saved_button = tk.Button(
        window,
        text="Ver Conselhos Salvos",
        font=button_font,
        command=show_saved_advices
    )
    view_saved_button.pack(pady=10)

    # Botão para sair do programa
    exit_button = tk.Button(
        window,
        text="Sair",
        font=button_font,
        command=window.quit
    )
    exit_button.pack(pady=10)

    # Iniciar loop da janela
    window.mainloop()


# Executar o programa com interface
if __name__ == "__main__":
    create_gui()
