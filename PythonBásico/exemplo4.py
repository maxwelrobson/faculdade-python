#Defina as variáveis para representar o preço de cada item do menu do restaurante.
#Solicite ao usuário que insira a quantidade de cada item que deseja pedir.
#Calcule o preço total do pedido, multiplicando o preço de cada item pela quantidade escolhida pelo usuário.
#Exiba o preço total do pedido para o usuário.

hamburguer = 10.50
batata_frita = 4.00
refrigerante = 3.00

quant_hamburguer = int(input("Digite a quantidade de hambúrgueres desejados: "))
quant_batata = int(input("Digite a quantidade de batatas fritas desejadas: "))
quant_refrigerante = int(input("Digite a quantidade de refrigerantes desejados: "))

preco_total = (hamburguer * quant_hamburguer) + (batata_frita * quant_batata) + (refrigerante * quant_refrigerante)

print("O preço total do seu pedido é: R$", preco_total)