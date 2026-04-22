class Lampada:
    def __init__(self):
        self.ligada = False

    def clicar_interruptor(self):
        self.ligada = not self.ligada

    def verificar_estado(self):
        if self.ligada:
            print("A lâmpada está acesa.")
        else:
            print("A lâmpada está apagada.")

minha_lampada = Lampada()
minha_lampada.clicar_interruptor()
minha_lampada.verificar_estado()


class Pet:
    def __init__(self, nome):
        self.nome = nome
        self.fome = 50

    def alimentar(self):
        self.fome -= 10

    def brincar(self):
        self.fome += 15

meu_pet = Pet("Ronaldinho")
meu_pet.brincar()
print(f"meu pet {meu_pet.nome} brincou e es {meu_pet.fome}")


class Bicicleta:
    def __init__(self):
        self.velocidade = 0

    def pedalar(self):
        self.velocidade += 5

    def frear(self):
        self.velocidade -= 5
        if self.velocidade < 0:
            self.velocidade = 0

bike = Bicicleta()
bike.pedalar()
bike.frear()
print(f"Velocidade atual: {bike.velocidade} km/h")