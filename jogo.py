# importa modulo
import pygame
from random import randint
# usa função
pygame.init()

# e a posição onde o carro vai aparecer
#o pos_y controla autura onde o carro vai ficar
#o pos_x 
x = 370        #valor max a esquerda 308, max dir 445,meio 370
y = 200
pos_x = 300
pos_y = 600
pos_y_a = 600
pos_y_c = 600
velocidade = 10
velocidade_outros = 5
fundo = pygame.image.load("pista.png")
carro = pygame.image.load("carro5.png")
jipe = pygame.image.load("jipe.png")
jipe1 = pygame.image.load("jipe1.png")
carro4 = pygame.image.load("carro4.png")



# se não iniciar use o comando python -m pip install pygame

# definindo tamanho da janela
janela = pygame.display.set_mode ((800,500))

#vamos usar o metodo a baixo e onde vai fica o nome na janela que vai aparecer
pygame.display.set_caption("Criando um jogo com python")

#para fazer com que a janela feche vamos criar um laço
# de repetição e uma variavel 

janela_aberta = True
while janela_aberta :
    pygame.time.delay(50)
    #quando for disparado algum evento ele vai cair dentro desse for
    for event in pygame.event.get():
        if event.type == pygame.quit:
            janela_aberta = False

    comandos = pygame.key.get_pressed()
 #aumenta ou diminui a posição na tela if comandos[pygame.K_UP]:
  #          y -=velocidade  
  #  if comandos[pygame.K_DOWN]:
  #          y +=velocidade
    if comandos[pygame.K_LEFT] and x >= 308:
            x -= velocidade
    if comandos[pygame.K_RIGHT] and x <= 445:
            x += velocidade   
#com esse if a baixo resetamos a posição dos carros apos passarem pela pista
    if  (pos_y <= -180) and (pos_y_a <= -180) and (pos_y_c <= -180):
         pos_y = randint (800, 2000)
         pos_y_a = randint (800, 2000)
         pos_y_c = randint (800, 2000) 
#a função a baixo muda a posição dos carros no eixo y
    pos_y  -= velocidade_outros
    pos_y_a -= velocidade_outros -2
    pos_y_c -= velocidade_outros - 1   

    janela.blit(fundo,(0,0))  
    janela.blit(carro,(x,y))
    janela.blit(jipe, (pos_x + 100, pos_y))
    janela.blit(jipe1, (pos_x + 80, pos_y_a))
    janela.blit(carro4, (pos_x + 70, pos_y_c))


    pygame.display.update()



   # o trexo de codigo a baixo desenha um circulo na tela
   # pygame.draw.circle(janela, (0,255,0),(x, y),50) 
    #pygame.display.update()

pygame.quit()        