menu = """
[1] Cadastrar Conta
[2] Desativar Conta
[3] Cadastrar Usuário
[4] Operações bancárias
[5] Sair
"""

menu1 = """
[1] Depósito
[2] Saque
[3] Extrato
[4] Sair
"""

contas = []
usuarios = []
saldo = 0
saldo_deposito = 0
saldo_saque = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

def Deposito(valor_deposito, extrato):
    global saldo
    saldo += valor_deposito
    valor_deposito1 = "{:.2f}".format(valor_deposito)
    extrato.append("Depósito de R$" + valor_deposito1)
    return saldo, extrato

def Saque(valor_saque, extrato):
    global saldo, LIMITE_SAQUES
    if LIMITE_SAQUES == 0:
        print("Você já atingiu o limite diário de saques.")
    elif valor_saque > limite:
        print("O valor do saque não pode exceder o limite de R$500,00.")
    elif valor_saque > saldo:
        print("Você não possui saldo suficiente para realizar esta operação.")
    else:
        saldo -= valor_saque
        LIMITE_SAQUES -= 1
        valor_saque1 = "{:.2f}".format(valor_saque)
        extrato.append("Saque de R$" + valor_saque1)
    return saldo, extrato

def Gerar_extrato(saldo, extrato):
    for extratos in extrato:
        print(extratos)
    print(f"Seu saldo atual é: R$ {saldo:.2f}")
    return saldo, extrato

while True:
    opcao = input(menu)

    if opcao == "1":
        conta_cpf = input("Digite o CPF do cliente: ")
        if conta_cpf not in [cliente["cpf"] for cliente in usuarios]:
            print("O CPF digitado não está cadastrado, por favor cadastre o cliente")
        else:
            conta_agencia = "0001"
            conta_numero = len(contas) + 1
            status_conta = "Ativo"
            contas.append({"numero": conta_numero, "agencia": conta_agencia, "cpf": conta_cpf, "status": status_conta})
            print("Conta Cadastrada com sucesso")

    elif opcao == "2":
        conta_desativ = int(input("Digite o número da conta que deseja desativar: "))
        for conta in contas:
            if conta_desativ == conta["numero"]:
                conta ["status"] = "Inativo"
                print("Inativação da conta realizada com sucesso")
                break
        else:
            print("A conta informada não existe")

    elif opcao == "3":
        cadastro_cpf = input("Digite o CPF do cliente: ")
        if cadastro_cpf in [cliente["cpf"] for cliente in usuarios]:
            print("O CPF digitado já está cadastrado")
        else:
            cadastro_nome = input("Digite o nome do cliente: ")
            cadastro_dn = input("Digite a data de nascimento do cliente: ")
            cadastro_end = input("Digite o endereço do cliente: ")
            usuarios.append({"cpf": cadastro_cpf, "nome": cadastro_nome, "data_nascimento": cadastro_dn, "endereco": cadastro_end})
            print("Usuário cadastrado com sucesso")

    elif opcao == "4":
        while True:
            opcao1 = input(menu1)
            if opcao1 == "1":
                valor_deposito = float(input("Digite o valor que deseja depositar: "))
                if valor_deposito < 1:
                    print("O valor depositado não pode ser 0 ou negativo")
                else:
                    Deposito(valor_deposito, extrato)
                    print("Depósito realizado com sucesso!")

            elif opcao1 == "2":
                valor_saque = float(input("Digite o valor que deseja sacar: "))
                Saque(valor_saque, extrato)

            elif opcao1 == "3":
                Gerar_extrato(saldo, extrato)
            
            elif opcao1 == "4":
                break
            
            else:
                print("Operação inválida, digite novamente a opção desejada")

    elif opcao == "5":
        break

    else:
        print("Operação inválida, digite novamente a opção desejada")
