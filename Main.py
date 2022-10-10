from cProfile import label
from email.mime import image
from tkinter.font import Font
import pygame
from random import randrange
from tkinter import *

janela = Tk()

janela.title('Guess game')
janela.resizable(False, False)


imagebg = PhotoImage(file="bg.png")
bg = Label(janela, image=imagebg)
bg.grid(column=2, row=0)

frame1 = Frame(janela)
frame1.grid(column=0, row=0)
text1 = Label(
    frame1, text=""" Olá, vamos brincar? 
    Irei pensar em um número de 0 a 10. 
    Tente adivinhar""", justify=CENTER, font=("Gotham", "12"))
text1.grid(column=0, row=0)


def music():

    pygame.init()
    pygame.mixer.music.load("tema.mp3")
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1, 0, 1000)


def layout_game():

    music()

    text2 = Label(
        frame1, text="Em qual número eu estou pensando ?", justify=CENTER, font=("Gotham", "12"))
    text2.grid(column=0, row=7)

    data = StringVar()
    textbox = Entry(frame1, textvariable=data)
    textbox.grid(column=0, row=8)
    numero_aleatorio = 4
    # randrange(11)

    botão = Button(frame1, text='Guess', justify=CENTER, font=(
        "Gotham", "13", "bold"), command=lambda: guess(data, numero_aleatorio))
    botão.grid(column=0, row=10)


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
        Texto_resultado = Label(
            frame1, text='', justify=CENTER, font=("Gotham", "12", "bold"))
        Texto_resultado.grid(column=0, row=12)
        Texto_resultado["text"] = resposta
        return ()
    else:
        pygame.mixer.Sound.play(erro)
        resposta = 'Poxa, tente novamente'
        Texto_resultado = Label(
            frame1, text='', justify=CENTER, font=("Gotham", "12", "bold"))
        Texto_resultado.grid(column=0, row=12)
        Texto_resultado["text"] = resposta
        return ()


botão = Button(frame1, text='Jogar', justify=CENTER, font=(
    "Gotham", "13", "bold"), command=layout_game)
botão.grid(column=0, row=5)

textofinal = Label(janela, text='Desenvolvido por Gobis e Peu', font=(
    "Gotham", "8", "italic"))
textofinal.grid(column=2, row=15)
janela.mainloop()
