from os import system as lt

lt("cls")


class Carro:
    def __init__(self, cor: str, fabricante: str, potencia: float, ano: int, modelo: str):
        self.cor = cor
        self.fabricante = fabricante
        self.potencia = potencia
        self.ano = ano
        self.modelo = modelo
        self.ligado = False
        self.velocidade = 0
        self.farol = False

    def __str__(self):
        return f"{self.modelo} {self.fabricante} ({self.ano}) - {self.cor}"

    def ligar(self):
        if not self.ligado:
            self.ligado = True
            return "Carro ligado."
        return "O carro já está ligado."

    def desligar(self):
        if self.ligado:
            self.ligado = False
            self.velocidade = 0
            return "Carro desligado."
        return "O carro já está desligado."

    def acelerar(self):
        if not self.ligado:
            return "Ligue o carro primeiro."

        if self.velocidade < 100:
            self.velocidade += 5

        return f"Velocidade: {self.velocidade} Km/h"

    def desacelerar(self):
        if not self.ligado:
            return "Ligue o carro primeiro."

        if self.velocidade > 0:
            self.velocidade -= 5

        return f"Velocidade: {self.velocidade} Km/h"

    def frear(self):
        self.velocidade = 0
        return "Carro parado."

    def farol_on(self):
        self.farol = True
        return "Farol aceso."

    def farol_off(self):
        self.farol = False
        return "Farol apagado."


# Lista de objetos (PONTO PRINCIPAL DA REFATORAÇÃO)
carros = [
    Carro("vermelho", "Chevrolet", 200, 1985, "Opala"),
    Carro("amarelo", "Fiat", 100, 1980, "Fiat 147"),
    Carro("preto", "Volkswagen", 50, 1976, "Fusca"),
]


def menu_carro(carro: Carro):
    while True:
        print("\n========================")
        print(carro)
        print("========================")

        op = input(
            "1 - Ligar\n"
            "2 - Desligar\n"
            "3 - Acelerar\n"
            "4 - Desacelerar\n"
            "5 - Acender Farol\n"
            "6 - Apagar Farol\n"
            "7 - Frear\n"
            "8 - Voltar\n-> "
        )

        match op:
            case "1":
                print(carro.ligar())
            case "2":
                print(carro.desligar())
            case "3":
                print(carro.acelerar())
            case "4":
                print(carro.desacelerar())
            case "5":
                print(carro.farol_on())
            case "6":
                print(carro.farol_off())
            case "7":
                print(carro.frear())
            case "8":
                break
            case _:
                print("Opção inválida.")

        input("Pressione ENTER...")
        lt("cls")


def menu_principal():
    while True:
        print("=== Escolha um carro ===")

        for i, carro in enumerate(carros):
            print(f"{i + 1} - {carro}")

        print("0 - Sair")

        escolha = input("-> ")

        if escolha == "0":
            break

        if escolha.isdigit():
            indice = int(escolha) - 1

            if 0 <= indice < len(carros):
                menu_carro(carros[indice])
            else:
                print("Carro inválido.")
        else:
            print("Entrada inválida.")

        input("Pressione ENTER...")
        lt("cls")


menu_principal()