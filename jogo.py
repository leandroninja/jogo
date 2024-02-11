# importa modulo
import pygame
# usa função
pygame.init()
x = 400
y = 300
velocidade = 10
# se não iniciar use o comando python -m pip install pygame

# definindo tamanho da janela
janela = pygame.display.set_mode ((800,600))

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

    janela.fill((0,0,0))                   


    pygame.draw.circle(janela, (0,255,0),(x, y),50) 
    pygame.display.update()

pygame.quit()        