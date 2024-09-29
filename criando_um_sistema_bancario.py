# =================== MÓDULOS ===================
import textwrap

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

def depositar(saldo, valor_deposito, extrato, numero_deposito, /):
    
    if valor_deposito > 0.0:
        saldo += valor_deposito
        extrato += f"Depósito {numero_deposito +1}:\tR$ {valor_deposito:.2f}\n"
        numero_deposito += 1
        print("Valor depositado com sucesso!")
    else:
        print("Valor inválido! Operação cancelada.")

    return saldo, extrato, numero_deposito

def sacar(*, saldo, valor_saque, extrato, limite_valor_saque, numero_saques, limite_numero_saques):
    
    # Excessões para não realizar o saque
    excedeu_numero_saques = numero_saques >= limite_numero_saques  # True ou False
    excedeu_valor_limite = valor_saque > limite_valor_saque  # True ou False
    excedeu_saldo = valor_saque > saldo # True ou False
        
    if excedeu_numero_saques:
        print("Limite máximo de 3 saques por dia atingido!")
    
    elif excedeu_valor_limite:
        print(f"Valor acima do limite de R$ {limite_valor_saque:.2f} por saque! Operação cancelada.")
    
    elif excedeu_saldo:
        print("Saldo insuficiente! Operação cancelada.")
        
    elif valor_saque > 0.0:
        saldo -= valor_saque
        extrato += f"Saque {numero_saques +1}:\tR$ {valor_saque:.2f}\n"
        numero_saques += 1
        print("Valor sacado com sucesso!")

    else: # Caso o usuário tente sacar um valor menor ou igual a 0
        print("Valor informado inválido! Operação cancelada.")
    
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato):

    print("============Extrato=============")
    print("Não foram realizadas movimentações.\n" if not extrato else extrato) # if ternário
    print(f"Saldo atual:\tR$ {saldo:.2f}")
    print("================================")

def criar_usuario(usuarios):
    cpf = input("Digite seu CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("CPF já cadastrado! Operação cancelada.")
        return
    
    nome = input("Digite seu nome completo: ")
    data_nascimento = input("Digite sua data de nascimento (dd-mm-aaaa): ")
    endereco = input("Digite seu endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Cadastro realizado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    # Compreensão de Listas
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
#                        [Retorno][        iteração       ][        Filtro        ]

    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Digite seu CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso!")

        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("Usuário não cadastrado! Faça o cadastro antes de criar uma conta.")

def listar_contas(contas):

    if contas:
        for conta in contas:
            linha = f"""\
            Agência:\t{conta["agencia"]}
            C/C:\t\t{conta["numero_conta"]}
            Titular:\t{conta["usuario"]["nome"]}
            """
            print("=" * 32)
            print(textwrap.dedent(linha))
    else:
        print("Nenhuma conta cadastrada!")

def main():
    LIMITE_NUMERO_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite_valor_saque = 500
    extrato = ""
    numero_saques = 0
    numero_deposito = 0
    usuarios = []
    contas = []
    
    while True:

        opcao = menu()
        print()

        # DEPÓSITO
        if opcao == "d":
            print("============Depósito============")

            valor_deposito = float(input("=> "))

            saldo, extrato, numero_deposito = depositar(saldo, valor_deposito, extrato, numero_deposito)

        # SAQUE
        elif opcao == "s":
            print("=============Saque==============")

            valor_saque = float(input("=> "))

            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor_saque=valor_saque,
                extrato=extrato,
                limite_valor_saque=limite_valor_saque,
                numero_saques=numero_saques,
                limite_numero_saques=LIMITE_NUMERO_SAQUES
            )

        # EXTRATO
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        # CRIAR NOVO USUÁRIO
        elif opcao == "nu":
            criar_usuario(usuarios)

        # CRIAR NOVA CONTA
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        # LISTAR CONTAS
        elif opcao == "lc":
            listar_contas(contas)

        # FINALIZAR PROGRAMA
        elif opcao == "q":
            break

        # MENSAGEM DE ERRO
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


# =================== APLICAÇÃO ===================
main()
