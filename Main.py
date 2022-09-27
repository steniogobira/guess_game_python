import pygame
from random import randrange
from time import sleep
from tkinter import *

# Janela representativa
janela = Tk()
janela.title('Guess game')

text1 = Label(janela, text="""
======================================================

Olá, vamos brincar?
Irei pensar em um número de 0 a 5. Tente adivinhar

======================================================
    """, justify=CENTER)
text1.grid(column=0, row=0)

# Criando função do jogo


def guess_game():

    text2 = Label(janela, text="Em qual número eu estou pensando ?",
                  justify=CENTER)
    text2.grid(column=0, row=2)

    data = StringVar()
    textbox = Entry(janela, textvariable=data)
    textbox.grid(column=0, row=4)
    n1 = (data.get())
    # Música
    pygame.init()
    pygame.mixer.music.load("tema.mp3")
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1, 0, 1000)

    # Efeitos sonoros
    erro = pygame.mixer.Sound("erro.mp3")
    vitoria = pygame.mixer.Sound("vitoria.mp3")
    pygame.mixer.Sound.set_volume(erro, 0.05)
    pygame.mixer.Sound.set_volume(vitoria, 0.05)

    # Escolhendo um número de 0 a 5
    a = randrange(6)
    sleep(3)

    def guess():

        # Condicionais.
        x = n1  # Chance 1
        if x == a:
            pygame.mixer.Sound.play(vitoria)
            resposta["text"] == 'Parabéns!! Você acertou. O número que eu estou pensando é {}'.format(
                a)
            resposta["text"] == 'Tchaaaau'
            pygame.mixer.music.fadeout(10000)
            pygame.mixer.music.set_volume(0.2)
            exit()
        else:
            pygame.mixer.Sound.play(erro)
            resposta["text"] = 'Poxa, tente novamente'

        x = n1  # Chance 2
        if x == a:
            pygame.mixer.Sound.play(vitoria)
            resposta["text"] = 'Parabéns!! Você acertou. O número que eu estou pensando é {}'.format(
                a)
            resposta["text"] = 'Tchaaaau'
            pygame.mixer.music.fadeout(10000)
            pygame.mixer.music.set_volume(0.2)
            sleep(10)
            exit()
        else:
            pygame.mixer.Sound.play(erro)
            resposta["text"] = 'Poxa, tente novamente'

        x = n1  # Chance 3
        if x == a:
            pygame.mixer.Sound.play(vitoria)
            resposta["text"] = 'Parabéns!! Você acertou. O número que eu estou pensando é {}'.format(
                a)
            resposta["text"] = 'Tchaaaau'
            pygame.mixer.music.fadeout(10000)
            pygame.mixer.music.set_volume(0.2)
            sleep(10)
            exit()
        else:
            pygame.mixer.Sound.play(erro)
            resposta["text"] = 'Poxa, tente novamente'

        x = n1  # Chance 4
        if x == a:
            pygame.mixer.Sound.play(vitoria)
            resposta["text"] = 'Parabéns!! Você acertou. O número que eu estou pensando é {}'.format(
                a)
            resposta["text"] = 'Tchaaaau'
            pygame.mixer.music.fadeout(10000)
            pygame.mixer.music.set_volume(0.2)
            sleep(10)
            exit()
        else:
            pygame.mixer.Sound.play(erro)
            resposta["text"] = 'Poxa, tente novamente'

        x = n1  # Chance 5
        if x == a:
            pygame.mixer.Sound.play(vitoria)
            resposta["text"] = 'Parabéns!! Você acertou. O número que eu estou pensando é {}'.format(
                a)
            resposta["text"] = 'Tchaaaau'
            pygame.mixer.music.fadeout(10000)
            pygame.mixer.music.set_volume(0.2)
            sleep(10)
            exit()
        else:
            pygame.mixer.Sound.play(erro)
            resposta["text"] = 'Poxa, tente novamente'

        x = n1  # Chance 6
        if x == a:
            pygame.mixer.Sound.play(vitoria)
            resposta["text"] = 'Parabéns!! Você acertou. O número que eu estou pensando é {}'.format(
                a)
            resposta["text"] = 'Tchaaaau'
            pygame.mixer.music.fadeout(10000)
            pygame.mixer.music.set_volume(0.2)
            sleep(10)
            exit()
        else:
            pygame.mixer.Sound.play(erro)
            pygame.mixer.music.fadeout(30000)
            pygame.mixer.music.set_volume(0.2)
            pygame.mixer.Sound.play(erro)
            resposta["text"] = 'pense um pouco mais e volte depois, tá?'
            sleep(10)
            exit()

    botão = Button(janela, text='guess', justify=CENTER, command=guess)
    botão.grid(column=0, row=5)

    resposta = Label(janela, text="")
    resposta.grid(column=0, row=8)


botão = Button(janela, text='Começar!', justify=CENTER, command=guess_game)
botão.grid(column=0, row=1)


janela.mainloop()