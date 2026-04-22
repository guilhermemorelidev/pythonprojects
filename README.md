🐍 Projeto Python Básico

Este projeto contém exemplos simples em Python utilizando estruturas fundamentais da linguagem, como:

Entrada de dados com input()
Conversão de tipos com int()
Estruturas condicionais (if, else, elif)
Uso de match case
Criação e uso de funções
📂 Estrutura do Projeto
📁 projeto-python/
 ├── main.py
 ├── funcoes.py
 └── README.md
🚀 Funcionalidades
🔹 Entrada de dados

O programa utiliza input() para receber informações do usuário.

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
🔹 Condicionais (if/else)
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")
🔹 Estrutura match-case
opcao = int(input("Escolha uma opção: "))

match opcao:
    case 1:
        print("Opção 1 escolhida")
    case 2:
        print("Opção 2 escolhida")
    case _:
        print("Opção inválida")
🔹 Funções
def saudacao(nome):
    return f"Olá, {nome}!"

print(saudacao("Maria"))
▶️ Como executar
Instale o Python (versão 3.10 ou superior recomendada)
Clone ou baixe o projeto
Execute o arquivo principal:
python main.py
📚 Objetivo

Este projeto foi criado para praticar conceitos básicos de programação em Python, sendo ideal para iniciantes.

🛠️ Tecnologias utilizadas
Python 3
✍️ Autor

Guilherme Moreli
