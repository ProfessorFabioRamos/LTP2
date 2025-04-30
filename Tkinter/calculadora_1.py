# Biblioteca Simples para GUI
import tkinter as tk

# Cria a janela principal
root = tk.Tk()

# Título da janela
root.title("Salve!")

# Define o tamanho da janela (largura x altura)
root.geometry("300x250")

# Função a ser chamada quando botão for pressionado
def calcular():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    soma = num1+num2
    label_result.config(text = f"Resultado: {soma}")

# Cria widget sem instanciar objeto
tk.Label(root, text = "CALCULADORA", font=("Arial,16")).pack(pady=5)

# Cria um Entry(entrada) para o primeiro número
entry1 = tk.Entry(root)
entry1.pack(pady=5)

# Símbolo de soma(+)
tk.Label(root, text = "+", font=("Arial,12")).pack(pady=5)

# Cria um Entry(entrada) para o segundo número
entry2 = tk.Entry(root)
entry2.pack(pady=5)

# Cria um Button para chamar função de calcular
button = tk.Button(root,text = "Somar", command=calcular)
button.pack(pady=5)

# Cria um widget Label para exibir o resultado da soma
label_result = tk.Label(root, text="Resultado: ", font=("Comic Sans MS", 16))
label_result.pack(pady=5)

# Inicia o loop de eventos, mantendo a janela aberta
root.mainloop()
