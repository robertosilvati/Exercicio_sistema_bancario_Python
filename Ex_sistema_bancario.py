menu = """
Bem vindo ao Banco Python
========= Menu de opções =========
[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair
==================================
"""
from datetime import datetime
saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUE = 3

while True:
    print(menu)
    opcao = int(input("Selecione a sua opção aqui: "))
    if opcao == 1:
        deposito = float(input("Digite o valor do depósito: "))

        if deposito > 0:
            saldo += deposito
            print(f"Realizando depósito de R$ {deposito:.2f}")
            extrato.append((datetime.now(), deposito, "Deposito"))
        else:
            print("Valor inválido")

    elif opcao == 2:
        saque = float(input("Informe o valor de saque: "))

        if saque > 0 and saldo >= saque:
            if saque > limite:
                print("Operação falhou!!")
                print(f"limite é de R$ {limite:.2f} por saque.")
            elif numero_saques == LIMITE_SAQUE:
                print("Operação falhou!!!")
                print(f"Seu limite diario é de {LIMITE_SAQUE} saques.")
            else:
                saldo -= saque
                print(f"Realziando saque de {saque:.2f}")
                extrato.append((datetime.now(), saque, "Saque"))
                numero_saques += 1
        elif saque < 0:
            print(f"Valores negativos invalidos!!!")
        else:
            print("Seu saldo em conta insuficiente para sacar")
    elif opcao == 3:
        print("\n================== Extrato ==================\n")
        for historico in extrato:
            data_hora, valor, mensagem = historico
            print(f"{data_hora.strftime('%d-%m-%Y %H:%M:%S')} {mensagem:10} R$ {valor:.2f}")
        print("\n=============================================")
        print(f"Saldo atual R$ {saldo:.2f}")
        

    elif opcao == 0:
        print("Saindo do sistema ")
        break
    else:
        print("Opção invalida, seleciona uma das opção do menu")