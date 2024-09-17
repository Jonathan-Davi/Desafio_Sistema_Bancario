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

while True:

    opcao = input(menu)

    if opcao == "1":
        print("Depositar")

    elif opcao == "2":
        print("Sacar")

    elif opcao == "3":
        print("Visualizar Extrato")

    elif opcao == "0":
        print("Finalizando Programa!!")
        break

    else:
        print("Opção inválida, por favor selecione uma operação válida!!")