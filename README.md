# 🐍 Projeto Python Básico — SENAI

> Projeto de introdução à linguagem Python, desenvolvido como parte das atividades práticas do curso no SENAI.

---

## 📋 Sobre o Projeto

Este projeto reúne exemplos práticos das estruturas fundamentais do Python, com foco em clareza e aprendizado progressivo. Ideal para quem está dando os primeiros passos na programação.

---

## 📂 Estrutura do Projeto

```
📁 projeto-python/
 ├── main.py        # Arquivo principal de execução
 ├── funcoes.py     # Funções reutilizáveis
 └── README.md      # Documentação do projeto
```

---

## 🚀 Funcionalidades

### 🔹 Entrada de Dados

Uso do `input()` para interação com o usuário e `int()` para conversão de tipos:

```python
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
```

---

### 🔹 Estruturas Condicionais (`if / else / elif`)

Tomada de decisões com base em condições:

```python
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")
```

---

### 🔹 Estrutura `match case`

Alternativa moderna ao encadeamento de `if/elif`, disponível a partir do Python 3.10:

```python
opcao = int(input("Escolha uma opção: "))

match opcao:
    case 1:
        print("Opção 1 escolhida")
    case 2:
        print("Opção 2 escolhida")
    case _:
        print("Opção inválida")
```

---

### 🔹 Funções

Criação e chamada de funções para organizar e reutilizar código:

```python
def saudacao(nome):
    return f"Olá, {nome}!"

print(saudacao("Maria"))
```

---

## ▶️ Como Executar

1. Certifique-se de ter o **Python 3.10 ou superior** instalado
   - [Download Python](https://www.python.org/downloads/)

2. Clone ou baixe este repositório

3. No terminal, navegue até a pasta do projeto e execute:

```bash
python main.py
```

---

## 📚 Objetivo

Este projeto foi criado para praticar os conceitos fundamentais de programação em Python aprendidos nas aulas do SENAI, cobrindo:

- [x] Entrada e saída de dados
- [x] Conversão de tipos
- [x] Estruturas condicionais
- [x] `match case`
- [x] Criação de funções

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Versão |
|------------|--------|
| Python | 3.10+ |

---

## ✍️ Autor

**Guilherme Moreli**  
Estudante — SENAI

---

> 💡 *Primeiro commit — início da jornada em Python!* 🚀
