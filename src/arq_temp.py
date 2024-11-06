""" Módulo teste
"""

import pygame

# Inicializa
pygame.init()

# Tela
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Minigame META MATH')

screen_width = screen.get_width()
screen_height = screen.get_height()

rect1_color = (233, 34, 54)
rect2_color = (49, 98, 222)

rect1 = pygame.Rect(30, 30, 30, 30)
rect2 = pygame.Rect(200, 100, 23, 45)


# Loop principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        rect1.height += 1
    if keys[pygame.K_RIGHT]:
        rect2.x -= 1

    screen.fill((255, 255, 255))

    pygame.draw.rect(screen, rect1_color, rect1)
    pygame.draw.rect(screen, rect2_color, rect2)
    
    if rect1.colliderect(rect2):
        rect1.x = 300

    if rect2.x < 0:
        rect2.x = screen_width - rect2.width

    pygame.display.flip()

pygame.quit()