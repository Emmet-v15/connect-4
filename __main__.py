from connect4 import Board
import pygame

pygame.init()

screen = pygame.display.set_mode([500, 500])

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((18, 18, 18))
    s = pygame.Surface((200,200))  # the size of your rect
    s.set_alpha(28)                # alpha level
    s.fill((255,255,255))           # this fills the entire surface
    screen.blit(s, (100,100))    # (0,0) are the top-left coordinates
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