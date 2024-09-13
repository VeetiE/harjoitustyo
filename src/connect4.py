import pygame
from board import Board

pygame.init()

screen=pygame.display.set_mode((700,700))
board=Board()
game_ended=False

def draw_square(screen, row, col):
    pygame.draw.rect(screen, (0,0,255), (col*100, row*100+100, 100, 100))

def draw_circle(screen, color, row, col):
    pygame.draw.circle(screen, color, (col*100+50, row*100+150), 50)
    
while game_ended==False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    for row in range(6):
        for col in range(7):
            draw_square(screen, row,col)
            
            draw_circle(screen,(0,0,0), row,col)
    pygame.display.update()
