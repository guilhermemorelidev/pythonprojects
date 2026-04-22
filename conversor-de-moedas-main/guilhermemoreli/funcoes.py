def contagem_letras(frase: str, letra : str) -> int:
    """Função para contar as letras de uma frase
    """
    contagem = 0 
    for i in frase:
        if i in letra:
            contagem += 1
        return contagem
    
def soma(*valor1 : int | float) -> int | float:
    total_soma = 0
    valor2 = valor1[0]
    for i in valor2:
        total_soma += 1
    return total_soma


def bom_dia():
    print("bom dia")
    
def boa_noite():
    print("boa noite")
    
def multiplicar(a,b):
    return a * b

def dividir(a,b):
    return a / b

