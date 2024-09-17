menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def deposito(saldo, extrato):
    valor = float(input("Entre com o valor do deposito: "))

    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Valor Inválido")

    print(f"\nNovo Saldo: {saldo}")
    return saldo, extrato

def sacar(saldo, extrato, numero_saques, LIMITE_SAQUES):
    valor = float(input("Entre com o valor do saque: "))

    if numero_saques >= LIMITE_SAQUES:
        print("\nNúmero de saques diários excedido!!")
        return saldo, extrato, numero_saques

    if valor > saldo:
        print("\nSaldo insuficiente!!")

    elif valor > 0 and valor <= limite:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"\nSaque de R$ {valor:.2f} realizado com sucesso!")

    else:
        print("\nNão foi possível realizar o saque!!")

    print(f"Novo saldo: R$ {saldo:.2f}")
    return saldo, extrato, numero_saques

def ext(extrato):
    if extrato == "":
        print("Não foram realizadas movimentações!")

    else:
        return print(f"\n-===-Extrato da conta-===-\n{extrato}")


while True:

    opcao = input(menu)

    if opcao == "1":
        saldo, extrato = deposito(saldo, extrato)

    elif opcao == "2":
        saldo, extrato, numero_saques = sacar(saldo, extrato, numero_saques, LIMITE_SAQUES)

    elif opcao == "3":
        ext(extrato)

    elif opcao == "0":
        print("Finalizando Programa!!")
        break

    else:
        print("Opção inválida, por favor selecione uma operação válida!!")