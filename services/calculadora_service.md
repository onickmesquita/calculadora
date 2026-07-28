# Fluxo das funções

## Somar

```

     Início
       │
       ▼
Recebe num1 e num2
       │
       ▼
    Calcula:
   num1 + num2
       │
       ▼
Armazena o resultado
       │
       ▼
Retorna o resultado
       │
       ▼
      Fim       

```

## Subtrair

```

    Início
       │
       ▼
Recebe num1 - num2
       │
       ▼
    Calcula:
  num1 - num2
       │
       ▼
Armazena o resultado    
       │
       ▼
Retorna o resultado
       │
       ▼
      Fim      

```

## Multiplicar

```

    Início
       │
       ▼
Recebe num1 * num2
       │
       ▼
    Calcula:
  num1 * num2
       │
       ▼
Armazena o resultado    
       │
       ▼
Retorna o resultado
       │
       ▼
      Fim      

```

## Dividir

```
     Início 
        │
        ▼
Recebe num1 e num2
        │
        ▼
num2 é igual a 0?
      │
 ┌────┴──────┐
 │           │
Sim         Não
 │           │
 │           │
 │           ▼
 ▼        Calcula:
raise    num1 / num2
Erro         │
 │           ▼
 │   Armazena o resultado
 │           │
 │           ▼
Fim   return resultado

```

NOTA: 

**raise** = Tratamento de erro específico para divisão por zero.

A palavra-chave raise significa:
>"Pare a execução e lance um erro."

Nesse caso, ela lança um erro do tipo "ZeroDivisionError", com a mensagem:

>"Não é possível dividir por zero."



## Importância da estrutura da class CalculadoraService

1. **Isolamento**: A lógica de negócio está protegida de mudanças na interface visual.

2. **Facilidade de Teste**: Podemos testar essas funções matematicamente sem precisar abrir a janela do Tkinter.

3. **Tratamento de Erros**: Foi incluida a validação para divisão por zero, sugerido na documentação do Python.