import tkinter as tk
from tkinter import messagebox
import banco 

def iniciar_interface():
    root = tk.Tk()
    root.title("Cadastro de Produtos")
    root.geometry("500x500")

    #Funções internas
    def inserir():
        nome = entry_nome.get()
        preco = entry_preco.get()

        if nome == "" or preco =="":
            messagebox.showwarning("Atenção","Preencha todos os campos!")
            return
        
        try:
            preco_float = float(preco)
            banco.inserir_produto(nome,preco_float)
            messagebox.showinfo("Sucesso",f"Produto {nome} inserido!")
            entry_nome.delete(0,tk.END)
            entry_preco.delete(0,tk.END)
        except ValueError:
            messagebox.showerror("Erro","Preço inválido")
        listar()

    def listar():
        listbox.delete(0,tk.END)
        produtos = banco.listar_produtos()
        for p in produtos:
            listbox.insert(tk.END,f"ID: {p[0]} | {p[1]} | R$ {p[2]:.2f}")
    
    def excluir():
        id_produto = entry_id.get()
        if id_produto =="":
            messagebox.showwarning("Atenção","Informe o ID para excluir!")
            return
        linhas_excluidas = banco.excluir_produto(id_produto)
        if linhas_excluidas == 0:
            messagebox.showinfo("Info","Nenhum produto com esse ID.")
        else:
            messagebox.showinfo("Sucesso",f"Produto com ID {id_produto} excluído")
        entry_id.delete(0,tk.END)

    # Widgets
    tk.Label(root,text = "Nome do produto:").pack(pady=10)
    entry_nome = tk.Entry(root)
    entry_nome.pack(pady=5)

    tk.Label(root,text = "Preço:").pack(pady=10)
    entry_preco = tk.Entry(root)
    entry_preco.pack(pady=5)

    tk.Button(root,text="Inserir Produto",command=inserir).pack(pady=10)

    tk.Label(root,text="Produtos Cadastrados:").pack(pady=10)
    listbox = tk.Listbox(root,width=50)
    listbox.pack(pady=5)

    tk.Label(root,text= "ID do produto para excluir:").pack(pady=10)
    entry_id = tk.Entry(root)
    entry_id.pack(pady=5)

    tk.Button(root,text="Excluir Produto",command=excluir).pack(pady=5)
    listar()
    root.mainloop()
