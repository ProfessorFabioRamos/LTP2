import tkinter as tk

root = tk.Tk()
root.title("Calculadora Quatro Operações")
root.geometry("400x400")
# Cor do fundo em hex
root.configure(bg="#e2eb94")

# FG = cor da letra, BG = cor do fundo
label = tk.Label(root, text="HELLO WORLD !", bg = "#0d00ff", fg="#ffffff"
                 , font = ("Shadow of the Deads",16))
label.pack(pady=10)

free_label = tk.Label(root,text="Texto Livre")
free_label.place(x=320,y=200)

root.mainloop()
