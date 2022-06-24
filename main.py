import pygame
from random import randint
pygame.init()
x = 610
y = 250
pos_x = 810
pos_y = 1200
pos_y_a = 1500
pos_y_c = 2000
timer = 0
tempo_segundo = 0

velocidade = 10
velocidade_outros = 12

fundo = pygame.image.load('tela_jogo.png')
carro = pygame.image.load('carro.png')
inimigo_1 = pygame.image.load('carro_cinza.png')
inimigo_2 = pygame.image.load('inimigo_1.png')
inimigo_3 = pygame.image.load('inimigo_2.png')

font = pygame.font.SysFont('arial black', 30)
texto = font.render("Tempo: ", True, (255,255,255), (0,0,0))
pos_texto = texto.get_rect()
pos_texto.center = (65,50)

janela = pygame.display.set_mode((1280,720))
pygame.display.set_caption("Corrida muito Louca")

janela_aberta = True

while janela_aberta :
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    comandos = pygame.key.get_pressed()

    if comandos[pygame.K_RIGHT] and x<= 840:
        x+=velocidade
    if comandos[pygame.K_LEFT] and x>=340:
        x-=velocidade

    if ((x + 80 > pos_x and y + 180 > pos_y)):
        y = y
    if ((x-80 < pos_x - 430 and y + 180 > pos_y_a)):
        y = y
    if ((x+80>pos_x  - 220 and y + 180 > pos_y_c) or (x-80 < pos_x  - 220 and y+180>pos_y_c)):
        y = y


    if (pos_y <= -80):
        pos_y = randint(800,2000)
    if (pos_y_a <= -80):
        pos_y_a = randint(1000,2000)
    if (pos_y_c <= -80):
        pos_y_c = randint(800,3000)



    if (timer<20):
        timer += 1
    else:
        tempo_segundo += 1
        texto = font.render("Tempo :"+str(tempo_segundo), True, (255,255,255), (0,0,0))
        timer = 0

    pos_y -= velocidade_outros
    pos_y_a -= velocidade_outros + 6
    pos_y_c -= velocidade_outros + 10

    janela.blit(fundo,(0,0))
    janela.blit(carro,(x,y))
    janela.blit(inimigo_1, (pos_x, pos_y))
    janela.blit(inimigo_2, (pos_x - 430 , pos_y_a))
    janela.blit(inimigo_3, (pos_x - 220, pos_y_c))
    janela.blit(texto,pos_texto)



    pygame.display.update()

pygame.quit()