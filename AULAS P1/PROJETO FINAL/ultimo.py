import requests
from deep_translator import GoogleTranslator
import tkinter as tk
from tkinter import messagebox

# API


def get_advice():
    try:
        response = requests.get('https://api.adviceslip.com/advice')
        if response.status_code == 200:
            advice_data = response.json()['slip']
            return advice_data['id'], advice_data['advice']
        else:
            messagebox.showerror("Erro", "Erro ao acessar a API de conselhos.")
            return None, None
    except Exception as e:
        messagebox.showerror("Erro", f"Erro: {e}")
        return None, None

# traduzir


def translate_advice(advice):
    try:
        translator = GoogleTranslator(source='en', target='pt')
        translated_advice = translator.translate(advice)
        return translated_advice
    except Exception as e:
        messagebox.showerror("Erro", f"Erro na tradução: {e}")
        return None

# exibir  conselhos


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
            translated_advice = translate_advice(advice)
            if translated_advice:
                all_advices.append(f"Conselho {advice_id} (Inglês): {
                                   advice}\n(Traduzido): {translated_advice}\n")

    if all_advices:
        result_text.set("\n\n".join(all_advices))

# salvar conselhos


def save_advice():
    advice_text = result_text.get()
    if advice_text:
        try:
            with open('conselhos.txt', 'a') as file:
                file.write(advice_text + '\n\n')
            messagebox.showinfo("Salvo", "Conselho salvo com sucesso.")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao salvar o conselho: {e}")
    else:
        messagebox.showwarning(
            "Aviso", "Nenhum conselho disponível para salvar.")

# conselhos salvos


def show_saved_advices():
    try:
        with open('conselhos.txt', 'r') as file:
            advices = file.readlines()
            if advices:
                saved_advices_window = tk.Toplevel()
                saved_advices_window.title("Conselhos Salvos")
                saved_advices_text = tk.Text(
                    saved_advices_window, wrap=tk.WORD, width=50, height=15)
                saved_advices_text.pack(padx=10, pady=10)

                for advice in advices:
                    saved_advices_text.insert(tk.END, advice.strip() + '\n')

                saved_advices_text.config(state=tk.DISABLED)
            else:
                messagebox.showinfo(
                    "Sem Conselhos", "Nenhum conselho salvo ainda.")
    except FileNotFoundError:
        messagebox.showerror("Erro", "Arquivo de conselhos não encontrado.")


def create_gui():
    window = tk.Tk()
    window.title("Conselhos da Cachaçaria do Seu Zé")

    window.geometry("600x500")

    title_font = ("Helvetica", 14, "bold")
    button_font = ("Helvetica", 12)
    label_font = ("Helvetica", 12)

    instruction_label = tk.Label(
        window,
        text="Escolha quantos conselhos deseja receber:",
        font=title_font,
        justify="center"
    )
    instruction_label.pack(pady=20)

    global num_advices_entry
    num_advices_entry = tk.Entry(window, font=label_font, justify="center")
    num_advices_entry.pack(pady=20)

    advice_button = tk.Button(
        window,
        text="Receber Conselhos",
        font=button_font,
        command=show_multiple_advices
    )
    advice_button.pack(pady=20)

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

    save_button = tk.Button(
        window,
        text="Salvar Conselhos",
        font=button_font,
        command=save_advice
    )
    save_button.pack(pady=20)

    view_saved_button = tk.Button(
        window,
        text="Ver Conselhos Salvos",
        font=button_font,
        command=show_saved_advices
    )
    view_saved_button.pack(pady=20)

    exit_button = tk.Button(
        window,
        text="Sair",
        font=button_font,
        command=window.quit
    )
    exit_button.pack(pady=20)

    window.mainloop()


if __name__ == "__main__":
    create_gui()
