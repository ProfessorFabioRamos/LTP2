# Biblioteca Simples para GUI
import tkinter as tk

# Cria a janela principal
root = tk.Tk()

# Título da janela
root.title("Salve!")

# Define o tamanho da janela (largura x altura)
root.geometry("300x150")

# Função a ser chamada quando botão for pressionado
def on_button_click():
    saudacao = f"Salve, {entry.get()}!"
    label_result.config(text=saudacao)

# Cria widget sem instanciar objeto
tk.Label(root, text = "Seu nome:").pack(pady=5)

# Cria um widget Entry(entrada) que recebe uma string
entry = tk.Entry(root)
# Ajusta espaçamento em pixels
entry.pack(pady=5)

# Cria um widget Label(rótulo) que será alterado pela função
label_result = tk.Label(root, text="", font=("Verdana, 16"))
label_result.pack(pady=5)

button = tk.Button(root,text = "Saudar", command=on_button_click)
button.pack(pady=5)

# Inicia o loop de eventos, mantendo a janela aberta
root.mainloop()
