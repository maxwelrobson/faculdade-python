#métodos com retorno
#serve para validar o estado de um objeto

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
    conta1 = Conta(1,123,'João', 1000)
    valor_saque = 200
    resultado_saque = conta1.sacar(valor_saque)

    print(f"Conta {conta1.numero}")

    #validando o retorno para verificar se o saque foi realizado
    if resultado_saque:
        print(f"Saque de R$ {valor_saque} realizado com sucesso!")
        print(f"Saldo atual: R$ {conta1.saldo}\n")
    else:
        print("Saldo insuficiente para realizar o saque.\n")

    conta2 = Conta(2, 123, 'João', 100)
    valor_saque = 200
    resultado_saque = conta2.sacar(valor_saque)

    print(f"Conta {conta2.numero}")

    # validando o retorno para verificar se o saque foi realizado
    if resultado_saque:
        print(f"Saque de R$ {valor_saque} realizado com sucesso!")
        print(f"Saldo atual: R$ {conta2.saldo}")
    else:
        print("Saldo insuficiente para realizar o saque.\n")



if __name__ == "__main__":
    main()