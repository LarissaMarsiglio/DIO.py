from datetime import datetime

menu = """

[a] Depositar
[b] Sacar
[c] Extrato
[d] Relatório Resumido
[e] Extrato por Data
[f] Sair

 """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3
numero_transacoes = 0
limite_transacoes = 10
ultima_data = datetime.now().strftime("%d/%m/%Y")
nome_usuario = input("Informe seu nome para cadastrar a conta: ")

print(f"\nBem vindo(a), {nome_usuario}! Sua conta foi criada com sucesso.")

while True:

    opcao = input(menu)

    data_atual = datetime.now().strftime("%d/%m/%Y")
    if data_atual != ultima_data:
        numero_transacoes = 0
        ultima_data = data_atual

    if numero_transacoes >= limite_transacoes:
        print ("Operacao falhou! Numero máximo de transções atingido")
        continue

    if opcao == "a":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            extrato += f"Depósito: R$ {valor:.2f}\n"
            numero_transacoes += 1
            print(f"Depósito realizado com sucesso! Saldo atual: R$ {saldo:.2f}")
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "b":
        valor = float(input("Informe o valor do saque: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= limite_saques

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
        elif valor > 0:
            saldo -= valor
            numero_saques += 1
            numero_transacoes += 1
            data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            extrato += f"[{data_hora}] Saque: R$ {valor:.2f}\n"
            print(f"Saque realizado com sucesso! Saldo atual: R$ {saldo:.2f}")
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "c":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "d":
        print("\n========== RELATÓRIO RESUMIDO ============")
        print(f"Saldo atual: R$ {saldo:.2f}")
        print(f"Número de saques realizados: {numero_saques}")
        print(f"Número de transações realizadas hoje: {numero_transacoes}")
        print("==========================================")      
    elif opcao == "e":
        data_filtro = input ("Informe a data (dd/mm/aaaa) para ver o extrato: ")
        print("\n======= EXTRATO DO DIA {data_filtro} =======")
        extrato_dia = [linha for linha in extrato.split('\n') if linha.startswith(f"[{data_filtro}")]
        print("\n".join(extrato_dia) if extrato_dia else "Não há transações nessa data.")
        print("==========================================")

    elif opcao == "f":
        print("Saindo.. Obrigado por utilizar nosso monopolio!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")