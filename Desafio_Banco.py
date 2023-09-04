menu = """

[1]Deposito
[2]Saque
[3]Extrato
[4]Sair

"""

saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":

        valor_deposito = float(input("Digite o valor que deseja depositar:"))

        if valor_deposito < 1:
            print("O valor depositado não pode ser 0 ou negativo")

        else:    
            saldo += valor_deposito
            valor_deposito1 = "{:.2f}".format(valor_deposito)
            extrato.append("Deposito de R$" + str(valor_deposito1))
            print("Deposito realizado com sucesso!")

    elif opcao == "2":
        valor_saque = float(input("Digite o valor que deseja sacar:"))

        if LIMITE_SAQUES == 0 :
            print("Você já realizou o número de saques diários máximo, por favor repita a operação amanhã.")     

        else:
            if valor_saque > limite :
                print("O valor do saque não pode exceder o limite de R$500,00.")

            else:
                if valor_saque > saldo :
                    print("Você não possui saldo suficiente para realizar essa operação.")
                
                else:
                    saldo -= valor_saque
                    LIMITE_SAQUES -= 1    
                    valor_saque1 = "{:.2f}".format(valor_saque)
                    extrato.append("Saque de R$" + str(valor_saque1))
                    print("Saque realizado com sucesso")
            
    elif opcao == "3":
        for extratos in extrato:
            print(extratos)
            
        print(f"Seu saldo atual é: R$ {saldo:.2f}") 

    elif opcao == "4":
        break

    else:
        print("Operação inválida, difite novamente a opção desejada")        