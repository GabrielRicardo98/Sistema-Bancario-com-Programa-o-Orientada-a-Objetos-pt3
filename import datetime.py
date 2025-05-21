import datetime

class ContaBancaria:
    """
    Representa uma conta bancária com saldo e histórico de transações.
    """

    def __init__(self, numero_conta, saldo_inicial=0, extrato_inicial=None):
        self._numero_conta = numero_conta
        self.saldo = saldo_inicial
        self.extrato = extrato_inicial if extrato_inicial is not None else []

    def consultar_saldo(self):
        """Exibe o saldo atual da conta."""
        print(f"Seu saldo atual é: R$ {self.saldo:.2f}")

    def depositar(self, valor):
        """Realiza uma operação de depósito na conta."""
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
        except ValueError:
            print("Erro: Valor inválido. Por favor, digite um número.")

    def sacar(self, valor):
        """Realiza uma operação de saque na conta."""
        try:
            valor_saque = float(valor)
            if valor_saque <= 0:
                print("Valor de saque inválido. Digite um número positivo.")
                return
            if valor_saque > self.saldo:
                print("Saldo insuficiente para realizar o saque.")
                return
            self.saldo -= valor_saque
            agora = datetime.datetime.now()
            self.extrato.append({
                "data_hora": agora.strftime("%d/%m/%Y %H:%M:%S"),
                "tipo": "Saque",
                "valor": valor_saque
            })
            print(f"Saque de R$ {valor_saque:.2f} realizado com sucesso.")
        except ValueError:
            print("Erro: Valor inválido. Por favor, digite um número.")

    def exibir_extrato(self):
        """Exibe o extrato das transações."""
        print(f"Extrato da conta {self._numero_conta}:")
        if not self.extrato:
            print("Nenhuma transação registrada.")
        else:
            for transacao in self.extrato:
                print(f"{transacao['data_hora']} - {transacao['tipo']}: R$ {transacao['valor']:.2f}")
        print(f"Saldo atual: R$ {self.saldo:.2f}")

# Exemplo de uso
if __name__ == "__main__":
    conta1 = ContaBancaria(numero_conta="12345-X", saldo_inicial=1000.0)
    conta2 = ContaBancaria(numero_conta="67890-Y")

    conta1.consultar_saldo()
    conta1.depositar(500)
    conta1.sacar(300)
    conta1.exibir_extrato()

    conta2.consultar_saldo()
    conta2.depositar(150)
    conta2.exibir_extrato()
