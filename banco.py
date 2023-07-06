menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

#conta
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3

#Escolha das opções
while True:

    opcao = input(menu)

    if opcao == "d":
            valor = float(input('Qual o valor o senhor(a) deseja deposita: '))
            if valor > 0:
                saldo += valor
                extrato += f"Depósito: R$ {valor:.2f}\n"
            else:
                print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        print(f'Seu saldo é {saldo}')
        if saldo > 0:
            saque = int(input('Qual valor deseja retira? R$ '))
            if saque <= saldo:
                if saque < limite:
                    if numero_saques < limite_saques:
                        if saque <= limite:
                            saldo = saldo - saque
                            numero_saques = numero_saques + 1
                            extrato += f"Saque: R$ {saque:.2f}\n"
                    else:
                        print('Operação falhou! Você excedeu seu limite de 3 saques por dia')
                else:
                    print("Operação falhou! O valor do saque excede o limite.")
            else:
                print("Operação falhou! Você não tem saldo suficiente.")

    elif opcao == "e":
        print("\n========== EXTRATO =========")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo> R$ {saldo:.2f}")
        print("===================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada")