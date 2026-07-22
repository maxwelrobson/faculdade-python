#tranferência entre contas

class Conta:
    def __init__(self, numero, cpf, nomeTitular, saldo):
        self.numero = numero
        self.cpf = cpf
        self.nomeTitular = nomeTitular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            return True

    def tranfereValor(self, contaDestino, valor):
        if self.saldo < valor:
            return ("Não exite saldo suficiente")
        else:
            contaDestino.depositar(valor)
            self.saldo -= valor
            return ("Transferência Realizada")

    def gerar_extrato(self):
        print(f"numero: {self.numero} \n cpf: {self.cpf} \n saldo: {self.saldo}" )

def main():
    conta1 = Conta(1, 123, 'João', 1000)
    conta2 = Conta(2, 456, 'Maria', 500)

    print('Saldo antes da transferência')
    print(f"Saldo da conta {conta1.numero}: R${conta1.saldo}")
    print(f"Saldo da conta {conta2.numero}: R${conta2.saldo}")

    conta1.tranfereValor(conta2, 300)
    print('Saldo após a tranferência')
    print(f"Saldo da conta {conta1.numero}: R${conta1.saldo}")
    print(f"Saldo da conta {conta2.numero}: R${conta2.saldo}")

if __name__ == "__main__":
    main()
