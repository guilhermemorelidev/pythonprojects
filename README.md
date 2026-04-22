🚀 Projeto Python: Fundamentos da Programação
Este é um projeto desenvolvido para praticar e demonstrar o uso das estruturas fundamentais da linguagem Python. O foco aqui foi aplicar lógica de programação utilizando sintaxes limpas e eficientes. 
🛠️ O que foi utilizado?
Neste projeto, você encontrará exemplos práticos de:
input(): Interação com o usuário para coleta de dados.
int() & Tipagem: Conversão de dados para números inteiros e manipulação de tipos.
if, elif, else: Estruturas condicionais para tomada de decisão no código.
match case: Introduzido no Python 3.10, utilizado para seleções mais elegantes (similar ao switch de outras linguagens).
def (Funções): Modularização do código para torná-lo reutilizável e organizado. 
📂 Estrutura do Código
O projeto está dividido em blocos que executam as seguintes lógicas:
Entrada de Dados: O programa solicita informações ao usuário.
Processamento: Os dados são validados e processados através de funções.
Saída: O resultado é exibido no console com base nas condições verificadas. 
🚀 Como executar o projeto
Certifique-se de ter o Python 3.10 ou superior instalado (necessário para o match case).
Clone este repositório:
bash
git clone https://github.com
Use o código com cuidado.
Navegue até a pasta e execute o arquivo principal:
bash
python main.py
 
Exemplo de trecho implementado:
python
def saudar_usuario(opcao):
    match opcao:
        case 1:
            return "Olá! Bem-vindo ao sistema."
        case 2:
            return "Até logo! Saindo..."
        case _:
            return "Opção inválida."
