
import tkinter as tk

def ledados():
    try:
        name = nome.get()
        tel = telefone.get()
        idade_user = int(idade.get())

        parar_piscar()

        if idade_user >= 18:
            resultado.config(
                text=f"Bem-vindo, {name}! Entrada permitida.",
                fg="#0f5132"
            )
        else:
            resultado.config(
                text=f"{name}, entrada não permitida.",
                fg="#842029"
            )
            mostrar_aviso(name)

    except ValueError:
        resultado.config(
            text="Digite uma idade válida.",
            fg="#842029"
        )

# --- Piscar ---
piscando = False

def piscar():
    global piscando
    if piscando:
        atual = aviso_nome.cget("bg")
        novo = "#ffcccc" if atual == "#ffffff" else "#ffffff"
        aviso_nome.config(bg=novo)
        janela.after(400, piscar)

def mostrar_aviso(name):
    global piscando
    aviso_nome.config(text=f"{name} NÃO PODE ENTRAR")
    aviso_nome.grid(row=2, column=1, pady=(0,10))  # abaixo do campo nome
    piscando = True
    piscar()

def parar_piscar():
    global piscando
    piscando = False
    aviso_nome.grid_forget()

# --- Fechar ---
def fechar():
    janela.destroy()

# --- Janela ---
janela = tk.Tk()
largura = 800
altura = 500

# centralizar
screen_w = janela.winfo_screenwidth()
screen_h = janela.winfo_screenheight()

pos_x = int((screen_w / 2) - (largura / 2))
pos_y = int((screen_h / 2) - (altura / 2))

janela.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")
janela.configure(bg="#f3f3f3")
janela.overrideredirect(True)

# --- Botão fechar ---
btn_fechar = tk.Button(
    janela,
    text="✕",
    command=fechar,
    bg="#f3f3f3",
    fg="#444",
    borderwidth=0,
    font=("Segoe UI", 12, "bold"),
    activebackground="#ff5c5c",
    activeforeground="white"
)
btn_fechar.place(relx=0.97, rely=0.02, anchor="ne")

# --- Frame principal ---
frame = tk.Frame(janela, bg="#f3f3f3")
frame.place(relx=0.5, rely=0.5, anchor="center")

# --- Título ---
titulo = tk.Label(
    frame,
    text="Controle de Acesso",
    font=("Segoe UI", 26, "bold"),
    bg="#f3f3f3",
    fg="#1f1f1f"
)
titulo.grid(row=0, column=0, columnspan=2, pady=20)

# --- Labels ---
fonte_label = ("Segoe UI", 14)

tk.Label(frame, text="Nome:", bg="#f3f3f3", font=fonte_label)\
    .grid(row=1, column=0, sticky="w", pady=10)

nome = tk.Entry(frame, width=25, font=("Segoe UI", 14), relief="flat")
nome.grid(row=1, column=1, pady=10)

# --- Aviso piscante (fica abaixo do nome) ---
aviso_nome = tk.Label(
    frame,
    text="",
    font=("Segoe UI", 12, "bold"),
    bg="#ffffff",
    fg="#842029",
    padx=10,
    pady=5
)

tk.Label(frame, text="Telefone:", bg="#f3f3f3", font=fonte_label)\
    .grid(row=3, column=0, sticky="w", pady=10)

telefone = tk.Entry(frame, width=25, font=("Segoe UI", 14), relief="flat")
telefone.grid(row=3, column=1, pady=10)

tk.Label(frame, text="Idade:", bg="#f3f3f3", font=fonte_label)\
    .grid(row=4, column=0, sticky="w", pady=10)

idade = tk.Entry(frame, width=25, font=("Segoe UI", 14), relief="flat")
idade.grid(row=4, column=1, pady=10)

# --- Botão ---
botao = tk.Button(
    frame,
    text="Confirmar",
    command=ledados,
    bg="#7aa7ff",
    fg="white",
    font=("Segoe UI", 14, "bold"),
    relief="flat",
    padx=15,
    pady=8
)
botao.grid(row=5, column=0, columnspan=2, pady=20)

# --- Resultado ---
resultado = tk.Label(
    frame,
    text="",
    bg="#f3f3f3",
    font=("Segoe UI", 14)
)
resultado.grid(row=6, column=0, columnspan=2)

# --- Linha azul inferior ---
linha = tk.Frame(janela, bg="#7aa7ff", height=3)
linha.pack(side="bottom", fill="x")

janela.mainloop()


