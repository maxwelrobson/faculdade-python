#Comunicação entre objetos na memória

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

    def gerar_extrato(self):
        print(f"numero: {self.numero} \n cpf: {self.cpf} \n saldo: {self.saldo}" )

def main():
    conta1 = Conta(1, 123, 'João', 0)
    conta2 = Conta(2, 456, 'Maria', 0)

    if (conta1 != conta2):
        print("endereços de memória diferentes")

    print(conta1)
    print(conta2)

    print(conta1.saldo)
    print(conta2.saldo)
    conta1.depositar(300)
    print(conta1.saldo)
    print(conta2.saldo)

    conta1 = conta2

    if(conta1 == conta2):
        ...
        print("Endereços iguais a memoria")

    print(conta1)
    print(conta2)

    print(conta1.saldo)
    print(conta2.saldo)
    conta1.depositar(1000)
    print(conta1.saldo)
    print(conta2.saldo)

if __name__ == "__main__":
    main()