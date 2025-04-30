# Biblioteca Simples para GUI
import tkinter as tk

# Cria a janela principal
root = tk.Tk()

# Título da janela
root.title("Aula 1 Tk")

# Define o tamanho da janela (largura x altura)
root.geometry("300x150")

# Função a ser chamada quando botão for pressionado
def on_button_click():
    label.config(text = "Bem-vindo!")

# Cria um widget Label(rótulo) dentro da janela Root
label = tk.Label(root, text="Olá Mundo!", font = ("Arial, 14"))
# Posiciona o label no centro, com espaçamento vertical
label.pack(pady=10)

# Cria um widget Button(botão) que chama a função on_button_click ao clicar
button = tk.Button(root, text= "Clique aqui", command= on_button_click)
# Posiciona o botão abaixo do label com espaçamento
button.pack(pady=5)

# Inicia o loop de eventos, mantendo a janela aberta
root.mainloop()
