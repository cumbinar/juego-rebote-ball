#cuatro imágenes que se mueven en un rectángulo
import sys
import pygame
# Inicializamos pygame
pygame.init()
# Muestro una ventana de 800x600
size = 800, 600
screen = pygame.display.set_mode(size)
# Cambio el título de la ventana
pygame.display.set_caption("CUMBI BALL")
# Inicializamos variables
width, height = 800, 600
speed = [8, 8]
speed2 = [8, 2]
speed3 = [1, 1]
speed4 = [1, 3]
blue = 0, 170, 228
# Creo uno objetos imagen y obtengo su rectángulo
ball = pygame.image.load("ball.png")
ballrect = ball.get_rect()

bate = pygame.image.load("bate.png")
baterect = bate.get_rect()

triangulo = pygame.image.load("triangulo.png")
triangulorect = triangulo.get_rect()

cuadro = pygame.image.load("cuadro.png")
cuadrorect = cuadro.get_rect()


# Comenzamos el bucle del juego
run = True
while run:
    # Espero un tiempo (milisegundos) para que la pelota no vaya muy rápida
    pygame.time.delay(20)
    # Capturamos los eventos que se han producido
    for event in pygame.event.get():
        #Si el evento es salir de la ventana, terminamos
        if event.type == pygame.QUIT:
            run = False
    # Muevo la pelota
    ballrect = ballrect.move(speed)
    baterect = baterect.move(speed2)
    triangulorect = triangulorect.move(speed3)
    cuadrorect = cuadrorect.move(speed4)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    if baterect.left < 0 or baterect.right > width:
        speed2[0] = -speed2[0]
    if baterect.top < 0 or baterect.bottom > height:
        speed2[1] = -speed2[1]

    if triangulorect.left < 0 or triangulorect.right > width:
        speed3[0] = -speed3[0]
    if triangulorect.top < 0 or triangulorect.bottom > height:
        speed3[1] = -speed3[1]

    if cuadrorect.left < 0 or cuadrorect.right > width:
        speed4[0] = -speed4[0]
    if cuadrorect.top < 0 or cuadrorect.bottom > height:
        speed4[1] = -speed4[1]


    #Pinto el fondo de blanco, dibujo la pelota y actualizo la pantalla
    screen.fill(blue)
    screen.blit(ball, ballrect)
    screen.blit(bate, baterect)
    screen.blit(triangulo, triangulorect)
    screen.blit(cuadro, cuadrorect)
    pygame.display.flip()
# Salgo de pygame
pygame.quit()
