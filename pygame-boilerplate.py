import pygame
pygame.init()

screen = pygame.display.set_mode([512, 512])

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((18, 18, 18))
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)
    pygame.display.flip()

pygame.quit()
