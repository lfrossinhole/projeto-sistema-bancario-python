# =================== MÓDULOS ===================

import textwrap
from abc import ABC, abstractmethod
from datetime import datetime

# =================== CLASSES ===================

class Cliente:
    def __init__(self, endereco):
        self._endereco = endereco
        self._contas = []
    
    @property
    def contas(self):
        return self._contas
    
    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)
    
    def adicionar_conta(self, conta):
        self._contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._cpf = cpf

    @property
    def nome(self):
        return self._nome
    
    @property
    def cpf(self):
        return self._cpf
    
    @property
    def data_nascimento(self):
        return self._data_nascimento

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod # método de fábrica
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    @property # get_saldo
    def saldo(self):
        return self._saldo
    
    @property # get_numero
    def numero(self):
        return self._numero
    
    @property # get_agencia
    def agencia(self):
        return self._agencia

    @property # get_cliente
    def cliente(self):
        return self._cliente
    
    @property # get_historico
    def historico(self):
        return self._historico
    
    def sacar(self, valor):
        saldo = self._saldo
        excedeu_saldo = (valor > saldo)

        if excedeu_saldo:
            print("Saldo insuficiente! Operação cancelada.")
        
        elif valor > 0:
            self._saldo -= valor
            print("Valor sacado com sucesso!")
            return True
        
        else:
            print("Valor informado inválido! Operação cancelada.")
        
        return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("Valor depositado com sucesso!")
            return True
        
        else:
            print("Valor inválido! Operação cancelada.")
        
        return False

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques

    def sacar(self, valor): # Sobrescrita do método sacar
        numero_saques = len(
            [transacao for transacao in self._historico.transacoes if transacao["tipo"] == Saque.__name__]
        )

        excedeu_limite = (valor > self._limite)
        excedeu_saques = (numero_saques >= self._limite_saques)

        if excedeu_limite:
            print(f"Valor acima do limite de R$ {self._limite:.2f} por saque! Operação cancelada.")
        
        elif excedeu_saques:
            print(f"Limite máximo de {self._limite_saques:.0f} saques por dia atingido!")
        
        else:
            return super().sacar(valor)
        
        return False
    
    def __str__(self): # o "self.cliente.nome" funciona por conta do POLIMORFISMO com HERANÇA
        return f"""
            Agência:\t{self._agencia}
            C/C:\t\t{self._numero}
            Titular:\t{self._cliente.nome}
            """

class Historico:
    def __init__(self):
        self._transacoes = []
    
    @property # get_transacoes
    def transacoes(self):
        return self._transacoes
    
    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            }
        )

class Transacao(ABC): # interface
    @property # get_valor
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = (conta.sacar(self._valor))

        if sucesso_transacao:
            conta._historico.adicionar_transacao(self)

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor
    
    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = (conta.depositar(self._valor))
    
        if sucesso_transacao:
            conta._historico.adicionar_transacao(self)

# =================== FUNÇÕES ===================

def menu():
    
    menu = """
    ==============MENU==============
    [d]\tDepositar
    [s]\tSacar
    [e]\tVisualizar Extrato
    [nu]\tNovo Usuário
    [nc]\tNova Conta
    [lc]\tListar Contas
    [q]\tSair

    => """

    return input(textwrap.dedent(menu))

def depositar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\nCliente não encontrado!")
        return

    valor = float(input("Informe o valor do depósito: "))
    transacao = Deposito(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    cliente.realizar_transacao(conta, transacao)

def sacar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\nCliente não encontrado!")
        return
    
    valor = float(input("Informe o valor do saque: "))
    transacao = Saque(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    cliente.realizar_transacao(conta, transacao)

def exibir_extrato(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\nCliente não encontrado!")
        return
    
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    print("\n============Extrato=============")
    transacoes = conta.historico.transacoes

    extrato = ""
    if not transacoes:
        extrato = "Não foram realizadas movimentações."
    
    else:
        for transacao in transacoes:
            extrato += f"\n{transacao['tipo']}: \n\tR$ {transacao['valor']:.2f}"
    
    print(extrato)
    print(f"\nSaldo: \n\tR$ {conta.saldo:.2f}")
    print("================================")

def criar_cliente(clientes):
    cpf = input("Digite seu CPF (somente números): ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print("\nCPF já cadastrado! Operação cancelada.")
        return
    
    nome = input("Digite seu nome completo: ")
    data_nascimento = input("Digite sua data de nascimento (dd-mm-aaaa): ")
    endereco = input("Digite seu endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)
    
    clientes.append(cliente)

    print("\nCadastro realizado com sucesso!")

def filtrar_cliente(cpf, clientes):
    # Compreensão de Listas
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
#                        [Retorno][        iteração       ][        Filtro        ]

    return clientes_filtrados[0] if clientes_filtrados else None

def criar_conta(numero_conta, clientes, contas):
    cpf = input("Digite seu CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\nCliente não encontraro! Operação Cancelada.")
        return
    
    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)

    print("\nConta criada com sucesso!")

def listar_contas(contas):
    for conta in contas:
        print("=" * 32)
        print(textwrap.dedent(str(conta)))

def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("\nCliente não possui conta!")
        return
    
    # FIXME: não permite cliente escolher a conta
    return cliente.contas[0]

def main():

    clientes = []
    contas = []
    
    while True:
        opcao = menu()
        print()

        if opcao == "d":
            print("============Depósito============")
            depositar(clientes)

        elif opcao == "s":
            print("=============Saque==============")
            sacar(clientes)

        elif opcao == "e":
            exibir_extrato(clientes)

        elif opcao == "nu":
            criar_cliente(clientes)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("\nOperação inválida, por favor selecione novamente a operação desejada.")

# =================== APLICAÇÃO ===================

main()
