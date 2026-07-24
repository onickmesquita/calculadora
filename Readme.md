# Projeto de aprendizagem 

---
# Calculadora em Python

Uma aplicação de calculadora desenvolvida em **Python** com interface gráfica utilizando **Tkinter**, criada com o objetivo de praticar os fundamentos da linguagem e conceitos de desenvolvimento de aplicações desktop.

---

## Sobre o Projeto

Este projeto consiste no desenvolvimento de uma calculadora gráfica inspirada em calculadoras físicas tradicionais.

Além das operações matemáticas básicas, o projeto contará com sistema de memória, tratamento de erros e uma interface intuitiva.

O principal objetivo é aplicar os conhecimentos adquiridos durante os estudos de Python em um projeto prático e organizado.

---

## Objetivo da aplicação


- Praticar lógica de programação
- Aprender programação orientada a objetos
- Trabalhar com interfaces gráficas utilizando Tkinter
- Organizar projetos em módulos
- Utilizar tratamento de exceções
- Criar uma aplicação semelhante a uma calculadora real

## Tecnologias

- Python 3.14.6
- Tkinter
- VS Code/ PyCharm
- Git
- GitHub

---

## Funcionalidades

### Operações Matemáticas

- ✅ Soma
- ✅ Subtração
- ✅ Multiplicação
- ✅ Divisão

### Interface

- Display para exibição dos cálculos
- Botões numéricos
- Botões das operações
- Botão "="
- Botão "."
- Botão Q/C (Limpar)

### Sistema de Memória

- M+
- M-

### Tratamento de Erros

- Divisão por zero
- Entrada inválida
- Operações incompletas
---

## Interface Desejada

```
┌───────────────────┐
│                   │
│      DISPLAY      │
│                   │
├───────────────────┤
│ Q/C │ M- │ M+ │ ÷ │
├───────────────────┤
│  7  │ 8  │ 9  │ × │
├───────────────────┤
│  4  │ 5  │ 6  │ - │
├───────────────────┤
│  1  │ 2  │ 3  │ + │
├───────────────────┤
│  0  │ .  │    =   │
└───────────────────┘
```

---
## Estrutura do Projeto

```
calculadora/

│
├── assets/
│
├── src/
│   ├── main.py
│   ├── interface.py
│   ├── operacoes.py
│   ├── memoria.py
│   ├── display.py
│   └── utils.py
│
├── README.md
│
└── requirements.txt
```

---
# Roadmap do Projeto

## Etapa 1 – Planejamento

### Objetivos
- Definir funcionalidades
- Criar fluxo da aplicação
- Planejar estrutura de pastas

### Conceitos praticados

- Lógica
- Organização
---
## Etapa 2 — Calculadora no Terminal

### Objetivos

Criar uma versão simples utilizando apenas o terminal.

### Funcionalidades

- Soma
- Subtração
- Multiplicação
- Divisão

### Conceitos

- print()
- input()
- if
- elif
- else
- while

---

## Etapa 3 — Modularização

Separar o projeto em arquivos.

Exemplo:

```
main.py
operacoes.py
```
### Conceitos

- def
- return
- import

---

## Etapa 4 — Interface Gráfica

Criar a janela da aplicação.

### Implementar

- Display
- Botões
- Layout

### Conceitos

- Tkinter
- Frames
- Labels
- Buttons

---
## Etapa 5 — Integração

Conectar os botões às funções matemáticas.

Exemplo:

```
Botão 5

↓

Display recebe 5

↓

Usuário pressiona +

↓

Escolhe outro número

↓

Resultado aparece no display
```

---

## Etapa 6 — Sistema de Memória

Adicionar os botões:

- M+
- M-

### Funcionamento

M+ : Guarda o número atual.

M- : Subtrai o valor atual da memória.

---
## Etapa 7 — Botão Q/C

Implementar limpeza completa da calculadora.

Ao clicar:

- Limpa display
- Limpa operação
- Limpa resultado

---
## Etapa 8 — Tratamento de Erros

Implementar:

- Divisão por zero
- Operação inválida
- Clique duplo em operadores

Utilizar:

```
try
except
```
---

## Etapa 9 — Melhorias Visuais

Deixar a interface mais dinâmica.

Adicionar:

- Cores
- Fontes
- Espaçamento
- Bordas
- Ícones

---

## Etapa 10 — Melhorias Futuras

### Funcionalidades

- Histórico de operações
- Teclado numérico
- Atalhos
- Tema escuro
- Tema claro
- Responsividade
- Sons dos botões

---
# Conceitos de Python Utilizados

- Variáveis
- Tipos de dados
- Operadores
- Condições
- Laços de repetição
- Funções
- Módulos
- Classes
- Objetos
- Tratamento de exceções
- Organização de projetos

---

## Fluxograma lógico

---
```
Início

↓

Criar Interface

↓

Aguardar clique

↓

Número?

↓

Adicionar ao display

↓

Operador?

↓

Salvar operação

↓

Novo número

↓

=

↓

Executar cálculo

↓

Mostrar resultado

↓

Nova operação
```
---

# Possíveis Melhorias

- Histórico de cálculos
- Copiar resultado
- Colar número
- Calculadora científica
- Porcentagem
- Potência
- Raiz quadrada
- Logaritmo
- Seno
- Cosseno
- Tangente

---

# Aprendizados

Este projeto foi desenvolvido para consolidar conhecimentos em:

- Python
- Programação Orientada a Objetos
- Interfaces Gráficas
- Organização de Código
- Boas práticas de desenvolvimento

---

# Autor

Desenvolvido por **Nicholas** como projeto de estudos em Python.