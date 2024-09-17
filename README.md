# Desafio Sistema Bancário

Este projeto foi desenvolvido como parte do desafio do bootcamp de **Ciência de Dados com Python** da NTT em parceria com a DIO. O sistema simula operações bancárias básicas, permitindo depósitos, saques, e a visualização do extrato.

## Funcionalidades

O sistema implementa três operações principais:

1. **Depositar**: Permite ao usuário adicionar saldo à conta.
2. **Sacar**: O usuário pode realizar saques com um limite diário de 3 saques e um valor máximo de R$ 500,00 por saque.
3. **Extrato**: Mostra todas as movimentações financeiras (depósitos e saques) realizadas até o momento.

Além dessas funcionalidades, o sistema também permite que o usuário encerre o programa com a opção de saída.

## Como Funciona

Ao iniciar o programa, um menu será exibido para o usuário com as opções disponíveis:

O usuário pode selecionar uma das operações digitando o número correspondente. Dependendo da operação escolhida, o sistema solicitará as informações necessárias, como o valor do depósito ou saque. Após cada operação, o saldo será atualizado e exibido ao usuário.

### Detalhes Técnicos

- **Saldo Inicial**: R$ 0,00
- **Limite de Saque Diário**: 3 saques
- **Valor Máximo por Saque**: R$ 500,00
- **Controle de Movimentações**: O extrato exibe todas as transações feitas durante a execução do programa.

### Funções Implementadas

- `deposito(saldo, extrato)`: Função que realiza o depósito e atualiza o extrato.
- `sacar(saldo, extrato, numero_saques, LIMITE_SAQUES)`: Função para sacar um valor, considerando o saldo e o limite diário de saques.
- `ext(extrato)`: Exibe o extrato de movimentações realizadas.

## Tecnologias Utilizadas

- **Linguagem**: Python

## Autor

Este projeto foi desenvolvido por **Jonathan Davi** para concluir o desafio do bootcamp **Ciência de Dados com Python** da NTT DATA em parceria com a DIO.

