import pygame
from random import randrange
from tkinter import *

janela = Tk()
janela.title('Guess game')

text1 = Label(janela, text="""
======================================================

Olá, vamos brincar?
Irei pensar em um número de 0 a 10. Tente adivinhar

======================================================
    """, justify=CENTER)
text1.grid(column=0, row=0)


def music():

    pygame.init()
    pygame.mixer.music.load("tema.mp3")
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1, 0, 1000)


def layout_game():

    music()

    text2 = Label(
        janela, text="Em qual número eu estou pensando ?", justify=CENTER)
    text2.grid(column=0, row=3)

    data = StringVar()
    textbox = Entry(janela, textvariable=data)
    textbox.grid(column=0, row=4)
    numero_aleatorio = randrange(11)

    botão = Button(janela, text='guess', justify=CENTER,
                   command=lambda: guess(data, numero_aleatorio))
    botão.grid(column=0, row=5)


def guess(data, numero_aleatorio):

    erro = pygame.mixer.Sound("erro.mp3")
    vitoria = pygame.mixer.Sound("vitoria.mp3")
    pygame.mixer.Sound.set_volume(erro, 0.05)
    pygame.mixer.Sound.set_volume(vitoria, 0.05)

    numero_usuario = int(data.get())
    print(numero_aleatorio)
    if numero_aleatorio == numero_usuario:
        pygame.mixer.Sound.play(vitoria)
        resposta = """
        Parabéns!! Você acertou. O número que eu estou pensando é {}""".format(numero_aleatorio)
        pygame.mixer.music.fadeout(10000)
        pygame.mixer.music.set_volume(0.2)
        Texto_resultado = Label(janela, text='', justify=CENTER)
        Texto_resultado.grid(column=0, row=8)
        Texto_resultado["text"] = resposta
        return ()
    else:
        pygame.mixer.Sound.play(erro)
        resposta = 'Poxa, tente novamente'
        Texto_resultado = Label(janela, text='', justify=CENTER)
        Texto_resultado.grid(column=0, row=8)
        Texto_resultado["text"] = resposta
        return ()


botão = Button(janela, text='Começar!', justify=CENTER, command=layout_game)
botão.grid(column=0, row=1)


janela.mainloop()
