import pygame
from random import randrange
from time import sleep

pygame.init()

# Música
pygame.mixer.music.load("tema.mp3")
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1, 0, 1500)


# Efeitos sonoros
erro = pygame.mixer.Sound("erro.mp3")
vitoria = pygame.mixer.Sound("vitoria.mp3")
pygame.mixer.Sound.set_volume(erro, 0.05)
pygame.mixer.Sound.set_volume(vitoria, 0.05)

# Inicializando
print('='*50)
print(
    'Olá, vamos brincar?'
)
print(
    'Irei pensar em um número de 0 a 5. Tente adivinhar'
)
print('='*50)
sleep(1)
print(
    'Pensando ...'
)
sleep(2)

# Escolhendo um número de 0 a 5
a = randrange(6)
sleep(3)

# Condicionais.

x = int(input('Em qual número eu estou pensando ? '))  # Chance 1
if x == a:
    pygame.mixer.Sound.play(vitoria)
    print('Parabéns!! Você acertou. O número que eu estou pensando é {}'.format(a))
    print("Tchauuu")
    pygame.mixer.music.fadeout(20000)
    pygame.mixer.music.set_volume(0.2)
    sleep(30)
    exit()
else:
    pygame.mixer.Sound.play(erro)
    print('Poxa, tente novamente')

x = int(input('Em qual número eu estou pensando ? '))  # Chance 2
if x == a:
    pygame.mixer.music.set_volume(3)
    pygame.mixer.Sound.play(vitoria)
    print('Parabéns!! Você acertou. O número que eu estou pensando é {}'.format(a))
    print("Tchauuu")
    pygame.mixer.music.fadeout(20000)
    pygame.mixer.music.set_volume(0.2)
    sleep(30)
    exit()
else:
    pygame.mixer.Sound.play(erro)
    print('Poxa, tente novamente')

x = int(input('Em qual número eu estou pensando ? '))  # Chance 3
if x == a:
    pygame.mixer.music.set_volume(3)
    pygame.mixer.Sound.play(vitoria)
    print('Parabéns!! Você acertou. O número que eu estou pensando é {}'.format(a))
    print("Tchauuu")
    pygame.mixer.music.fadeout(20000)
    pygame.mixer.music.set_volume(0.2)
    sleep(30)
    exit()
else:
    pygame.mixer.Sound.play(erro)
    print('Poxa, tente novamente')

x = int(input('Em qual número eu estou pensando ? '))  # Chance 4
if x == a:
    pygame.mixer.music.set_volume(3)
    pygame.mixer.Sound.play(vitoria)
    print('Parabéns!! Você acertou. O número que eu estou pensando é {}'.format(a))
    print("Tchauuu")
    pygame.mixer.music.fadeout(20000)
    pygame.mixer.music.set_volume(0.2)
    sleep(30)
    exit()
else:
    pygame.mixer.Sound.play(erro)
    print('Poxa, tente novamente')

x = int(input('Em qual número eu estou pensando ? '))  # Chance 5
if x == a:
    pygame.mixer.music.set_volume(3)
    pygame.mixer.Sound.play(vitoria)
    print('Parabéns!! Você acertou. O número que eu estou pensando realmente é {}'.format(a))
    print("Tchauuu")
    pygame.mixer.music.fadeout(20000)
    pygame.mixer.music.set_volume(0.2)
    sleep(30)
    exit()
else:
    pygame.mixer.Sound.play(erro)
    print('Poxa, tente novamente')

x = int(input('Em qual número eu estou pensando ? '))  # Chance 6
if x == a:
    pygame.mixer.music.set_volume(3)
    pygame.mixer.Sound.play(vitoria)
    print('Parabéns!! Você acertou. O número que eu estou pensando é {}'.format(a))
    print("Tchauuu")
    pygame.mixer.music.fadeout(20000)
    pygame.mixer.music.set_volume(0.2)
    sleep(30)
    exit()
else:
    pygame.mixer.Sound.play(erro)
    pygame.mixer.music.fadeout(30000)
    pygame.mixer.music.set_volume(0.2)
    print('Pense um pouco mais e volte depois, tá?')
    sleep(50)
    exit()
