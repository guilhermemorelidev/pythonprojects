try:
    numero1 = int(input("digite o primeiro numero "))
    dividir = int(input("quantas vezes você quer dividir? "))
    resultado = numero1 / dividir
    print(resultado)

except ZeroDivisionError:
    print("nao pode dividir por 0")


try:
    numero1 = int(input("digite o primeiro numero "))
    numero2 = int(input("digite o segundo numero "))
    resultado = numero1 + numero2
    print(resultado)

except ValueError:
    print("Você precisa digitar um numero inteiro")