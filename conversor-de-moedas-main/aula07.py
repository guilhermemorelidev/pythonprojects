import tkinter as tk
from tkinter import messagebox
import random
import pygame  # Para o som
from PIL import Image, ImageTk  # Para carregar as imagens

class DadoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Super Dado 25 Faces")
        self.root.geometry("400x500")

        # Inicializa o mixer de som
        pygame.mixer.init()

        # Configurações iniciais
        self.numero_secreto = random.randint(1, 25)
        
        # Widgets
        self.label_instrucao = tk.Label(root, text="Tente adivinhar o número (1-25):", font=("Arial", 12))
        self.label_instrucao.pack(pady=10)

        self.entrada = tk.Entry(root, font=("Arial", 14))
        self.entrada.pack(pady=5)

        self.btn_sortear = tk.Button(root, text="Girar Dado!", command=self.rolar_dado, 
                                     bg="blue", fg="white", font=("Arial", 12, "bold"))
        self.btn_sortear.pack(pady=20)

        # Espaço para a imagem do dado
        self.canvas_dado = tk.Label(root)
        self.canvas_dado.pack(pady=10)

    def tocar_som(self):
        try:
            pygame.mixer.music.load("sorteio.mp3") # Certifique-se de ter esse arquivo
            pygame.mixer.music.play()
        except:
            print("Arquivo de som não encontrado.")

    def rolar_dado(self):
        try:
            palpite = int(self.entrada.get())
            self.tocar_som()
            
            # Sorteia o resultado visual do dado
            resultado_dado = random.randint(1, 25)
            self.atualizar_imagem(resultado_dado)

            if palpite == self.numero_secreto:
                messagebox.showinfo("Vitoria!", f"Incrível! O número era {self.numero_secreto}.")
                self.numero_secreto = random.randint(1, 25) # Reinicia o jogo
            elif palpite < self.numero_secreto:
                messagebox.showwarning("Dica", "Mais alto! Tente de novo.")
            else:
                messagebox.showwarning("Dica", "Mais baixo! Tente de novo.")
                
        except ValueError:
            messagebox.showerror("Erro", "Por favor, digite um número válido.")

    def atualizar_imagem(self, numero):
        try:
            # Carrega a imagem correspondente ao número sorteado
            img = Image.open(f"imagens/{numero}.png")
            img = img.resize((200, 200)) # Ajusta o tamanho
            self.foto = ImageTk.PhotoImage(img)
            self.canvas_dado.config(image=self.foto)
        except:
            self.canvas_dado.config(text=f"🎲 {numero}", font=("Arial", 50))

# Inicialização do App
if __name__ == "__main__":
    root = tk.Tk()
    app = DadoApp(root)
    root.mainloop()