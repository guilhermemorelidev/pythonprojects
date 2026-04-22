#funções
from os import system as lt 
lt("cls")

#1

# def dobro(valor1: int):
#     dobrar = valor1 * 2
#     return dobrar

# valor1 = int(input("digite o numero que deseja dobrar "))
# valor_dobro = dobro(valor1)

# print(f"o dobro de {valor1} é {valor_dobro}")

#2

# def apresentacao(nome: str, idade: int)-> tuple:
#     return nome, idade

# apresentar = apresentacao("guilherme", 16)


# print(f"meu nome é {apresentar[0]} e minha idade é {apresentar[1]}")

# def calcular_media(valor1: float, valor2: float)-> float:
#     media = (valor1 + valor2) / 2
#     return media 

# media_final = calcular_media(8.7, 9.5)

# print(f"a média final é {media_final}") 

def e_par(valor: int) -> bool:
    return valor % 2 == 0

numero = int(input("Digite um número: "))

if e_par(numero):
    print("par")
else:
    print("impar")
    

