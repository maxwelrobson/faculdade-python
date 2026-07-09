print("antes while")
palavra = input("Entre com uma palavra:")
while palavra != "sair":
    print("dentro while")
    palavra = input("Digite sair para encerrar o laço:")
print("Você digitou sair e agora está fora do laço")