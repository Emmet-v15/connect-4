from connect4 import Board
import pygame
from pygame import gfxdraw


def drawAlphaRect(surface, size, pos, alpha, rgb=None):
    # precise

    s = pygame.Surface(size, pygame.SRCALPHA)
    if rgb == None:
        s.fill((255, 255, 255, alpha))
    else:
        s.fill((*rgb, alpha))
    surface.blit(s, pos)

    # faster
    # rect = pygame.Surface(size)
    # rect.set_alpha(alpha)
    # rect.fill((255, 255, 255))
    # surface.blit(rect, pos)


def drawAlphaCircle(surface, pos, radius, color=None):
    if color != None:

        gfxdraw.aacircle(surface, *pos, radius, (255, 255, 255))
        gfxdraw.filled_circle(surface, *pos, radius, (255, 255, 255))
    else:
        gfxdraw.aacircle(surface, *pos, radius, (255, 255, 255))
        gfxdraw.filled_circle(
            surface, *pos, radius, (255, 255, 255))


pygame.init()

win_size = [500, 500]
screen = pygame.display.set_mode(win_size)

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                event.pos

    screen.fill((18, 18, 18))

    for x in range(7):
        for y in range(7):
            if y == 0:
                drawAlphaRect(screen, [win_size[0]/8, win_size[1]/8],
                              [x*win_size[0]/7 + 5, y*win_size[1]/7 + 5], 50)
            else:
                drawAlphaCircle(screen, [round(x*win_size[0]/7) + 5 + round(win_size[0]/16), round(y*win_size[1]/7) + 5 + round(win_size[0]/16)], round(win_size[0]/16),
                                28)

    pygame.display.flip()

pygame.quit()

# if __name__ == "__main__":
#     board = new Board(9, 9)

#     players = ["R", "G"]
#     winner = None

#     while not winner:
#         for playerId in players:
#             print("Player", playerId + "'s Turn to slot a disc:")
#             board.printBoard()
#             col = 0
#             row = 0
#             while True:
#                 while not col:
#                     col = input("SELECT COLUMN (1-6)#> ")
#                 col = int(col)-1
#                 row = board.getFreeSlot(col)
#                 if row != None:
#                     break
#                 print("Column full, retry")
#                 col = None
#             board.claimSlot(row, col, playerId)
#             if board.checkForWinner(row, col):
#                 winner = playerId
#                 break
#     board.printBoard()
#     print(playerId, "won!")
