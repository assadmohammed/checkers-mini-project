import pygame 
from .constants import SQUARE_SIZE,ROWS,COLUMNS,BLACK,RED

class Boards: 
    def __init__(self):
        self.board = []
        self.selected_pieces = None
        self.white_left = self.black_left = 12 
        self.white_kings = self.black_kings = 0 

    
    def draw_squares(self, win):
        win.fill(BLACK)
        for row in range(ROWS):
            for col in range(row % 2, 8, 2):
                pygame.draw.rect(win,RED, (row*SQUARE_SIZE, col*SQUARE_SIZE,SQUARE_SIZE,SQUARE_SIZE))


 