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
LIMITE_SAQUES = 5

def deposito(saldo, extrato):
    valor = float(input("Entre com o valor do deposito: "))

    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Valor Inválido")

    print(f"Novo Saldo: {saldo}")
    return saldo, extrato

while True:

    opcao = input(menu)

    if opcao == "1":
        saldo, extrato = deposito(saldo, extrato)

    elif opcao == "2":
        print("Sacar")

    elif opcao == "3":
        print("Visualizar Extrato")

    elif opcao == "0":
        print("Finalizando Programa!!")
        break

    else:
        print("Opção inválida, por favor selecione uma operação válida!!")