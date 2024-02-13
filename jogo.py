# importa modulo
import pygame
from random import randint
# usa função
pygame.init()

# e a posição onde o carro vai aparecer
#o pos_y controla a altura onde o carro vai ficar
#o pos_x 
x = 360       #valor max a esquerda 308, max dir 445,meio 370
y = 100
pos_x = 300
pos_y = 600
pos_y_a = 600
pos_y_b = 600
pos_y_c = 600
pos_y_d = 600
pos_y_e = 600
pos_y_f = 600
timer = 0
tempo_segundo = 0

velocidade = 10

velocidade_outros = 5
fundo = pygame.image.load("pista.png")
carro = pygame.image.load("carro1.png")
carro2 = pygame.image.load("carro2.png")
carro3 = pygame.image.load("carro3.png")
carro4 = pygame.image.load("carro4.png")
carro5 = pygame.image.load("carro5.png")
jipe = pygame.image.load("jipe.png")
jipe1 = pygame.image.load("jipe1.png")

font = pygame.font.SysFont ('arial black',30)
texto = font.render("tempo: ",True,(255,255,255),(0,0,0))
pos_texto = texto.get_rect()
pos_texto.center = (70,20)


# se não iniciar use o comando python -m pip install pygame

# definindo tamanho da janela
janela = pygame.display.set_mode ((800,619))

#vamos usar o metodo a baixo e onde vai fica o nome na janela que vai aparecer
pygame.display.set_caption("Criando um jogo com python")

#para fazer com que a janela feche vamos criar um laço
# de repetição e uma variavel 

janela_aberta = True
while janela_aberta :
    pygame.time.delay(50)
    #quando for disparado algum evento ele vai cair dentro desse for
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_UP]:
            y -=velocidade  
    if comandos[pygame.K_DOWN]:
            y +=velocidade
    if comandos[pygame.K_LEFT] and x>= 125:       #308
            x -= velocidade                        #na pista propria
    if comandos[pygame.K_RIGHT] and x<= 620:      #445
            x += velocidade   
#com esse if a baixo resetamos a posição dos carros apos passarem pela pista
    if  (pos_y <= -180) and (pos_y_a <= -180) and (pos_y_b <= -180) and (pos_y_c <= -180) and (pos_y_d <= -180) and (pos_y_e <= -180):
         pos_y = randint (1000, 1500)
         pos_y_a = randint (1000, 1400)
         pos_y_b = randint (1000, 1300)
         pos_y_c = randint (1000, 1200) 
         pos_y_d = randint (1000, 1100)
         pos_y_e = randint (900, 1000)
         pos_y_f = randint (800, 900)

#logica do if else todo esse bloco de codigo esta dentro do while esse while tem delay que atualiza a tela a cada 50 mls
 #mas a ideia e que a variavel seja incrementada a cada 1 seg ou seja vai passar pelo while 20 vezes a cada 50 mils       
  # e quando der 1 seg vai cair no else
  
    if  (timer <20):
         timer +=1

    else:  
          tempo_segundo +=1
          texto = font.render("tempo: "+str(tempo_segundo),True,(255,255,255),(0,0,0))
          timer = 0  
#a função a baixo muda a posição dos carros no eixo y
    pos_y  -= velocidade_outros
    pos_y_a -= velocidade_outros -2
    pos_y_b -= velocidade_outros - 1 
    pos_y_c -= velocidade_outros - 2
    pos_y_d -= velocidade_outros - 1
    pos_y_e -= velocidade_outros - 2 
    pos_y_f -= velocidade_outros - 1    





    janela.blit(fundo,(0,0))  
    janela.blit(carro,(x,y))
    janela.blit(carro2, (pos_x + 60, pos_y_b))
    janela.blit(carro3, (pos_x + 120, pos_y_c))
    janela.blit(carro4, (pos_x + 240, pos_y_d))
    janela.blit(carro5, (pos_x + -50, pos_y_f))
    janela.blit(jipe, (pos_x + 100, pos_y))
    janela.blit(jipe1, (pos_x - 90 , pos_y_a))
    


    janela.blit(texto,pos_texto)
    pygame.display.update()



   # o trexo de codigo a baixo desenha um circulo na tela
   # pygame.draw.circle(janela, (0,255,0),(x, y),50) 
    #pygame.display.update()

pygame.quit()        