def calcula_imc (peso, altura):
    return  peso * 100 / (altura * 2)

peso = eval(input('Digite o seu peso em quilos: '))
altura = eval(input('Digite sua altura em centimetros: '))
calcula_imc(peso, altura)
imc = calcula_imc(peso, altura)
print('imc =', imc)