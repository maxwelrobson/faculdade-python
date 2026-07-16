#capturando o tipo da execeção

while True:
    try:
        nr = int(input('digite um número:'))
        s = nr * 3
        print(s)
        q = 12 / s
        print(q)
        break
    except ValueError: #Tratamento para o valor digitado
        print('Entre com um número válido')
    except ZeroDivisionError: #Tratamento para divisão por zero
        print('0 número não pode ser zero')