# importa modulo
import pygame
# usa função
pygame.init()
# e a posição onde o carro vai aparecer
#o pos_y controla autura onde o carro vai ficar
#o pos_x 
x = 450
y = 300
pos_x = 100
pos_y = 300
velocidade = 10
velocidade_outros = 8
fundo = pygame.image.load("pista.png")
carro = pygame.image.load("carro3.png")
jipe = pygame.image.load("jipe.png")
jipe1 = pygame.image.load("jipe1.png")
carro4 = pygame.image.load("carro4.png")



# se não iniciar use o comando python -m pip install pygame

# definindo tamanho da janela
janela = pygame.display.set_mode ((800,800))

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
    if comandos[pygame.K_UP]:
            y -=velocidade  
    if comandos[pygame.K_DOWN]:
            y +=velocidade
    if comandos[pygame.K_LEFT]:
            x -=velocidade
    if comandos[pygame.K_RIGHT]:
            x +=velocidade   

    if  (pos_y <= -200):
        pos_y = 600

    pos_y  -= velocidade_outros     

    janela.blit(fundo,(0,0))  
    janela.blit(carro,(x,y))
    janela.blit(jipe, (pos_x + 180, pos_y))
    janela.blit(jipe1, (pos_x + 280, pos_y))
    janela.blit(carro4, (pos_x +100, pos_y))


    pygame.display.update()



   # o trexo de codigo a baixo desenha um circulo na tela
   # pygame.draw.circle(janela, (0,255,0),(x, y),50) 
    #pygame.display.update()

pygame.quit()        