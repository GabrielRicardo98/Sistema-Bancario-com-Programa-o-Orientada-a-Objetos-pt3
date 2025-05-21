import datetime

class ContaBancaria:
    def __init__(self, numero_conta, saldo_inicial=0, extrato_inicial=None):
        self._numero_conta = numero_conta
        self.saldo = saldo_inicial
        self.extrato = extrato_inicial if extrato_inicial is not None else []

    def consultar_saldo(self):
        print(f"Conta {self._numero_conta} - Saldo: R$ {self.saldo:.2f}")

    def depositar(self, valor):
        try:
            valor_deposito = float(valor)
            if valor_deposito <= 0:
                print("Valor de depósito inválido.")
                return
            self.saldo += valor_deposito
            agora = datetime.datetime.now()
            self.extrato.append({
                "data_hora": agora.strftime("%d/%m/%Y %H:%M:%S"),
                "tipo": "Depósito",
                "valor": valor_deposito
            })
            print(f"Depósito de R$ {valor_deposito:.2f} na conta {self._numero_conta} realizado.")
        except ValueError:
            print("Erro: Valor inválido.")

    def sacar(self, valor):
        try:
            valor_saque = float(valor)
            if valor_saque <= 0:
                print("Valor de saque inválido.")
                return
            if valor_saque > self.saldo:
                print("Saldo insuficiente.")
                return
            self.saldo -= valor_saque
            agora = datetime.datetime.now()
            self.extrato.append({
                "data_hora": agora.strftime("%d/%m/%Y %H:%M:%S"),
                "tipo": "Saque",
                "valor": valor_saque
            })
            print(f"Saque de R$ {valor_saque:.2f} na conta {self._numero_conta} realizado.")
        except ValueError:
            print("Erro: Valor inválido.")

    def exibir_extrato(self):
        print(f"\nExtrato da conta {self._numero_conta}:")
        if not self.extrato:
            print("Nenhuma transação registrada.")
        else:
            for transacao in self.extrato:
                print(f"{transacao['data_hora']} - {transacao['tipo']}: R$ {transacao['valor']:.2f}")
        print(f"Saldo final: R$ {self.saldo:.2f}\n")

# Classe adicional para gerenciar múltiplas contas
class Banco:
    def __init__(self):
        self.contas = {}

    def adicionar_conta(self, numero_conta, saldo_inicial=0):
        if numero_conta in self.contas:
            print("Conta já existe.")
        else:
            self.contas[numero_conta] = ContaBancaria(numero_conta, saldo_inicial)
            print(f"Conta {numero_conta} criada com sucesso.")

    def acessar_conta(self, numero_conta):
        return self.contas.get(numero_conta, None)

    def listar_contas(self):
        print("\nContas cadastradas:")
        for numero in self.contas:
            print(f"- {numero}")
        print()

# Uso
if __name__ == "__main__":
    banco = Banco()

    banco.adicionar_conta("12345-X", 1000)
    banco.adicionar_conta("67890-Y", 500)

    conta1 = banco.acessar_conta("12345-X")
    conta2 = banco.acessar_conta("67890-Y")

    conta1.depositar(200)
    conta1.sacar(150)
    conta1.exibir_extrato()

    conta2.depositar(300)
    conta2.sacar(100)
    conta2.exibir_extrato()

    banco.listar_contas()
