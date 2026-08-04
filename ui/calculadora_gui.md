# Documentação calculadora_gui

## Importações

1. *import tkinter as tk*

```
Importa a biblioteca Tkinter, que é responsável por criar janelas, botões, caixas de texto, menus etc. Foi dado o apelido tk em vez de escrever tkinter.Tk(), você escreve tk.Tk().
``` 

2. *from tkinter import ttk*

```
Aqui é importado o módulo ttk. O ttk possui componentes mais modernos do Tkinter.

Exemplo:

- ttk.Button()
- ttk.Entry()
- ttk.Label()

Eles possuem um visual melhor que os componentes tradicionais.
```


## *Classe CalculadoraGUI*

Essa classe será responsável apenas pela interface gráfica.

Ela apenas:

- cria janela
- cria botões
- cria display
- envia informações para outra classe


## ***def `__init__`(self, service):***

Esse é o construtor da classe. Sempre que alguém fizer `gui = CalculadoraGUI(service)` o Python executará automaticamente o método `__init__`.

### + ***O parâmetro service:***
Perceba: `(service)`, Esse objeto representa a classe responsável pelos cálculos.

Por exemplo:

```
class CalculadoraService:

    def somar(self, a, b):
        return a + b

```

Depois:

```

service = CalculadoraService()

gui = CalculadoraGUI(service)

```

A interface recebe essa classe pronta. Isso é chamado de **Injeção de Dependência (Dependency Injection)**

### + ***self.service = service***

Guarda o objeto recebido dentro da própria classe.

Agora qualquer método poderá acessar self.service

Por exemplo:

```
self.service.somar(10,20)
```

Observe o comentário *Injeção da lógica de cálculos*, ou seja, a interface não calcula, ela apenas chama `service.somar()`

### + ***self.window = tk.Tk()***

Cria a janela principal, é equivalente a "Abra uma janela.", depois dessa linha já existe uma janela na memória.

### + ***self.window.title("Calculadora Python")***

Define o título da janela. Na barra superior aparecerá: - "Calculadora Python"

### + ***self._configurar_layout()***

Assim que a janela é criada, esse método monta toda a interface.

Ele criará:

- display
- botões
- organização

## ***def _configurar_layout(self):***

Método privado (pela convenção do _). Responsável por desenhar toda a interface.

### + ***self.display = ttk.Entry(...)***

Cria uma caixa de texto. Ela será o visor da calculadora.

Exemplo:

```
____________________

45+8

____________________
```

Dentro dela aparecem vários parâmetros.

1. `self.window`
     Diz que esse componente pertence à janela.

2. `font=("Arial",24)`
    Fonte usada.

3. `justify='right'`
    Todo texto digitado ficará alinhado à direita.


### + ***self.display.grid(...)***

Agora o display é colocado na janela. Antes ele existia. Agora ele ganha uma posição.

1. `row`
    row=0 - Linha zero. Primeira linha.

2. `columnspan`
    columnspan=4 - O display ocupa quatro colunas.
    Ex.
    ```
    ---------
    |       |
    ---------
    |7|8|9|+|
    |4|5|6|-|
    ```

3. `sticky`
    sticky="nsew", Significa:

    North
    South
    East
    West

Ou seja:

O componente se estica para todos os lados da célula.

4. `padx` 
    Espaçamento horizontal.

5. `pady`
    Espaçamento vertical.


### + ***btn_soma = ttk.Button(...)***

Cria um botão.

1. **Primeiro argumento**
    self.window - O botão pertence à janela.

2. **text**
    text="+" - Texto mostrado no botão. `+`

3. **command** 
    command=self._executar_soma - Quando o usuário clicar no botão: `+` o Python executará automaticamente: `self._executar_soma()`


### + ***btn_soma.grid(...)***

Posiciona o botão.


## ***def _executar_soma(self):***

Método chamado quando o botão é pressionado.

# Fluxo esperado:

```

Usuário

↓

Interface

↓

CalculadoraService

↓

Resultado

↓

Interface

```

A GUI apenas:

- lê números
- chama o serviço
- mostra o resultado

Quem realmente calcula é outra classe.


### + ***pass***

Significa:

"Ainda não implementei esse método." É apenas um espaço reservado.

## ***def run(self):***

Cria um método chamado run(). Sua única responsabilidade é iniciar a interface.

### + ***self.window.mainloop()***

Essa é a linha mais importante do Tkinter. Ela inicia o loop de eventos da interface. Enquanto essa linha estiver executando, o programa fica "escutando" ações do usuário: 

- clique em botão
- digitação
- fechar janela
- redimensionar janela

Sem ela, a janela abriria e fecharia imediatamente.

# Resumo do fluxo do programa

```
Criar CalculadoraGUI
          │
          ▼
     __init__()
          │
          ├── Guarda o service
          │
          ├── Cria a janela
          │
          ├── Define o título
          │
          └── Chama _configurar_layout()
                       │
                       ▼
                 Cria display
                 Cria botão "+"
            Organiza tudo com grid()
                       │
                       ▼
                     run()
                       │
                       ▼
               window.mainloop()
                       │
                       ▼
       Usuário interage com a calculadora
                       │
                       ▼
                Clique no botão "+"
                       │
                       ▼
               _executar_soma()
                       │
                       ▼
          Chama `self.service.somar(...)`
                       │
                       ▼
           Exibe o resultado no display
```