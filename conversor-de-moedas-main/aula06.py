import tkinter as tk

def confirmar_escolha():
    # Pega o que foi digitado no campo de nome e remove os espaços em branco
    nome_jogador = nome.get().strip()
    # Pega o valor do Radiobutton selecionado
    classe_escolhida = var_classe.get()

    # Validação para garantir que o usuário preencheu tudo
    if not nome_jogador:
        resultado.config(text="Por favor, digite o nome do personagem.", fg="#842029")
        return
    
    if not classe_escolhida:
        resultado.config(text="Por favor, selecione uma classe.", fg="#842029")
        return

    # Usando o match case para definir a cor e a mensagem com base na classe
    match classe_escolhida:
        case 'Guerreiro':
            cor_destaque = "#DB1A1A"
        case 'Mago':
            cor_destaque = "#6E1A37"
        case 'Arqueiro':
            cor_destaque = "#72BAA9"

    mensagem = f"Parabéns! O {classe_escolhida} {nome_jogador} está pronto para a aventura."
    resultado.config(text=mensagem, fg=cor_destaque)

def fechar():
    janela.destroy()

def atualizar_imagem():
    """Atualiza a imagem mostrada com base na classe selecionada no Radiobutton."""
    classe_escolhida = var_classe.get()
    if classe_escolhida in imagens_classes:
        label_imagem.config(image=imagens_classes[classe_escolhida])

# --- Janela ---
janela = tk.Tk()
largura = 800
altura = 500

# Centralizar na tela
screen_w = janela.winfo_screenwidth()
screen_h = janela.winfo_screenheight()
pos_x = int((screen_w / 2) - (largura / 2))
pos_y = int((screen_h / 2) - (altura / 2))

janela.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")
janela.configure(bg="#f3f3f3")
janela.overrideredirect(True) # Remove a barra superior padrão do Windows

# --- Carregamento das Imagens ---
# IMPORTANTE: O Tkinter aceita arquivos .png e .gif nativamente com PhotoImage.
# Certifique-se de que os arquivos img1.png, img2.png e img3.png estejam na mesma pasta deste script.
# Mantenha o tamanho das imagens razoável (ex: 200x200 ou 250x250 pixels) para não quebrar o layout.
try:
    imagens_classes = {
        "Guerreiro": tk.PhotoImage(file="assets\img1.png"),
        "Mago": tk.PhotoImage(file="assets\img2.png"),
        "Arqueiro": tk.PhotoImage(file="assets\img3.png")
    }
except tk.TclError:
    # Caso as imagens não sejam encontradas, criamos um dicionário vazio para não dar erro
    print("Aviso: Imagens não encontradas na pasta. O programa rodará sem elas.")
    imagens_classes = {}

# --- Botão fechar customizado ---
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
    text="Criação de Personagem",
    font=("Segoe UI", 26, "bold"),
    bg="#f3f3f3",
    fg="#1f1f1f"
)
# Aumentei o columnspan para abraçar a nova coluna da imagem
titulo.grid(row=0, column=0, columnspan=4, pady=(0, 20))

# --- Nome do Personagem ---
fonte_label = ("Segoe UI", 14)

tk.Label(frame, text="Nome do seu personagem:", bg="#f3f3f3", font=fonte_label).grid(row=1, column=0, columnspan=3, pady=(10, 5))

nome = tk.Entry(frame, width=30, font=("Segoe UI", 14), relief="solid", borderwidth=1)
nome.grid(row=2, column=0, columnspan=3, pady=(0, 20))

# --- Escolha da Classe ---
tk.Label(frame, text="Escolha sua classe:", bg="#f3f3f3", font=fonte_label).grid(row=3, column=0, columnspan=3, pady=(10, 5))

var_classe = tk.StringVar(value="")

# Adicionado o parâmetro command=atualizar_imagem em cada Radiobutton
rb_guerreiro = tk.Radiobutton(frame, text="Guerreiro", variable=var_classe, value="Guerreiro", command=atualizar_imagem, bg="#f3f3f3", font=("Segoe UI", 12), activebackground="#f3f3f3")
rb_mago = tk.Radiobutton(frame, text="Mago", variable=var_classe, value="Mago", command=atualizar_imagem, bg="#f3f3f3", font=("Segoe UI", 12), activebackground="#f3f3f3")
rb_arqueiro = tk.Radiobutton(frame, text="Arqueiro", variable=var_classe, value="Arqueiro", command=atualizar_imagem, bg="#f3f3f3", font=("Segoe UI", 12), activebackground="#f3f3f3")

rb_guerreiro.grid(row=4, column=0, padx=10, pady=10)
rb_mago.grid(row=4, column=1, padx=10, pady=10)
rb_arqueiro.grid(row=4, column=2, padx=10, pady=10)

# --- Label da Imagem (Nova adição) ---
# Fica na coluna 3, expandindo pelas linhas para ficar ao lado do formulário
label_imagem = tk.Label(frame, bg="#f3f3f3")
label_imagem.grid(row=1, column=3, rowspan=5, padx=(30, 0))

# --- Botão Confirmar ---
botao = tk.Button(
    frame,
    text="Confirmar",
    command=confirmar_escolha,
    bg="#7aa7ff",
    fg="white",
    font=("Segoe UI", 14, "bold"),
    relief="flat",
    padx=20,
    pady=8,
    activebackground="#5a85de",
    activeforeground="white",
    cursor="hand2"
)
botao.grid(row=5, column=0, columnspan=3, pady=30)

# --- Resultado ---
resultado = tk.Label(
    frame,
    text="",
    bg="#f3f3f3",
    font=("Segoe UI", 14, "bold")
)
resultado.grid(row=6, column=0, columnspan=4)

janela.mainloop()