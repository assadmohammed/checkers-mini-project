import pygame
from checkers.constants import WIDTH,HEIGHT
from checkers.Board import Boards
FPS = 60


WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("checkers")

def main():
    run = True
    clock = pygame.time.Clock()
    board = Boards()


    while run :
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

                
        board.draw_squares(WIN)
        pygame.display.update()
        
        pygame.quit
            
          
    

main()