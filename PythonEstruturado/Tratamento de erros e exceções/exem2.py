#Tratamento com Loop

while True:
    try: #"Tente isso"
        nr = int(input('digite um número:'))
        s = nr * 3
        print (s)
        q = 12/ s
        print(q)
        break
    except ValueError: #Erro de valor
        print('Entre com um número válido')