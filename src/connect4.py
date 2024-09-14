import pygame
from board import Board

pygame.init()

screen=pygame.display.set_mode((700,700))
board=Board()
game_ended=False

turn=0

def draw_square(screen, row, col):
    pygame.draw.rect(screen, (0,0,255), (col*100, row*100+100, 100, 100))

def draw_circle(screen, color, row, col):
    pygame.draw.circle(screen, color, (col*100+50, row*100+150), 50)
    
while game_ended==False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type==pygame.MOUSEMOTION:
            screen.fill((0,0,0))
            mouse_pos=event.pos
            if turn==0:
                pygame.draw.circle(screen, (255,0,0), (mouse_pos[0], 50), 50)
            else:
                pygame.draw.circle(screen, (255,255,0), (mouse_pos[0], 50), 50)
        if event.type==pygame.MOUSEBUTTONDOWN:
            mouse_x=event.pos[0]
            col=int(mouse_x//100)
            if turn == 0:
                board.update_board(col, 1)
            else:
                board.update_board(col, 2)
            turn+=1
            turn=turn%2


    for row in range(6):
        for col in range(7):
            draw_square(screen, row,col)
            if board.board[row][col]==0:
                draw_circle(screen,(0,0,0), row,col)
            elif board.board[row][col]==1:
                draw_circle(screen,(255,0,0), row,col)
            elif board.board[row][col]==2:
                draw_circle(screen,(255,255,0), row,col)
    pygame.display.update()
    if board.game_ended==True:
        game_ended=True
