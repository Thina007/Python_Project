import pygame,sys
import time
import numpy as np

pygame.init()

#global value's Declear:

WIDTH=600
HEIGHT=600
BOARD_ROWS=3
BOARD_COLS=3
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15
CROSS_WIDTH=25
SPACE=55
nu=0
no=0

RED=(255,0,0)
BG_COLOR=(28,170,156)
LINE_COLOR=(23,145,135)
CIRCLE_COLOR=(239,231,200)
CROSS_COLOR = (66,66,66)
LINE_WIDTH=15



screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("TIC TAC TOE : 'O'-Turn")

screen.fill(BG_COLOR)

board=np.zeros((BOARD_ROWS,BOARD_COLS))
#print(board)

def draw_line():
    #harizontal line:
    pygame.draw.line(screen,LINE_COLOR,(0,200),(600,200),LINE_WIDTH)
    pygame.draw.line(screen,LINE_COLOR,(0,400),(600,400),LINE_WIDTH)
    #Vertical line:
    pygame.draw.line(screen,LINE_COLOR,(200,0),(200,600),LINE_WIDTH)
    pygame.draw.line(screen,LINE_COLOR,(400,0),(400,600),LINE_WIDTH)
     
   
   
def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 2:
                pygame.draw.circle( screen,CIRCLE_COLOR,(int(col*200+100),int(row*200+100)),CIRCLE_RADIUS,CIRCLE_WIDTH)
            elif board[row][col] == 1:
                pygame.draw.line(screen,CROSS_COLOR,(col*200+SPACE,row*200+200-SPACE),(col*200+200-SPACE,row*200+SPACE),CROSS_WIDTH)
                pygame.draw.line(screen,CROSS_COLOR,(col*200+SPACE,row*200+SPACE),(col*200+200-SPACE,row*200+200-SPACE),CROSS_WIDTH)



    
def mark_square(row,col,player):
    board[row][col]=player


def available_square(row,col):
    return board[row][col] == 0
        
def is_board_full():
     for row in range(BOARD_ROWS):
        for col in range (BOARD_COLS):
            if board[row][col] == 0:
                return False
     return True



draw_line()

player = 1
while True:
     for event in pygame.event.get():
        if event.type ==pygame.QUIT:
           sys.exit()
           
        if event.type == pygame.MOUSEBUTTONDOWN:

            mouseX = event.pos[0] # x
            mouseY = event.pos[1] # y
            

            clicked_row = int(mouseY // 200)
            clicked_col = int(mouseX // 200)            
            if available_square(clicked_row,clicked_col ): 
               
               if nu==3:
                   break
               
                   
               if player ==1:
                    no = no+1                    
                    mark_square(clicked_row,clicked_col,1)
                    pygame.display.set_caption("'X'-Turn")
                    player = 2
                    
                    

                    if board[0][0]== 1 and board[0][1]== 1 and board[0][2]== 1 :
                         draw_figures()
                         nu=3
                         pygame.display.set_caption("'O'-Win")
                         pygame.draw.line(screen,RED,(0,100),(600,100),13)
                         break
                    if board[0][0]== 1 and board[1][0]== 1 and board[2][0]== 1 :
                         draw_figures()
                         nu=3
                         pygame.display.set_caption("'O'-Win")
                         pygame.draw.line(screen,RED,(100,0),(100,600),13)
                         break
                    if board[2][0]== 1 and board[2][1]== 1 and board[2][2]== 1:
                         draw_figures()
                         nu=3
                         pygame.display.set_caption("'O'-Win")
                         pygame.draw.line(screen,RED,(0,500),(600,500),13)
                         break
                    if board[2][2]== 1 and board[1][2]== 1 and board[0][2]== 1:
                         draw_figures()
                         nu=3
                         pygame.display.set_caption("'O'-Win")
                         pygame.draw.line(screen,RED,(500,0),(500,600),13)
                         break
                    if board[0][0]== 1 and board[1][1]== 1 and board[2][2]== 1:
                         draw_figures()
                         nu=3
                         pygame.display.set_caption("'O'-Win")
                         pygame.draw.line(screen,RED,(0,0),(600,600),13)
                         break
                    if board[0][2]== 1 and board[1][1]== 1 and board[2][0]== 1:
                         draw_figures()
                         nu=3
                         pygame.display.set_caption("'O'-Win")
                         pygame.draw.line(screen,RED,(600,0),(0,600),13)
                         break
                    if board[0][1]==1 and  board[1][1]==1 and board[2][1]==1:   
                         draw_figures()
                         nu=3
                         pygame.display.set_caption("'O'-Win")
                         pygame.draw.line(screen,RED,(300,0),(300,600),13)
                         break
                    if board[1][0]==1 and  board[1][1]==1 and board[1][2]==1 :  
                         draw_figures()
                         nu=3
                         pygame.display.set_caption("'O'-Win")
                         pygame.draw.line(screen,RED,(0,300),(600,300),13)
                         break  
                    if no==9:
                        draw_figures()  
                        pygame.display.set_caption("Tie...")
                        break
                        
               elif player == 2:
                    no=no+1                                     
                    mark_square(clicked_row,clicked_col,2)
                    pygame.display.set_caption("'O'-Turn")
                    player = 1


                    if board[0][0] == 2 and board[0][1] == 2 and board[0][2] == 2:
                         draw_figures()
                         nu=3
                         pygame.display.set_caption("'X'-Win")
                         pygame.draw.line(screen,RED,(0,100),(600,100),13)
                         break
                    if board[0][0] == 2 and board[1][0] == 2 and board[2][0] == 2:
                         draw_figures()
                         nu=3
                         pygame.display.set_caption("'X'-Win")
                         pygame.draw.line(screen,RED,(100,0),(100,600),13)  
                         break
                    if board[2][0] == 2 and board[2][1] == 2 and board[2][2] == 2:
                         draw_figures()
                         nu=3
                         pygame.display.set_caption("'X'-Win")
                         pygame.draw.line(screen,RED,(0,500),(600,500),13)
                         break
                    if board[2][2] == 2 and board[1][2] == 2 and board[0][2] == 2:
                         draw_figures()
                         nu=3
                         pygame.display.set_caption("'X'-Win")
                         pygame.draw.line(screen,RED,(500,0),(500,600),13) 
                         break
                    if board[0][0] == 2 and board[1][1] == 2 and board[2][2] == 2:
                         draw_figures()
                         nu=3
                         pygame.display.set_caption("'X'-Win")
                         pygame.draw.line(screen,RED,(0,0),(600,600),13)
                         break
                    if board[0][2] == 2 and board[1][1] == 2 and board[2][0] == 2:
                         draw_figures()
                         nu=3
                         pygame.display.set_caption("'X'-Win")
                         pygame.draw.line(screen,RED,(600,0),(0,600),13)
                         break
                    if board[0][1]==2 and  board[1][1]==2 and board[2][1]==2 : 
                         draw_figures()
                         nu=3
                         pygame.display.set_caption("'X'-Win")
                         pygame.draw.line(screen,RED,(300,0),(300,600),13) 
                         break
                    if board[1][0]==2 and  board[1][1]==2 and board[1][2]==2 :  
                         draw_figures()
                         nu=3
                         pygame.display.set_caption("'X'-Win")
                         pygame.draw.line(screen,RED,(0,300),(600,300),13)
                         break
                    
                    if no==9:
                      draw_figures()
                      pygame.display.set_caption("Tie...")
                      sys.exit()
                      break
                              
            draw_figures()
                    
              
                
     pygame.display.update()            

