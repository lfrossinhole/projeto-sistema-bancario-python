# Desafio de Projeto 1: Criando um Sistema Bancário em Python

## Objetivo:
- Criar um código em Python que implemente as operações: Depósito, Saque e Extrato

## Especificações do Desafio:

### 1 - Operação de Depósito:
- Deve aceitar somente valores positivos
- Os depósitos devem ser armazenados em uma variável para posterior exibição no Extrato

### 2 - Operação de Saque:
- Limite máximo de 3 saques diários
- Limite máximo de valor de saque de R$ 500,00
- Exibir mensagem caso o valor do saque seja maior que o saldo em conta
- Os saques devem ser armazenados em uma variável para posterior exibição no Extrato

### 3 - Operação de Extrato:
- Deve listar todos os depósitos e saques realizados
- Ao final da listagem, deve exibir o saldo atual em conta no formato "R$ xxx.xx"
- Se o extrato extiver em branco, exibir mensagem "Não foram realizadas movimentações."

## Tecnologias Utilizadas:
- Fundamentos da Linguagem Python 🐍

<br>
<br>
<br>

# Desafio de Projeto 2: Otimizando o Sistema Bancário com Funções Python

## Objetivo:
- Separar as funções existentes de saque, depósito e extrato em funções.
- Criar duas novas funções: cadastrar usuário (cliente) e cadastrar conta bancária.

## Desafio:
Precisamos deixar nosso código mais modularizado, para isso vamos criar funções para as operações existentes:
- Sacar
- Depositar
- Visualizar histórico

Além disso, para a versão 2 do nosso sistema precisamos criar duas novas funções:
- Criar usuário (cliente do banco)
- Criar conta corrente (vincular com o usuario)

## Separação em funções:
- Devemos criar funções para todas as operações do sistema.
- Para exercitar tudo o que aprendemos neste módulo, cada função vai ter uma regra na passagem de argumentos.
- O retorno e a forma como serão chamadas, pode ser definida por você da forma que achar melhor.

## Especificações do Desafio:

### 1 - Operação de Saque:
- A função saque deve receber os argumentos apenas por nome (keyword only).
- Sugestão de argumentos: saldo, valor, extrato, limite, numero_saques, limite_saques.
- Sugestão de retorno: saldo e extrato.


### 2 - Operação de Depósito:
- A função depósito deve receber os argumentos apenas por posição (positional only).
- Sugestão de argumentos: saldo, valor, extrato.
- Sugestão de retorno: saldo e extrato.

### 3 - Operação de Extrato:
- A função extrato deve receber os argumentos por posição e nome (positional only e keyword only).
- Argumentos posicionais: saldo
- Argumentos nomeados: extrato

### 4 - Criar usuário (cliente)
- O programa deve armazenar os usuários em uma lista.
- Um usuário é composto por: nome, data de nascimento, cpf e endereço.
- O endereço é uma string com formado: logradouro, nro - bairro - cidade/sigla estado.
- Deve ser armazenado somente os números do CPF. (sem ponto nem traço, também é uma string)
- Não podemos cadastrar 2 usuários com o mesmo CPF. (o sistema não deve aceitar se o CPF for repetido)

### 5 - Criar conta corrente
- O programa deve armazenar as contas em uma lista.
- Uma conta é composta por: agência, número da conta e usuário.
- O número da conta é sequencial, iniciando em 1.
- O números da agência é fixo: "0001".
- Um usuário pode ter mais de uma conta, mas uma conta pertence a somente um usuário.

## Dica
para vincular um usuário a uma conta, filtre a lista de usuários buscando o número de CPF informado para cada usuário da lista.

## Tecnologias Utilizadas:
- Estruturas de Dados da Linguagem Python 🐍
