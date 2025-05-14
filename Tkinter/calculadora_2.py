import tkinter as tk

root = tk.Tk()
root.title("Calculadora Quatro Operações")
root.geometry("400x400")
# Cor do fundo em hex
root.configure(bg="#e2eb94")
# Variável de resultado inicializada com 0
result = 0

title = tk.Label(root, text="Calculadora", font=("Arial",16,"bold"))
# Label ocupando 2 colunas na linha 0 
title.grid(row=0,column=0,columnspan=2, pady=(10))

entry1 = tk.Entry(root,width=10)
entry1.grid(row=1, column=0,padx=20,sticky="e") # sticky = alinhamento, e = East (Leste)

entry2 = tk.Entry(root,width=10)
entry2.grid(row=1, column=1,padx=20,sticky="e") # sticky = alinhamento, e = East (Leste)

def operacao(id):
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    match id:
        case 0:
            result = num1+num2
        case 1:
            result = num1-num2
        case 2:
            result = num1*num2
        case 3:
            result = num1/num2
    label_result.config(text=f"Resultado: {result:.2f}")

# Botão de soma
sum_button = tk.Button(root, text="+")
sum_button.grid(row=2, column=0, padx=10, pady= 10)
sum_button.config(command=lambda:operacao(0))

# Botão de subtração
sub_button = tk.Button(root, text="-")
sub_button.grid(row=2, column=1, padx=10, pady= 10)
sub_button.config(command=lambda:operacao(1))

# Botão de multiplicação
mult_button = tk.Button(root, text="*")
mult_button.grid(row=2, column=2, padx=10, pady= 10)
mult_button.config(command=lambda:operacao(2))

# Botão de divisão
div_button = tk.Button(root, text="/")
div_button.grid(row=2, column=3, padx=10, pady= 10)
div_button.config(command=lambda:operacao(3))

label_result = tk.Label(root, text="Resultado: ", font=("Arial",16))
label_result.grid(row=3,column=0, columnspan=2, pady=20)

root.mainloop()
