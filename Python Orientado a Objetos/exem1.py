#criando classe
class Conta:
    def __init__(self, numero, cpf, nomeTitulas,saldo):
        self.numero = numero
        self.cpf = cpf
        self.nomeTitulas = nomeTitulas
        self.saldo = saldo

#instanciando um objeto conta
class Conta:
    def __init__(self, numero, cpf, nomeTitular, saldo):
        self.numero = numero
        self.cpf = cpf
        self.nomeTitular = nomeTitular
        self.saldo = saldo

#observe os parametros passados na criação do objeto
def main():
    c1 = Conta(1, 1,"Joao",1000)
    print(f"Nome do titular da conta: {c1.nomeTitular}")
    print(f"Número da conta: {c1.numero}")
    print(f"CPF do titular da conta: {c1.cpf}")
    print(f"Saldo da conta: {c1.saldo}")

# Nesse caso, a condicao do IF a seguir sera TRUE.
# Então o que está no corpo do IF será executado. No caso,
# é um chamado ao metodo main do script

if __name__ == "__main__":
    main()
