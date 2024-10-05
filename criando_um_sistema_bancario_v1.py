menu = """
[d] Depositar
[s] Sacar
[e] Visualizar Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_deposito = 1
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        print("\n===========Depósito===========\n")
        while True:
            valor_deposito = float(input("=> "))

            if valor_deposito > 0.0:
                saldo += valor_deposito
                extrato += f"Depósito {numero_deposito}: R$ {valor_deposito:.2f}\n"
                numero_deposito += 1
                print("Valor depositado com sucesso!\n")
                print("==============================")
                break
            else:
                print("Valor inválido! Deposite apenas valores positivos.\n")

    elif opcao == "s":
        print("\n============Saque============\n")

        if numero_saques < LIMITE_SAQUES:
                valor_saque = float(input("=> "))

                if saldo >= valor_saque:
                    if valor_saque <= 500:
                        saldo -= valor_saque
                        extrato += f"Saque {numero_saques+1}:    R$ {valor_saque:.2f}\n"
                        numero_saques += 1
                        print("Valor sacado com sucesso!\n")
                        print("=============================")
                    else:
                        print("Valor acima do limite de R$ 500.00 por saque! Operação cancelada.")
                else:
                    print("Saldo insuficiente! Operação cancelada.\n")
                    print("=============================")
        else:
            print("Limite máximo de 3 saques por dia atingido!\n")
            print("=============================")
    
    elif opcao == "e":
        print("\n============Extrato============\n")

        if numero_deposito == 1 and numero_saques == 0:
            print("Não foram realizadas movimentações.\n")
            print("===============================")
        else:
            print(extrato)
            print(f"Saldo atual: R$ {saldo:.2f}\n")
            print("===============================")
    
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
