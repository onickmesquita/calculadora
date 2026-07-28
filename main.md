# Arquivo main

O **main.py** deve ser o orquestrador, responsável por instanciar a lógica e iniciar a interface.

## O que este arquivo faz?

1. **Orquestração**: Ele importa a classe especializada de cálculos da pasta services/

2. **Injeção de Dependência**:  Seguindo o princípio DIP (Inversão de Dependência), o plano é criar o serviço aqui e "injetá-lo" na interface gráfica quando a criarmos.

3. **Segurança**: O bloco if __name__ == "__main__": evita que a calculadora comece a rodar sozinha caso você importe este arquivo em outro lugar no futuro.