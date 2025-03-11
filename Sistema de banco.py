from datetime import datetime

#Estrutura para armazenar dados
usuarios = []
contas =[]

#função para criar usuario
def criar_usuario(nome, data_nascimento, cpf, endereco):
    #validando CPF
    cpf = cpf.replace(".", "").replace("-", "")
    if not cpf.isdigit() or len(cpf) != 11:
        print ("Erro:Cpf Inválido!")
        return None

    #verificar se o cpf ja existe
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            print ("Erro: CPF já cadastrado!")
            return None
    usuario ={
        'nome' : nome,
        'data_de_nascimento' : data_nascimento,
        'cpf' : cpf,
        'endereco' : endereco
    }
    usuarios.append(usuario)
    print(f"Usuário {nome} cadastrado com sucesso!")
    return usuario
#função para criar conta corrente
def criar_conta(usuario):
    #Sequencial
    numero_conta = len(contas) + 1
    agencia = "00001"
    conta = {
        'agencia': agencia,
        'numero_conta': numero_conta,
        'usuario': usuario
    }
    contas.append(conta)
    print(f"Conta {numero_conta} criado com sucesso!")
    return conta
#função de deposito
def deposito(saldo, valor):
    if valor <= 0:
        print("Operação falhou! O valor informado deve ser maior que zero.")
        return saldo
    saldo += valor
    data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    print(f"[{data_hora}] Depósito de R$ {valor:.2f} realizado com sucesso!")
    return saldo
#função extrato
def extrato(extrato, *, saldo):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

#função saque
def realizar_saque(*, saldo, valor, limite, numero_saque, limite_saque):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saque >= limite_saque

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        numero_saque += 1
        print(f"Saque realizado com sucesso! Saldo atual: R$ {saldo:.2f}")
        return saldo, numero_saque, True
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, numero_saque, False
#Menu de opções
menu = """

[a] Cadastrar usuário
[b] Criar conta corrente
[c] Depositar
[d] Sacar
[e] Extrato
[f] Relatório Resumido
[g] Sair

 """

saldo = 0
limite = 500
extrato_registro = ""
numero_saques = 0
limite_saques = 3
numero_transacoes = 0
limite_transacoes = 10
ultima_data = datetime.now().strftime("%d/%m/%Y")


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
        nome = input("Informe o nome: ")
        data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ")
        cpf = input("Informe o CPF: ").replace(".", "").replace("-", "")
        endereco = input("Informe o endereço (logradouro, numero, bairro, cidade, estado): ")

        usuario = criar_usuario(nome, data_nascimento, cpf, endereco)

    elif opcao == "b":
        if len(usuarios) == 0:
            print("Nenhum usuário cadastrado. Cadastre um usuário primeiro.")
            continue
        cpf = input("Informe o CPF do usuário para criar a conta: ").replace(".", "").replace("-", "")
        usuario = next((u for u in usuarios if u['cpf'] == cpf), None)
        if usuario is None:
            print("Usuário não encontrado!")
            continue
        criar_conta(usuario)

    elif opcao == "c":
        valor = float(input("Informe o valor do depósito: "))
        saldo = deposito(saldo, valor)

    elif opcao == "d":
        valor = float(input("Informe o valor do saque: "))
        saldo, numero_saques, sucesso = realizar_saque(saldo=saldo, valor=valor, limite=limite, numero_saque=numero_saques, limite_saque=limite_saques)

    elif opcao == "e":
        extrato(extrato=extrato_registro, saldo=saldo)

    elif opcao == "f":
        print(f"Contas cadastradas: {len(contas)}")
        print(f"Usuários cadastrados: {len(usuarios)}")

    elif opcao == "g":
        print("Saindo... Obrigado por utilizar nosso banco!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
