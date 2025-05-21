import datetime
import json

class ContaBancaria:
    def __init__(self, numero_conta, saldo_inicial=0, extrato_inicial=None):
        self.saldo = saldo_inicial
        self.numero_conta = numero_conta
        self.extrato = extrato_inicial if extrato_inicial is not None else []

    def consultar_saldo(self):
        print(f"Seu saldo atual é: R$ {self.saldo:.2f}")

    def depositar(self, valor):
        try:
            valor_deposito = float(valor)
            if valor_deposito <= 0:
                print("Valor de depósito inválido. Digite um número positivo.")
                return
            self.saldo += valor_deposito
            agora = datetime.datetime.now()
            self.extrato.append({
                "data_hora": agora.strftime("%d/%m/%Y %H:%M:%S"),
                "tipo": "Depósito",
                "valor": valor_deposito
            })
            print(f"Depósito de R$ {valor_deposito:.2f} realizado com sucesso.")
            print(f"Seu novo saldo é: R$ {self.saldo:.2f}")
        except ValueError:
            print("Valor inválido para depósito. Por favor, digite um número.")

    def sacar(self, valor):
        try:
            valor_saque = float(valor)
            if valor_saque <= 0:
                print("Valor de saque inválido. Digite um número positivo.")
                return
            if valor_saque <= self.saldo:
                self.saldo -= valor_saque
                agora = datetime.datetime.now()
                self.extrato.append({
                    "data_hora": agora.strftime("%d/%m/%Y %H:%M:%S"),
                    "tipo": "Saque",
                    "valor": valor_saque
                })
                print(f"Saque de R$ {valor_saque:.2f} realizado com sucesso.")
                print(f"Seu novo saldo é: R$ {self.saldo:.2f}")
            else:
                print("Saldo insuficiente.")
        except ValueError:
            print("Valor inválido para saque. Por favor, digite um número.")

    def exibir_extrato(self):
        if not self.extrato:
            print("Não foram realizadas transações.")
        else:
            print("\n--- Extrato Bancário ---")
            for transacao in self.extrato:
                print(f"{transacao['data_hora']} - {transacao['tipo']}: R$ {transacao['valor']:.2f}")
            print(f"Saldo atual: R$ {self.saldo:.2f}")

    def transferir(self, conta_destino, valor):
        try:
            valor_transferencia = float(valor)
            if valor_transferencia <= 0:
                print("Valor de transferência inválido. Digite um número positivo.")
                return
            if not isinstance(conta_destino, ContaBancaria):
                print("Erro: A conta de destino não é válida.")
                return
            if valor_transferencia <= self.saldo:
                self.saldo -= valor_transferencia
                agora = datetime.datetime.now()
                self.extrato.append({
                    "data_hora": agora.strftime("%d/%m/%Y %H:%M:%S"),
                    "tipo": f"Transferência para {conta_destino.numero_conta}",
                    "valor": valor_transferencia
                })
                print(f"Transferência de R$ {valor_transferencia:.2f} para conta {conta_destino.numero_conta} realizada com sucesso.")
                print(f"Seu novo saldo é: R$ {self.saldo:.2f}")
                conta_destino.depositar(valor_transferencia)
            else:
                print("Saldo insuficiente para realizar a transferência.")
        except ValueError:
            print("Valor inválido para transferência. Por favor, digite um número.")

def salvar_dados(conta, filename="banco_dados.json"):
    dados = {
        "numero_conta": conta.numero_conta,
        "saldo": conta.saldo,
        "extrato": conta.extrato
    }
    with open(filename, "w") as f:
        json.dump(dados, f, indent=4)
    print(f"Dados da conta {conta.numero_conta} salvos com sucesso!")

def carregar_dados(filename="banco_dados.json"):
    try:
        with open(filename, "r") as f:
            dados = json.load(f)
            return ContaBancaria(dados["numero_conta"], dados["saldo"], dados["extrato"])
    except FileNotFoundError:
        print("Arquivo de dados não encontrado. Criando nova conta com número padrão '00000-0'.")
        return ContaBancaria("00000-0")

def menu_interativo():
    print("\n--- Olá! Bem-vindo ao seu banco virtual. ---")
    print("1 - Consultar Saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Exibir Extrato")
    print("5 - Transferir")
    print("6 - Sair")
    print("------------------------------------------")

def executar_comandos_simulados(comandos):
    minha_conta = carregar_dados()
    outra_conta = carregar_dados(filename="banco_secundario.json")
    if outra_conta.numero_conta == "00000-0":
        outra_conta.numero_conta = "54321-X"

    for comando in comandos:
        opcao = comando.get("opcao")
        valor = comando.get("valor")

        if opcao == 1:
            minha_conta.consultar_saldo()
        elif opcao == 2:
            minha_conta.depositar(valor)
        elif opcao == 3:
            minha_conta.sacar(valor)
        elif opcao == 4:
            minha_conta.exibir_extrato()
        elif opcao == 5:
            print(f"\nRealizando transferência da conta {minha_conta.numero_conta} para {outra_conta.numero_conta}")
            minha_conta.transferir(outra_conta, valor)
        elif opcao == 6:
            salvar_dados(minha_conta)
            salvar_dados(outra_conta, filename="banco_secundario.json")
            print("Obrigado por utilizar nosso banco virtual!")
            break
        else:
            print("Opção inválida. Por favor, digite um número entre 1 e 6.")

if __name__ == "__main__":
    # Exemplo de comandos simulados para testar o código em ambientes sem input()
    comandos_teste = [
        {"opcao": 2, "valor": "100.00"},
        {"opcao": 1},
        {"opcao": 3, "valor": "50.00"},
        {"opcao": 4},
        {"opcao": 5, "valor": "25.00"},
        {"opcao": 6}
    ]
    executar_comandos_simulados(comandos_teste)

