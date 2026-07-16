#uso de else e finaly


# try:
#  Bloco 1
# except Exception1:
#  Bloco tratador para Exception1
# except Exception2:
#   Bloco tratador para Exception1
# ...
# else:
#   Bloco 2 – executado caso nenhuma exceção seja levantada
# finally:
#   Bloco 3 – executado independente do que ocorrer
# Instrução fora do try/except  

while True:
    try:
        nr = int(input('digite um número:'))
        s= nr * 3
        print(s)
        q = 12 /s
        print(q)
    except ValueError:
        print('Entre com um número válido')
    except ZeroDivisionError:
        print('0 número não pode ser zero')
    else:
        print('entrou no else') #Executa se não passar por nenhum except (porque é else)
        break
    finally:
        print('entrou no finally') #Sempre executa no final mesmo no except
