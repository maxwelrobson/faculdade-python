from tkinter import *

def funClicar():
    print("Botão pressionado")

janelaPrincipal = Tk()
texto = Label(master = janelaPrincipal, text = "Minha janela exibida")
texto.pack()

botao = Button(master = janelaPrincipal, text = 'Clique', command = funClicar)
botao.pack()

botao_fechar = Button(master = janelaPrincipal, text = 'Fechar', command = janelaPrincipal.destroy)
botao_fechar.pack()

janelaPrincipal.mainloop()
