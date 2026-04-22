import tkinter as tk

def calcular_idade():
    try:
        idade = int(entry_idade.get())
        if idade >= 18:
            classificacao = "Acesso Permitido"
            label_resultado.config(text=classificacao, fg="green")
        else:
            classificacao = "Acesso negado: você tem menos de 18 anos"
            label_resultado.config(text=classificacao, fg="red")
            
    except ValueError:
        label_resultado.config(text="Por favor, digite valores numéricos válidos.", fg="orange")

# --- Janela ---
janela = tk.Tk()
janela.title("Cadastro de usuários")
janela.geometry("800x600")

# Definimos uma tupla de fonte para facilitar a repetição
FONTE_PADRAO = ("Arial", 16)
FONTE_TITULO = ("Arial", 20, "bold")

# Centralizar as colunas da grade (grid)
janela.grid_columnconfigure(0, weight=1)
janela.grid_columnconfigure(1, weight=1)

# --- Widgets com tamanhos maiores ---
tk.Label(janela, text="Sistema de Controle", font=FONTE_TITULO).grid(row=0, column=0, columnspan=2, pady=30)

tk.Label(janela, text="Digite sua idade:", font=FONTE_PADRAO).grid(row=1, column=0, padx=10, pady=10, sticky="e")

# Aumentamos a largura (width) e a fonte do campo de entrada
entry_idade = tk.Entry(janela, font=FONTE_PADRAO, width=10)
entry_idade.grid(row=1, column=1, padx=10, pady=10, sticky="w")

# Botão maior usando 'ipadx' e 'ipady' (espaçamento interno)
botao_calcular = tk.Button(janela, text="ACESSAR", font=FONTE_PADRAO, command=calcular_idade, bg="#007bff", fg="white")
botao_calcular.grid(row=2, column=0, columnspan=2, pady=30, ipadx=50, ipady=10)

# Resultado com fonte maior
label_resultado = tk.Label(janela, text="", font=("Cascadia Code", 14, "bold"), wraplength=700)
label_resultado.grid(row=3, column=0, columnspan=2, pady=20)

janela.mainloop()
