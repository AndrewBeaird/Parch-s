import pygame
import random
import time

pygame.init()

WIDTH = 720
HEIGHT = 720

screen = pygame.display.set_mode((WIDTH, HEIGHT))

game_over = False

Red_Turn = False
Purple_Turn = False
Green_Turn = False
Blue_Turn = True

has_rolled = False

move1_complete = False
move2_complete = False

BlueBase = 4
BlueHome = 0
PurpleBase = 4
PurpleHome = 0
GreenBase = 4
GreenHome = 0
RedBase = 4 
RedHome = 0

Bluepiece1 = None
Bluepiece2 = None
Bluepiece3 = None
Bluepiece4 = None

Purplepiece1 = None
Purplepiece2 = None
Purplepiece3 = None
Purplepiece4 = None

Greenpiece1 = None
Greenpiece2 = None
Greenpiece3 = None
Greenpiece4 = None

Redpiece1 = None
Redpiece2 = None
Redpiece3 = None
Redpiece4 = None

Blockade = True
Clear_Blockade = False

Grey = (52,53,54)
Light_Grey = (135, 135, 135)
White = (216, 223, 232)
Gold = (240, 172, 13)
Light_Green = (148, 240, 188)
Light_Blue = (163, 235, 243)
Blue = (36, 29, 219)
Green = (0, 134, 58)
Light_Red = (252, 148, 148)
Red = (212, 0, 0)
Light_Purple = (199, 172, 235)
Purple = (152, 5, 118)

#Draw board lines using game board as reference.
def drawb():
    w = 30
    x,y = 0,0
    for row in board:
        for col in board:
            pygame.draw.rect(screen, (0,0,0), (x, y, w, w), 1)
            x = x + w
        y = y + w
        x = 0 
 

#Draw game squares using game board as reference.
def draw():
    w = 30
    x,y = 0,0
    for i in range (0, 24):
        for j in range (0, 24):
            if board[i][j] == ".":
                pygame.draw.rect(screen, (Grey), (x, y, w, w), 0)
            elif board[i][j]== "x":
                pygame.draw.rect(screen, (White), (x, y, w, w), 0)
            elif board[i][j]== "s":
                pygame.draw.rect(screen, (Gold), (x, y, w, w), 0)
            elif board[i][j]== "o":
                pygame.draw.rect(screen, (Gold), (x, y, w, w), 0)
            elif board[i][j]== "q":
                pygame.draw.rect(screen, (Light_Green), (x, y, w, w), 0)
            elif board[i][j]== "g":
                pygame.draw.rect(screen, (Green), (x, y, w, w), 0)
            elif board[i][j]== "w":
                pygame.draw.rect(screen, (Light_Blue), (x, y, w, w), 0)
            elif board[i][j]== "b":
                pygame.draw.rect(screen, (Blue), (x, y, w, w), 0)
            elif board[i][j]== "t":
                pygame.draw.rect(screen, (Light_Red), (x, y, w, w), 0)
            elif board[i][j]== "r":
                pygame.draw.rect(screen, (Red), (x, y, w, w), 0)
            elif board[i][j]== "j":
                pygame.draw.rect(screen, (Light_Purple), (x, y, w, w), 0)
            elif board[i][j]== "p":
                pygame.draw.rect(screen, (Purple), (x, y, w, w), 0)
            elif board[i][j]== "z":
                pygame.draw.rect(screen, (Light_Grey), (x, y, w, w), 0)

            x = x + w
        y = y + w
        x = 0 

#Draw game board
board = [ 
    [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",],
    [".",".",".",".",".",".",".",".",".","x","x","s","s","x","x",".",".",".",".",".",".",".",".",".",],
    [".",".",".",".",".",".",".",".",".","x","x","t","t","x","x",".",".",".",".",".",".",".",".",".",],
    [".",".",".",".",".",".",".",".",".","x","x","t","t","x","x",".",".",".",".",".",".",".",".",".",],
    [".",".",".",".",".",".",".",".",".","x","x","t","t","x","x",".",".",".",".",".",".",".",".",".",],
    [".",".",".",".",".",".",".",".",".","s","s","t","t","s","s",".",".",".",".",".",".",".",".",".",],
    [".",".",".",".",".","r","r",".",".","x","x","t","t","x","x",".",".","b","b",".",".",".",".",".",],
    [".",".",".",".",".","r","r",".",".","x","x","t","t","x","x",".",".","b","b",".",".",".",".",".",],
    [".",".",".",".",".",".",".",".",".","x","x","t","t","x","x",".",".",".",".",".",".",".",".",".",],
    [".",".","x","x","x","x","s","x","x","x","o","o","o","o","x","x","x","s","x","x","x","x",".",".",],
    [".",".","x","x","x","x","s","x","x","x","o","o","o","o","x","x","x","s","x","x","x","x",".",".",],
    [".",".","s","q","q","q","q","q","q","q","o","o","o","o","w","w","w","w","w","w","w","s",".",".",],
    [".",".","s","q","q","q","q","q","q","q","o","o","o","o","w","w","w","w","w","w","w","s",".",".",],
    [".",".","x","x","x","x","s","x","x","x","o","o","o","o","x","x","x","s","x","x","x","x",".",".",],
    [".",".","x","x","x","x","s","x","x","x","o","o","o","o","x","x","x","s","x","x","x","x",".",".",],
    [".",".",".",".",".",".",".",".",".","x","x","j","j","x","x",".",".",".",".",".",".",".",".",".",],
    [".",".",".",".",".","g","g",".",".","x","x","j","j","x","x",".",".","p","p",".",".",".",".",".",],
    [".",".",".",".",".","g","g",".",".","x","x","j","j","x","x",".",".","p","p",".",".",".",".",".",],
    [".",".",".",".",".",".",".",".",".","s","s","j","j","s","s",".",".",".",".",".",".",".",".",".",],
    [".",".",".",".",".",".",".",".",".","x","x","j","j","x","x",".",".",".",".",".",".",".",".",".",],
    [".",".",".",".",".",".",".",".",".","x","x","j","j","x","x",".",".",".",".",".",".",".",".",".",],
    [".",".",".",".",".",".",".",".",".","x","x","j","j","x","x",".",".",".",".",".",".",".",".",".",],
    [".",".",".",".",".",".",".",".",".","x","x","s","s","x","x",".",".",".",".",".",".",".",".",".",],
    [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",]]

#References game track that red pieces will follow. 
game_track_red = [[5,10], [6,10], [7,10], [8,10], [10,9], [10,8], [10,7], [10,6], [10,5], [10,4], [10,3], [10,2], 
[12,2], [13,2], [13,3], [13,4], [13,5],
[13,6], [13,7], [13,8], [13,9], [15,9], [16,9], [17,9], [18,9], [19,9], [20,9], [21,9], [22,9], [22,11], 
[22,13], [21,13], [20,13], [19,13], [18,13], [17,13], [16,13], [15,13], [14,14], [14,15], [14,16], [14,17], [14,18],
[14,19], [14,20], [14,21], [12,21], [10,21], [10,20], [10,19], [10,18], [10,17], [10,16], [10,15], [10, 14],
[8,14], [7,14], [6,14], [5,14], [4,14], [3,14], [2,14], [1,14], [1,12], 
[2,12], [3,12], [4,12], [5,12], [6,12], [7,12], [8,12], 
[0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0]]

#References secondary game track that red pieces will follow.
game_track_red2 = [[5,9], [6,9], [7,9], [8,9], [9,9], [9,8], [9,7], [9,6], [9,5], [9,4], [9,3], [9,2], 
[11,2], [14,2], [14,3], [14,4], [14,5],
[14,6], [14,7], [14,8], [14,9], [15,10], [16,10], [17,10], [18,10], [19,10], [20,10], [21,10], [22,10], [22,12],
[22,14], [21,14], [20,14], [19,14], [18,14], [17,14], [16,14], [15,14], [13,14], [13,15], [13,16], [13,17], [13,18],
[13,19], [13,20], [13,21], [11,21], [9,21], [9,20], [9,19], [9,18], [9,17], [9,16], [9,15], [9, 14],
[8,13], [7,13], [6,13], [5,13], [4,13], [3,13], [2,13], [1,13], [1,11], 
[2,11], [3,11], [4,11], [5,11], [6,11],[7,11], [8,11], 
[0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0]]

#References game track that purple pieces will follow.
game_track_purple = [[18,13], [17,13], [16,13], [15,13], [14,14], [14,15], [14,16], [14,17], [14,18], [14,19], 
[14,20], [14,21], [12,21], [10,21], [10,20], [10,19], [10,18], 
[10,17], [10,16], [10,15], [10,14], [8,14], [7,14], [6,14], [5,14], [4,14], [3,14], [2,14], [1,14], [1,12], 
[1, 10], [2,10], [3,10], [4,10], [5,10], [6,10], [7,10], [8,10], [10,9], [10,8], [10,7], [10,6], [10,5], [10,4], 
[10,3], [10,2], [12,2], [13,2], [13,3], [13,4], [13,5], [13,6], [13,7], [13,8], [13,9], [15,9], [16,9], [17,9], 
[18,9], [19,9], [20,9], [21,9], [22,9], [22,11], 
[21,11], [20,11], [19,11], [18,11], [17,11], [16,11], [15,11], 
[0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0]]

#References secondary game track that purple pieces will follow.
game_track_purple2 = [[18,14], [17,14], [16,14], [15,14], [13,14], [13,15], [13,16], [13,17], [13,18], [13,19], [13,20], 
[13,21], [11,21], [9,21], [9,20], [9,19], [9,18], [9,17], [9,16], [9,15], [9, 14], [8,13], [7,13], [6,13], [5,13], 
[4,13], [3,13], [2,13], [1,13], [1,11], [1,9], [2,9], [3,9], [4,9], [5,9], [6,9], [7,9], [8,9], 
[9,9], [9,8], [9,7], [9,6], [9,5], [9,4], [9,3], [9,2], [11,2], [14,2], [14,3], [14,4], [14,5], [14,6], [14,7], [14,8], 
[14,9], [15,10], [16,10], [17,10], [18,10], [19,10], [20,10], [21,10], [22,10], [22,12],
[21,12], [20,12], [19,12], [18,12], [17,12], [16,12], [15,12],
[0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0]]

#References game track that green pieces will follow.
game_track_green = [[13,6], [13,7], [13,8], [13,9], [15,9], [16,9], [17,9], [18,9], [19,9], [20,9], [21,9], [22,9], [22,11], 
[22,13], [21,13], [20,13], [19,13], [18,13], [17,13], [16,13], [15,13], [14,14], [14,15], [14,16], [14,17], [14,18],
[14,19], [14,20], [14,21], [12,21], [10,21], [10,20], [10,19], [10,18], [10,17], [10,16], [10,15], [10, 14],
[8,14], [7,14], [6,14], [5,14], [4,14], [3,14], [2,14], [1,14], [1,12],[1, 10], [2,10], 
[3,10], [4,10], [5,10], [6,10], [7,10], [8,10], [10,9], [10,8], [10,7], [10,6], [10,5], [10,4], [10,3], [10,2], [12,2], 
[12,3], [12,4], [12,5], [12,6], [12,7], [12,8], [12,9],
[0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0]] 

#References secondary game track that green pieces will follow.
game_track_green2 = [[14,6], [14,7], [14,8], [14,9], [15,10], [16,10], [17,10], [18,10], [19,10], [20,10], [21,10], [22,10], [22,12],
[22,14], [21,14], [20,14], [19,14], [18,14], [17,14], [16,14], [15,14], [13,14], [13,15], [13,16], [13,17], [13,18],
[13,19], [13,20], [13,21], [11,21], [9,21], [9,20], [9,19], [9,18], [9,17], [9,16], [9,15], [9, 14],
[8,13], [7,13], [6,13], [5,13], [4,13], [3,13], [2,13], [1,13], [1,11], [1,9], [2,9], 
[3,9], [4,9], [5,9], [6,9], [7,9], [8,9], [9,9], [9,8], [9,7], [9,6], [9,5], [9,4], [9,3], [9,2], [11,2],
[11,3], [11,4], [11,5], [11,6], [11,7], [11,8], [11,9],
[0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0]]

#References game track that blue pieces will follow.
game_track_blue = [[10,17], [10,16], [10,15], [10,14], [8,14], [7,14], [6,14], [5,14], [4,14], [3,14], [2,14], [1,14], [1,12], 
[1, 10], [2,10], [3,10], [4,10], [5,10], [6,10], [7,10], [8,10], [10,9], [10,8], [10,7], [10,6], [10,5], [10,4], 
[10,3], [10,2], [12,2], [13,2], [13,3], [13,4], [13,5], [13,6], [13,7], [13,8], [13,9], [15,9], [16,9], [17,9], 
[18,9], [19,9], [20,9], [21,9], [22,9], [22,11],
[22,13], [21,13], [20,13], [19,13], [18,13], [17,13], [16,13], [15,13], [14,14], [14,15], [14,16], [14,17], [14,18],
[14,19], [14,20], [14,21], [12,21], 
[12,20], [12,19], [12,18], [12,17], [12,16], [12,15], [12,14],
[0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0]]

#References secondary game track that blue pieces will follow.
game_track_blue2 = [[9,17], [9,16], [9,15], [9, 14], [8,13], [7,13], [6,13], [5,13], 
[4,13], [3,13], [2,13], [1,13], [1,11], [1,9], [2,9], [3,9], [4,9], [5,9], [6,9], [7,9], [8,9], 
[9,9], [9,8], [9,7], [9,6], [9,5], [9,4], [9,3], [9,2], [11,2], [14,2], [14,3], [14,4], [14,5], [14,6], [14,7], [14,8], 
[14,9], [15,10], [16,10], [17,10], [18,10], [19,10], [20,10], [21,10], [22,10], [22,12], [22,14], [21,14], [20,14], [19,14], 
[18,14], [17,14], [16,14], [15,14], [13,14], [13,15], [13,16], [13,17], [13,18], [13,19], [13,20], [13,21], [11,21],
[11,20], [11,19], [11,18], [11,17], [11,16], [11,15], [11,14],
[0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0]]
 
#Random dice roll #1
def Show_num1(diceRoll, color):
    if diceRoll == 1:
        board[23][19] = color
        board[22][19] = color
        board[21][19] = color
        board[20][19] = color
        board[19][19] = color

    if diceRoll == 2:
        board[19][17] = color
        board[19][18] = color
        board[19][19] = color
        board[20][19] = color
        board[21][17] = color
        board[21][18] = color
        board[21][19] = color
        board[22][17] = color
        board[23][17] = color
        board[23][18] = color
        board[23][19] = color

    if diceRoll == 3:
        board[19][17] = color
        board[19][18] = color
        board[19][19] = color
        board[20][19] = color
        board[21][17] = color
        board[21][18] = color
        board[21][19] = color
        board[22][19] = color
        board[23][17] = color
        board[23][18] = color
        board[23][19] = color

    if diceRoll == 4:
        board[19][17] = color
        board[19][19] = color
        board[20][17] = color
        board[20][19] = color
        board[21][17] = color
        board[21][18] = color
        board[21][19] = color
        board[22][19] = color
        board[23][19] = color

    if diceRoll == 5:
        board[19][17] = color
        board[19][18] = color
        board[19][19] = color
        board[20][17] = color
        board[21][17] = color
        board[21][18] = color
        board[21][19] = color
        board[22][19] = color
        board[23][17] = color
        board[23][18] = color
        board[23][19] = color

    if diceRoll == 6:
        board[19][17] = color
        board[19][18] = color
        board[19][19] = color
        board[20][17] = color
        board[21][17] = color
        board[21][18] = color
        board[21][19] = color
        board[22][17] = color
        board[22][19] = color
        board[23][17] = color
        board[23][18] = color
        board[23][19] = color 
#Random dice roll #2
def Show_num2(diceRoll, color):
    
    if diceRoll == 1:
        board[23][23] = color
        board[22][23] = color
        board[21][23] = color
        board[20][23] = color
        board[19][23] = color

    if diceRoll == 2:
        board[19][21] = color
        board[19][22] = color
        board[19][23] = color
        board[20][23] = color
        board[21][21] = color
        board[21][22] = color
        board[21][23] = color
        board[22][21] = color
        board[23][21] = color
        board[23][22] = color
        board[23][23] = color

    if diceRoll == 3:
        board[19][21] = color
        board[19][22] = color
        board[19][23] = color
        board[20][23] = color
        board[21][21] = color
        board[21][22] = color
        board[21][23] = color
        board[22][23] = color
        board[23][21] = color
        board[23][22] = color
        board[23][23] = color

    if diceRoll == 4:
        board[19][21] = color
        board[19][23] = color
        board[20][21] = color
        board[20][23] = color
        board[21][21] = color
        board[21][22] = color
        board[21][23] = color
        board[22][23] = color
        board[23][23] = color

    if diceRoll == 5:
        board[19][21] = color
        board[19][22] = color
        board[19][23] = color
        board[20][21] = color
        board[21][21] = color
        board[21][22] = color
        board[21][23] = color
        board[22][23] = color
        board[23][21] = color
        board[23][22] = color
        board[23][23] = color

    if diceRoll == 6:
        board[19][21] = color
        board[19][22] = color
        board[19][23] = color
        board[20][21] = color
        board[21][21] = color
        board[21][22] = color
        board[21][23] = color
        board[22][21] = color
        board[22][23] = color
        board[23][21] = color
        board[23][22] = color
        board[23][23] = color 
    
    draw()
    drawb()      
    pygame.display.update() 
    pygame.time.wait(500)

#Subtract red base when a 5 is rolled.
def SubRBase():
    if RedBase == 4:
        board[6][5] = "r"
        board[6][6] = "r"
        board[7][5] = "r"
        board[7][6] = "r"
    elif RedBase == 3:
        board[6][5] = "r"
        board[6][6] = "r"
        board[7][5] = "r"
        board[7][6] = "z"
    elif RedBase == 2:
        board[6][5] = "r"
        board[6][6] = "r"
        board[7][5] = "z"
        board[7][6] = "z"
    elif RedBase == 1:
        board[6][5] = "z"
        board[6][6] = "r"
        board[7][5] = "z"
        board[7][6] = "z"
    elif RedBase <= 0:
        board[6][5] = "z"
        board[6][6] = "z"
        board[7][5] = "z"
        board[7][6] = "z"
#Subtract purple base when a 5 is rolled.
def SubPBase():
    if PurpleBase == 4:
        board[16][17] = "p"
        board[16][18] = "p"
        board[17][17] = "p"
        board[17][18] = "p"
    elif PurpleBase == 3:
        board[16][17] = "p"
        board[16][18] = "p"
        board[17][17] = "p"
        board[17][18] = "z"
    elif PurpleBase == 2:
        board[16][17] = "p"
        board[16][18] = "p"
        board[17][17] = "z"
        board[17][18] = "z"
    elif PurpleBase == 1:
        board[16][17] = "z"
        board[16][18] = "p"
        board[17][17] = "z"
        board[17][18] = "z"
    elif PurpleBase <= 0:
        board[16][17] = "z"
        board[16][18] = "z"
        board[17][17] = "z"
        board[17][18] = "z"
#Subtract green base when a 5 is rolled.
def SubGBase():
    if GreenBase == 4:
        board[16][5] = "g"
        board[16][6] = "g"
        board[17][5] = "g"
        board[17][6] = "g"
    elif GreenBase == 3:
        board[16][5] = "g"
        board[16][6] = "g"
        board[17][5] = "g"
        board[17][6] = "z"
    elif GreenBase == 2:
        board[16][5] = "g"
        board[16][6] = "g"
        board[17][5] = "z"
        board[17][6] = "z"
    elif GreenBase == 1:
        board[16][5] = "z"
        board[16][6] = "g"
        board[17][5] = "z"
        board[17][6] = "z"
    elif GreenBase <= 0:
        board[16][5] = "z"
        board[16][6] = "z"
        board[17][5] = "z"
        board[17][6] = "z"
#Subtract blue base when a 5 is rolled.
def SubBBase():
    if BlueBase == 4:
        board[6][17] = "b"
        board[6][18] = "b"
        board[7][17] = "b"
        board[7][18] = "b"
    elif BlueBase == 3:
        board[6][17] = "b"
        board[6][18] = "b"
        board[7][17] = "b"
        board[7][18] = "z"
    elif BlueBase == 2:
        board[6][17] = "b"
        board[6][18] = "b"
        board[7][17] = "z"
        board[7][18] = "z"
    elif BlueBase == 1:
        board[6][17] = "z"
        board[6][18] = "b"
        board[7][17] = "z"
        board[7][18] = "z"
    elif BlueBase <= 0:
        board[6][17] = "z"
        board[6][18] = "z"
        board[7][17] = "z"
        board[7][18] = "z"


#Add to red home base once piece has succesfully navigated board.
def AdRHome():
    if RedHome == 4:
        board[9][11] = "r"
        board[9][12] = "r"
        board[10][11] = "r"
        board[10][12] = "r"
    elif RedHome == 3:
        board[9][11] = "r"
        board[9][12] = "r"
        board[10][11] = "r"
        board[10][12] = "o"
    elif RedHome == 2:
        board[9][11] = "r"
        board[9][12] = "r"
        board[10][11] = "o"
        board[10][12] = "o"
    elif RedHome == 1:
        board[9][11] = "r"
        board[9][12] = "o"
        board[10][11] = "o"
        board[10][12] = "o"
    elif RedHome <= 0:
        board[9][11] = "o"
        board[9][12] = "o"
        board[10][11] = "o"
        board[10][12] = "o"
#Add to purple home base once piece has succesfully navigated board.
def AdPHome():
    if PurpleHome == 4:
        board[13][11] = "p"
        board[13][12] = "p"
        board[14][11] = "p"
        board[14][12] = "p"
    elif PurpleHome == 3:
        board[13][11] = "p"
        board[13][12] = "p"
        board[14][11] = "p"
        board[14][12] = "o"
    elif PurpleHome == 2:
        board[13][11] = "p"
        board[13][12] = "p"
        board[14][11] = "o"
        board[14][12] = "o"
    elif PurpleHome == 1:
        board[13][11] = "p"
        board[13][12] = "o"
        board[14][11] = "o"
        board[14][12] = "o"
#Add to blue home base once piece has succesfully navigated board.
def AdBHome():
    if BlueHome == 4:
        board[11][12] = "b"
        board[11][13] = "b"
        board[12][12] = "b"
        board[12][13] = "b"
    elif BlueHome == 3:
        board[11][12] = "b"
        board[11][13] = "b"
        board[12][12] = "b"
        board[12][13] = "o"
    elif BlueHome == 2:
        board[11][12] = "b"
        board[11][13] = "b"
        board[12][12] = "o"
        board[12][13] = "o"
    elif BlueHome == 1:
        board[11][12] = "b"
        board[11][13] = "o"
        board[12][12] = "o"
        board[12][13] = "o" 
#Add to green home base once piece has succesfully navigated board.
def AdGHome():
    if GreenHome == 4:
        board[11][10] = "g"
        board[11][11] = "g"
        board[12][10] = "g"
        board[12][11] = "g"
    elif GreenHome == 3:
        board[11][10] = "g"
        board[11][11] = "g"
        board[12][10] = "g"
        board[12][11] = "o"
    elif GreenHome == 2:
        board[11][10] = "g"
        board[11][11] = "g"
        board[12][10] = "o"
        board[12][11] = "o"
    elif GreenHome == 1:
        board[11][10] = "g"
        board[11][11] = "o"
        board[12][10] = "o"
        board[12][11] = "o"

#Set dice roll #1 back to 0 position
def clock_reset1():
    board[19][17] = "."
    board[19][18] = "."
    board[19][19] = "."
    board[20][17] = "."
    board[20][19] = "."
    board[21][17] = "."
    board[21][18] = "."
    board[21][19] = "."
    board[22][17] = "."
    board[22][19] = "."
    board[23][17] = "."
    board[23][18] = "."
    board[23][19] = "."  
#Set dice roll #2 back to 0 position
def clock_reset2():
    board[19][21] = "."
    board[19][22] = "."
    board[19][23] = "."
    board[20][21] = "."
    board[20][23] = "."
    board[21][21] = "."
    board[21][22] = "."
    board[21][23] = "."
    board[22][21] = "."
    board[22][23] = "."
    board[23][21] = "."
    board[23][22] = "."
    board[23][23] = "." 


#Read dice roll #1 and advance red piece along game track.
def red_read1(position):
    global Redpiece1
    global Redpiece2
    global Redpiece3
    global Redpiece4
    global RedHome

    piece = position

    rules = [board[23][19] != ".",
    board[22][19] != ".",
    board[21][19] != ".",
    board[20][19] != ".",
    board[19][19] != ".",
    board[23][17] == ".",
    board[22][17] == ".",
    board[21][17] == ".",
    board[20][17] == ".",
    board[19][17] == ".",]

    if all(rules):
        if (piece + 1) <= 70: 
            piece += 1
        elif (piece +1) == 71:
            piece += 1
            RedHome += 1
            
    rules = [board[19][17] != ".",
    board[19][18] != ".",
    board[19][19] != ".",
    board[20][19] != ".",
    board[21][17] != ".",
    board[21][18] != ".",
    board[21][19] != ".",
    board[22][17] != ".",
    board[23][17] != ".",
    board[23][18] != ".",
    board[23][19] != "."]

    if all(rules):
        if (piece + 2) <= 70: 
            piece += 2
        elif (piece +2) == 71:
            piece += 2
            RedHome += 1
            
    rules = [board[19][17] != ".",
    board[19][18] != ".",
    board[19][19] != ".",
    board[20][19] != ".",
    board[21][17] != ".",
    board[21][18] != ".",
    board[21][19] != ".",
    board[22][19] != ".",
    board[23][17] != ".",
    board[23][18] != ".",
    board[23][19] != "."]

    if all(rules):
        if (piece + 3) <= 70: 
            piece += 3
        elif (piece +3) == 71:
            piece += 3
            RedHome += 1
            
    rules = [board[19][17] != ".",
    board[19][19] != ".",
    board[20][17] != ".",
    board[20][19] != ".",
    board[21][17] != ".",
    board[21][18] != ".",
    board[21][19] != ".",
    board[22][19] != ".",
    board[23][19] != "."]

    if all(rules):
        if (piece + 4) <= 70: 
            piece += 4
        elif (piece +4) == 71:
            piece += 4
            RedHome += 1
            
    rules = [board[19][17] != ".",
    board[19][18] != ".",
    board[19][19] != ".",
    board[20][17] != ".",
    board[21][17] != ".",
    board[21][18] != ".",
    board[21][19] != ".",
    board[22][17] == ".",
    board[22][19] != ".",
    board[23][17] != ".",
    board[23][18] != ".",
    board[23][19] != "."]

    if all(rules):
        if (piece + 5) <= 70: 
            piece += 5
        elif (piece +5) == 71:
            piece += 5
            RedHome += 1
            
    rules = [board[19][17] != ".",
    board[19][18] != ".",
    board[19][19] != ".",
    board[20][17] != ".",
    board[21][17] != ".",
    board[21][18] != ".",
    board[21][19] != ".",
    board[22][17] != ".",
    board[22][19] != ".",
    board[23][17] != ".",
    board[23][18] != ".",
    board[23][19] != "."]
    if all(rules):
        if (piece + 6) <= 70: 
            piece += 6
        elif (piece +6) == 71:
            piece += 6
            RedHome += 1
            
    if position == Redpiece1:
        Redpiece1 = piece
    elif position == Redpiece2:
        Redpiece2 = piece
    elif position == Redpiece3:
        Redpiece3 = piece
    elif position == Redpiece4:
        Redpiece4 = piece
#Read dice roll #2 and advance red piece along game track.
def red_read2(position):
    global Redpiece1
    global Redpiece2
    global Redpiece3
    global Redpiece4
    global RedHome

    piece = position

    rules = [board[23][23] != ".",
    board[22][23] != ".",
    board[21][23] != ".",
    board[20][23] != ".",
    board[19][23] != ".",
    board[23][21] == ".",
    board[22][21] == ".",
    board[21][21] == ".",
    board[20][21] == ".",
    board[19][21] == ".",]

    if all(rules):
        if (piece + 1) <= 70: 
            piece += 1
        elif (piece +1) == 71:
            piece += 1
            RedHome += 1
            
    rules = [board[19][21] != ".",
    board[19][22] != ".",
    board[19][23] != ".",
    board[20][23] != ".",
    board[21][21] != ".",
    board[21][22] != ".",
    board[21][23] != ".",
    board[22][21] != ".",
    board[23][21] != ".",
    board[23][22] != ".",
    board[23][23] != "."]

    if all(rules):
        if (piece + 2) <= 70: 
            piece += 2
        elif (piece +2) == 71:
            piece += 2
            RedHome += 1
            
    rules = [board[19][21] != ".",
    board[19][22] != ".",
    board[19][23] != ".",
    board[20][23] != ".",
    board[21][21] != ".",
    board[21][22] != ".",
    board[21][23] != ".",
    board[22][23] != ".",
    board[23][21] != ".",
    board[23][22] != ".",
    board[23][23] != "."]

    if all(rules):
        if (piece + 3) <= 70: 
            piece += 3
        elif (piece +3) == 71:
            piece += 3
            RedHome += 1
            
    rules = [board[19][21] != ".",
    board[19][23] != ".",
    board[20][21] != ".",
    board[20][23] != ".",
    board[21][21] != ".",
    board[21][22] != ".",
    board[21][23] != ".",
    board[22][23] != ".",
    board[23][23] != "."]

    if all(rules):
        if (piece + 4) <= 70: 
            piece += 4
        elif (piece +4) == 71:
            piece += 4
            RedHome += 1
            
    rules = [board[19][21] != ".",
    board[19][22] != ".",
    board[19][23] != ".",
    board[20][21] != ".",
    board[21][21] != ".",
    board[21][22] != ".",
    board[21][23] != ".",
    board[22][21] == ".",
    board[22][23] != ".",
    board[23][21] != ".",
    board[23][22] != ".",
    board[23][23] != "."]

    if all(rules):
        if (piece + 5) <= 70: 
            piece += 5
        elif (piece +5) == 71:
            piece += 5
            RedHome += 1
            
    rules = [board[19][21] != ".",
    board[19][22] != ".",
    board[19][23] != ".",
    board[20][21] != ".",
    board[21][21] != ".",
    board[21][22] != ".",
    board[21][23] != ".",
    board[22][21] != ".",
    board[22][23] != ".",
    board[23][21] != ".",
    board[23][22] != ".",
    board[23][23] != "."]

    if all(rules):
        if (piece + 6) <= 70: 
            piece += 6
        elif (piece +6) == 71:
            piece += 6
            RedHome += 1
            
    if position == Redpiece1:
        Redpiece1 = piece
    elif position == Redpiece2:
        Redpiece2 = piece
    elif position == Redpiece3:
        Redpiece3 = piece
    elif position == Redpiece4:
        Redpiece4 = piece
#Read dice roll #1 and advance purple piece along game track.
def purple_read1(position):
   
    global Purplepiece1
    global Purplepiece2
    global Purplepiece3
    global Purplepiece4
    global PurpleHome

    piece = position

    rules = [board[23][19] != ".",
    board[22][19] != ".",
    board[21][19] != ".",
    board[20][19] != ".",
    board[19][19] != ".",
    board[23][17] == ".",
    board[22][17] == ".",
    board[21][17] == ".",
    board[20][17] == ".",
    board[19][17] == ".",]

    if all(rules):
        if (piece + 1) <= 70: 
            piece += 1
        elif (piece +1) == 71:
            piece += 1
            PurpleHome += 1
            
    rules = [board[19][17] != ".",
    board[19][18] != ".",
    board[19][19] != ".",
    board[20][19] != ".",
    board[21][17] != ".",
    board[21][18] != ".",
    board[21][19] != ".",
    board[22][17] != ".",
    board[23][17] != ".",
    board[23][18] != ".",
    board[23][19] != "."]

    if all(rules):
        if (piece + 2) <= 70: 
            piece += 2
        elif (piece +2) == 71:
            piece += 2
            PurpleHome += 1
            
    rules = [board[19][17] != ".",
    board[19][18] != ".",
    board[19][19] != ".",
    board[20][19] != ".",
    board[21][17] != ".",
    board[21][18] != ".",
    board[21][19] != ".",
    board[22][19] != ".",
    board[23][17] != ".",
    board[23][18] != ".",
    board[23][19] != "."]

    if all(rules):
        if (piece + 3) <= 70: 
            piece += 3
        elif (piece +3) == 71:
            piece += 3
            PurpleHome += 1
            
    rules = [board[19][17] != ".",
    board[19][19] != ".",
    board[20][17] != ".",
    board[20][19] != ".",
    board[21][17] != ".",
    board[21][18] != ".",
    board[21][19] != ".",
    board[22][19] != ".",
    board[23][19] != "."]

    if all(rules):
        if (piece + 4) <= 70: 
            piece += 4
        elif (piece +4) == 71:
            piece += 4
            PurpleHome += 1
            
    rules = [board[19][17] != ".",
    board[19][18] != ".",
    board[19][19] != ".",
    board[20][17] != ".",
    board[21][17] != ".",
    board[21][18] != ".",
    board[21][19] != ".",
    board[22][17] == ".",
    board[22][19] != ".",
    board[23][17] != ".",
    board[23][18] != ".",
    board[23][19] != "."]

    if all(rules):
        if (piece + 5) <= 70: 
            piece += 5
        elif (piece +5) == 71:
            piece += 5
            PurpleHome += 1
            
    rules = [board[19][17] != ".",
    board[19][18] != ".",
    board[19][19] != ".",
    board[20][17] != ".",
    board[21][17] != ".",
    board[21][18] != ".",
    board[21][19] != ".",
    board[22][17] != ".",
    board[22][19] != ".",
    board[23][17] != ".",
    board[23][18] != ".",
    board[23][19] != "."]
    if all(rules):
        if (piece + 6) <= 70: 
            piece += 6
        elif (piece +6) == 71:
            piece += 6
            PurpleHome += 1
            
    if position == Purplepiece1:
        Purplepiece1 = piece
    elif position == Purplepiece2:
        Purplepiece2 = piece
    elif position == Purplepiece3:
        Purplepiece3 = piece
    elif position == Purplepiece4:
        Purplepiece4 = piece
#Read dice roll #2 and advance purple piece along game track.
def purple_read2(position):

    global Purplepiece1
    global Purplepiece2
    global Purplepiece3
    global Purplepiece4
    global PurpleHome

    piece = position

    rules = [board[23][23] != ".",
    board[22][23] != ".",
    board[21][23] != ".",
    board[20][23] != ".",
    board[19][23] != ".",
    board[23][21] == ".",
    board[22][21] == ".",
    board[21][21] == ".",
    board[20][21] == ".",
    board[19][21] == ".",]

    if all(rules):
        if (piece + 1) <= 70: 
            piece += 1
        elif (piece +1) == 71:
            piece += 1
            PurpleHome += 1
            
    rules = [board[19][21] != ".",
    board[19][22] != ".",
    board[19][23] != ".",
    board[20][23] != ".",
    board[21][21] != ".",
    board[21][22] != ".",
    board[21][23] != ".",
    board[22][21] != ".",
    board[23][21] != ".",
    board[23][22] != ".",
    board[23][23] != "."]

    if all(rules):
        if (piece + 2) <= 70: 
            piece += 2
        elif (piece +2) == 71:
            piece += 2
            PurpleHome += 1
            
    rules = [board[19][21] != ".",
    board[19][22] != ".",
    board[19][23] != ".",
    board[20][23] != ".",
    board[21][21] != ".",
    board[21][22] != ".",
    board[21][23] != ".",
    board[22][23] != ".",
    board[23][21] != ".",
    board[23][22] != ".",
    board[23][23] != "."]

    if all(rules):
        if (piece + 3) <= 70: 
            piece += 3
        elif (piece +3) == 71:
            piece += 3
            PurpleHome += 1
            
    rules = [board[19][21] != ".",
    board[19][23] != ".",
    board[20][21] != ".",
    board[20][23] != ".",
    board[21][21] != ".",
    board[21][22] != ".",
    board[21][23] != ".",
    board[22][23] != ".",
    board[23][23] != "."]

    if all(rules):
        if (piece + 4) <= 70: 
            piece += 4
        elif (piece +4) == 71:
            piece += 4
            PurpleHome += 1
            
    rules = [board[19][21] != ".",
    board[19][22] != ".",
    board[19][23] != ".",
    board[20][21] != ".",
    board[21][21] != ".",
    board[21][22] != ".",
    board[21][23] != ".",
    board[22][21] == ".",
    board[22][23] != ".",
    board[23][21] != ".",
    board[23][22] != ".",
    board[23][23] != "."]

    if all(rules):
        if (piece + 5) <= 70: 
            piece += 5
        elif (piece +5) == 71:
            piece += 5
            PurpleHome += 1
            
    rules = [board[19][21] != ".",
    board[19][22] != ".",
    board[19][23] != ".",
    board[20][21] != ".",
    board[21][21] != ".",
    board[21][22] != ".",
    board[21][23] != ".",
    board[22][21] != ".",
    board[22][23] != ".",
    board[23][21] != ".",
    board[23][22] != ".",
    board[23][23] != "."]

    if all(rules):
        if (piece + 6) <= 70: 
            piece += 6
        elif (piece +6) == 71:
            piece += 6
            PurpleHome += 1       

    if position == Purplepiece1:
        Purplepiece1 = piece
    elif position == Purplepiece2:
        Purplepiece2 = piece
    elif position == Purplepiece3:
        Purplepiece3 = piece
    elif position == Purplepiece4:
        Purplepiece4 = piece
#Read dice roll #1 and advance blue piece along game track.
def blue_read1(position):
    
    global Bluepiece1
    global Bluepiece2
    global Bluepiece3
    global Bluepiece4
    global BlueHome

    piece = position

    rules = [board[23][19] != ".",
    board[22][19] != ".",
    board[21][19] != ".",
    board[20][19] != ".",
    board[19][19] != ".",
    board[23][17] == ".",
    board[22][17] == ".",
    board[21][17] == ".",
    board[20][17] == ".",
    board[19][17] == ".",]

    if all(rules):
        if (piece + 1) <= 70: 
            piece += 1
        elif (piece +1) == 71:
            piece += 1
            BlueHome += 1
            
    rules = [board[19][17] != ".",
    board[19][18] != ".",
    board[19][19] != ".",
    board[20][19] != ".",
    board[21][17] != ".",
    board[21][18] != ".",
    board[21][19] != ".",
    board[22][17] != ".",
    board[23][17] != ".",
    board[23][18] != ".",
    board[23][19] != "."]

    if all(rules):
        if (piece + 2) <= 70: 
            piece += 2
        elif (piece +2) == 71:
            piece += 2
            BlueHome += 1
            
    rules = [board[19][17] != ".",
    board[19][18] != ".",
    board[19][19] != ".",
    board[20][19] != ".",
    board[21][17] != ".",
    board[21][18] != ".",
    board[21][19] != ".",
    board[22][19] != ".",
    board[23][17] != ".",
    board[23][18] != ".",
    board[23][19] != "."]

    if all(rules):
        if (piece + 3) <= 70: 
            piece += 3
        elif (piece +3) == 71:
            piece += 3
            BlueHome += 1
            
    rules = [board[19][17] != ".",
    board[19][19] != ".",
    board[20][17] != ".",
    board[20][19] != ".",
    board[21][17] != ".",
    board[21][18] != ".",
    board[21][19] != ".",
    board[22][19] != ".",
    board[23][19] != "."]

    if all(rules):
        if (piece + 4) <= 70: 
            piece += 4
        elif (piece +4) == 71:
            piece += 4
            BlueHome += 1
            
    rules = [board[19][17] != ".",
    board[19][18] != ".",
    board[19][19] != ".",
    board[20][17] != ".",
    board[21][17] != ".",
    board[21][18] != ".",
    board[21][19] != ".",
    board[22][17] == ".",
    board[22][19] != ".",
    board[23][17] != ".",
    board[23][18] != ".",
    board[23][19] != "."]

    if all(rules):
        if (piece + 5) <= 70: 
            piece += 5
        elif (piece +5) == 71:
            piece += 5
            BlueHome += 1
            
    rules = [board[19][17] != ".",
    board[19][18] != ".",
    board[19][19] != ".",
    board[20][17] != ".",
    board[21][17] != ".",
    board[21][18] != ".",
    board[21][19] != ".",
    board[22][17] != ".",
    board[22][19] != ".",
    board[23][17] != ".",
    board[23][18] != ".",
    board[23][19] != "."]
    if all(rules):
        if (piece + 6) <= 70: 
            piece += 6
        elif (piece +6) == 71:
            piece += 6
            BlueHome += 1
            
    if position == Bluepiece1:
        Bluepiece1 = piece
    elif position == Bluepiece2:
        Bluepiece2 = piece
    elif position == Bluepiece3:
        Bluepiece3 = piece
    elif position == Bluepiece4:
        Bluepiece4 = piece
#Read dice roll #2 and advance blue piece along game track.
def blue_read2(position):

    global Bluepiece1
    global Bluepiece2
    global Bluepiece3
    global Bluepiece4
    global BlueHome

    piece = position

    rules = [board[23][23] != ".",
    board[22][23] != ".",
    board[21][23] != ".",
    board[20][23] != ".",
    board[19][23] != ".",
    board[23][21] == ".",
    board[22][21] == ".",
    board[21][21] == ".",
    board[20][21] == ".",
    board[19][21] == ".",]

    if all(rules):
        if (piece + 1) <= 70: 
            piece += 1
        elif (piece +1) == 71:
            piece += 1
            BlueHome += 1
            

    rules = [board[19][21] != ".",
    board[19][22] != ".",
    board[19][23] != ".",
    board[20][23] != ".",
    board[21][21] != ".",
    board[21][22] != ".",
    board[21][23] != ".",
    board[22][21] != ".",
    board[23][21] != ".",
    board[23][22] != ".",
    board[23][23] != "."]

    if all(rules):
        if (piece + 2) <= 70: 
            piece += 2
        elif (piece +2) == 71:
            piece += 2
            BlueHome += 1
            

    rules = [board[19][21] != ".",
    board[19][22] != ".",
    board[19][23] != ".",
    board[20][23] != ".",
    board[21][21] != ".",
    board[21][22] != ".",
    board[21][23] != ".",
    board[22][23] != ".",
    board[23][21] != ".",
    board[23][22] != ".",
    board[23][23] != "."]

    if all(rules):
        if (piece + 3) <= 70: 
            piece += 3
        elif (piece +3) == 71:
            piece += 3
            BlueHome += 1
            

    rules = [board[19][21] != ".",
    board[19][23] != ".",
    board[20][21] != ".",
    board[20][23] != ".",
    board[21][21] != ".",
    board[21][22] != ".",
    board[21][23] != ".",
    board[22][23] != ".",
    board[23][23] != "."]

    if all(rules):
        if (piece + 4) <= 70: 
            piece += 4
        elif (piece +4) == 71:
            piece += 4
            BlueHome += 1
            

    rules = [board[19][21] != ".",
    board[19][22] != ".",
    board[19][23] != ".",
    board[20][21] != ".",
    board[21][21] != ".",
    board[21][22] != ".",
    board[21][23] != ".",
    board[22][21] == ".",
    board[22][23] != ".",
    board[23][21] != ".",
    board[23][22] != ".",
    board[23][23] != "."]

    if all(rules):
        if (piece + 5) <= 70: 
            piece += 5
        elif (piece +5) == 71:
            piece += 5
            BlueHome += 1
            

    rules = [board[19][21] != ".",
    board[19][22] != ".",
    board[19][23] != ".",
    board[20][21] != ".",
    board[21][21] != ".",
    board[21][22] != ".",
    board[21][23] != ".",
    board[22][21] != ".",
    board[22][23] != ".",
    board[23][21] != ".",
    board[23][22] != ".",
    board[23][23] != "."]

    if all(rules):
        if (piece + 6) <= 70: 
            piece += 6
        elif (piece +6) == 71:
            piece += 6
            BlueHome += 1
            

    if position == Bluepiece1:
        Bluepiece1 = piece
    elif position == Bluepiece2:
        Bluepiece2 = piece
    elif position == Bluepiece3:
        Bluepiece3 = piece
    elif position == Bluepiece4:
        Bluepiece4 = piece
#Read dice roll #1 and advance green piece along game track.
def green_read1(position):
    
    global Greenpiece1
    global Greenpiece2
    global Greenpiece3
    global Greenpiece4
    global GreenHome

    piece = position

    rules = [board[23][19] != ".",
    board[22][19] != ".",
    board[21][19] != ".",
    board[20][19] != ".",
    board[19][19] != ".",
    board[23][17] == ".",
    board[22][17] == ".",
    board[21][17] == ".",
    board[20][17] == ".",
    board[19][17] == ".",]

    if all(rules):
        if (piece + 1) <= 70: 
            piece += 1
        elif (piece +1) == 71:
            piece += 1
            GreenHome += 1
            
    rules = [board[19][17] != ".",
    board[19][18] != ".",
    board[19][19] != ".",
    board[20][19] != ".",
    board[21][17] != ".",
    board[21][18] != ".",
    board[21][19] != ".",
    board[22][17] != ".",
    board[23][17] != ".",
    board[23][18] != ".",
    board[23][19] != "."]

    if all(rules):
        if (piece + 2) <= 70: 
            piece += 2
        elif (piece +2) == 71:
            piece += 2
            GreenHome += 1
            
    rules = [board[19][17] != ".",
    board[19][18] != ".",
    board[19][19] != ".",
    board[20][19] != ".",
    board[21][17] != ".",
    board[21][18] != ".",
    board[21][19] != ".",
    board[22][19] != ".",
    board[23][17] != ".",
    board[23][18] != ".",
    board[23][19] != "."]

    if all(rules):
        if (piece + 3) <= 70: 
            piece += 3
        elif (piece +3) == 71:
            piece += 3
            GreenHome += 1
            
    rules = [board[19][17] != ".",
    board[19][19] != ".",
    board[20][17] != ".",
    board[20][19] != ".",
    board[21][17] != ".",
    board[21][18] != ".",
    board[21][19] != ".",
    board[22][19] != ".",
    board[23][19] != "."]

    if all(rules):
        if (piece + 4) <= 70: 
            piece += 4
        elif (piece +4) == 71:
            piece += 4
            GreenHome += 1
            
    rules = [board[19][17] != ".",
    board[19][18] != ".",
    board[19][19] != ".",
    board[20][17] != ".",
    board[21][17] != ".",
    board[21][18] != ".",
    board[21][19] != ".",
    board[22][17] == ".",
    board[22][19] != ".",
    board[23][17] != ".",
    board[23][18] != ".",
    board[23][19] != "."]

    if all(rules):
        if (piece + 5) <= 70: 
            piece += 5
        elif (piece +5) == 71:
            piece += 5
            GreenHome += 1
            
    rules = [board[19][17] != ".",
    board[19][18] != ".",
    board[19][19] != ".",
    board[20][17] != ".",
    board[21][17] != ".",
    board[21][18] != ".",
    board[21][19] != ".",
    board[22][17] != ".",
    board[22][19] != ".",
    board[23][17] != ".",
    board[23][18] != ".",
    board[23][19] != "."]
    if all(rules):
        if (piece + 6) <= 70: 
            piece += 6
        elif (piece +6) == 71:
            piece += 6
            GreenHome += 1
            
    if position == Greenpiece1:
        Greenpiece1 = piece
    elif position == Greenpiece2:
        Greenpiece2 = piece
    elif position == Greenpiece3:
        Greenpiece3 = piece
    elif position == Greenpiece4:
        Greenpiece4 = piece
#Read dice roll #2 and advance green piece along game track.
def green_read2(position):
    global Greenpiece1
    global Greenpiece2
    global Greenpiece3
    global Greenpiece4
    global GreenHome

    piece = position

    rules = [board[23][23] != ".",
    board[22][23] != ".",
    board[21][23] != ".",
    board[20][23] != ".",
    board[19][23] != ".",
    board[23][21] == ".",
    board[22][21] == ".",
    board[21][21] == ".",
    board[20][21] == ".",
    board[19][21] == ".",]

    if all(rules):
        if (piece + 1) <= 70: 
            piece += 1
        elif (piece +1) == 71:
            piece += 1
            GreenHome += 1
            
    rules = [board[19][21] != ".",
    board[19][22] != ".",
    board[19][23] != ".",
    board[20][23] != ".",
    board[21][21] != ".",
    board[21][22] != ".",
    board[21][23] != ".",
    board[22][21] != ".",
    board[23][21] != ".",
    board[23][22] != ".",
    board[23][23] != "."]

    if all(rules):
        if (piece + 2) <= 70: 
            piece += 2
        elif (piece +2) == 71:
            piece += 2
            GreenHome += 1
            
    rules = [board[19][21] != ".",
    board[19][22] != ".",
    board[19][23] != ".",
    board[20][23] != ".",
    board[21][21] != ".",
    board[21][22] != ".",
    board[21][23] != ".",
    board[22][23] != ".",
    board[23][21] != ".",
    board[23][22] != ".",
    board[23][23] != "."]

    if all(rules):
        if (piece + 3) <= 70: 
            piece += 3
        elif (piece +3) == 71:
            piece += 3
            GreenHome += 1
            
    rules = [board[19][21] != ".",
    board[19][23] != ".",
    board[20][21] != ".",
    board[20][23] != ".",
    board[21][21] != ".",
    board[21][22] != ".",
    board[21][23] != ".",
    board[22][23] != ".",
    board[23][23] != "."]

    if all(rules):
        if (piece + 4) <= 70: 
            piece += 4
        elif (piece +4) == 71:
            piece += 4
            GreenHome += 1
            
    rules = [board[19][21] != ".",
    board[19][22] != ".",
    board[19][23] != ".",
    board[20][21] != ".",
    board[21][21] != ".",
    board[21][22] != ".",
    board[21][23] != ".",
    board[22][21] == ".",
    board[22][23] != ".",
    board[23][21] != ".",
    board[23][22] != ".",
    board[23][23] != "."]

    if all(rules):
        if (piece + 5) <= 70: 
            piece += 5
        elif (piece +5) == 71:
            piece += 5
            GreenHome += 1
            
    rules = [board[19][21] != ".",
    board[19][22] != ".",
    board[19][23] != ".",
    board[20][21] != ".",
    board[21][21] != ".",
    board[21][22] != ".",
    board[21][23] != ".",
    board[22][21] != ".",
    board[22][23] != ".",
    board[23][21] != ".",
    board[23][22] != ".",
    board[23][23] != "."]

    if all(rules):
        if (piece + 6) <= 70: 
            piece += 6
        elif (piece +6) == 71:
            piece += 6
            GreenHome += 1
            
    if position == Greenpiece1:
        Greenpiece1 = piece
    elif position == Greenpiece2:
        Greenpiece2 = piece
    elif position == Greenpiece3:
        Greenpiece3 = piece
    elif position == Greenpiece4:
        Greenpiece4 = piece

#Read dice roll #1 and return number.
def advance1():

    rules = [board[23][19] != ".",
    board[22][19] != ".",
    board[21][19] != ".",
    board[20][19] != ".",
    board[19][19] != ".",
    board[23][17] == ".",
    board[22][17] == ".",
    board[21][17] == ".",
    board[20][17] == ".",
    board[19][17] == ".",]

    if all(rules):
        return 1

    rules = [board[19][17] != ".",
    board[19][18] != ".",
    board[19][19] != ".",
    board[20][17] == ".",
    board[20][19] != ".",
    board[21][17] != ".",
    board[21][18] != ".",
    board[21][19] != ".",
    board[22][17] != ".",
    board[22][19] == ".",
    board[23][17] != ".",
    board[23][18] != ".",
    board[23][19] != "."]

    if all(rules):
        return 2

    rules = [board[19][17] != ".",
    board[19][18] != ".",
    board[19][19] != ".",
    board[20][19] != ".",
    board[21][17] != ".",
    board[21][18] != ".",
    board[21][19] != ".",
    board[22][19] != ".",
    board[23][17] != ".",
    board[23][18] != ".",
    board[23][19] != "."]

    if all(rules):
        return 3

    rules = [board[19][17] != ".",
    board[19][19] != ".",
    board[20][17] != ".",
    board[20][19] != ".",
    board[21][17] != ".",
    board[21][18] != ".",
    board[21][19] != ".",
    board[22][19] != ".",
    board[23][19] != "."]

    if all(rules):
        return 4

    rules = [board[19][17] != ".",
    board[19][18] != ".",
    board[19][19] != ".",
    board[20][17] != ".",
    board[20][19] == ".",
    board[21][17] != ".",
    board[21][18] != ".",
    board[21][19] != ".",
    board[22][17] == ".",
    board[22][19] != ".",
    board[23][17] != ".",
    board[23][18] != ".",
    board[23][19] != "."]

    if all(rules):
        return 5

    rules = [board[19][17] != ".",
    board[19][18] != ".",
    board[19][19] != ".",
    board[20][17] != ".",
    board[20][19] == ".",
    board[21][17] != ".",
    board[21][18] != ".",
    board[21][19] != ".",
    board[22][17] != ".",
    board[22][19] != ".",
    board[23][17] != ".",
    board[23][18] != ".",
    board[23][19] != "."]
    if all(rules):
        return 6
#Read dice roll #2 and return number.
def advance2():
    
    rules = [board[23][23] != ".",
    board[22][23] != ".",
    board[21][23] != ".",
    board[20][23] != ".",
    board[19][23] != ".",
    board[23][21] == ".",
    board[22][21] == ".",
    board[21][21] == ".",
    board[20][21] == ".",
    board[19][21] == ".",]

    if all(rules):
        return 1

    rules = [board[19][21] != ".",
    board[19][22] != ".",
    board[19][23] != ".",
    board[20][21] == ".",
    board[20][23] != ".",
    board[21][21] != ".",
    board[21][22] != ".",
    board[21][23] != ".",
    board[22][21] != ".",
    board[22][23] == ".",
    board[23][21] != ".",
    board[23][22] != ".",
    board[23][23] != "."]

    if all(rules):
        return 2

    rules = [board[19][21] != ".",
    board[19][22] != ".",
    board[19][23] != ".",
    board[20][23] != ".",
    board[21][21] != ".",
    board[21][22] != ".",
    board[21][23] != ".",
    board[22][23] != ".",
    board[23][21] != ".",
    board[23][22] != ".",
    board[23][23] != "."]

    if all(rules):
        return 3

    rules = [board[19][21] != ".",
    board[19][23] != ".",
    board[20][21] != ".",
    board[20][23] != ".",
    board[21][21] != ".",
    board[21][22] != ".",
    board[21][23] != ".",
    board[22][23] != ".",
    board[23][23] != "."]

    if all(rules):
        return 4

    rules = [board[19][21] != ".",
    board[19][22] != ".",
    board[19][23] != ".",
    board[20][21] != ".",
    board[20][23] == ".",
    board[21][21] != ".",
    board[21][22] != ".",
    board[21][23] != ".",
    board[22][21] == ".",
    board[22][23] != ".",
    board[23][21] != ".",
    board[23][22] != ".",
    board[23][23] != "."]

    if all(rules):
        return 5

    rules = [board[19][21] != ".",
    board[19][22] != ".",
    board[19][23] != ".",
    board[20][21] != ".",
    board[20][23] == ".",
    board[21][21] != ".",
    board[21][22] != ".",
    board[21][23] != ".",
    board[22][21] != ".",
    board[22][23] != ".",
    board[23][21] != ".",
    board[23][22] != ".",
    board[23][23] != "."]

    if all(rules):  
        return 6

# Share safe space if occupied by other piece.
def safe_space(piece, color):
    global board

    if color == ("r"):
        x, y = game_track_red[piece]
        z, t = game_track_red2[piece]
    elif color == ("g"):
        x, y = game_track_green[piece]
        z, t = game_track_green2[piece]
    elif color == ("b"):
        x, y = game_track_blue[piece]
        z, t = game_track_blue2[piece]
    elif color == ("p"):
        x, y = game_track_purple[piece]
        z, t = game_track_purple2[piece]

    if board[z][t] in ("r", "g", "b", "p"):
        board[x][y] = color
    elif board[x][y] in ("r", "g", "b", "p"):
        board[z][t] = color  

#Check to see if there is a blockade
def bloqueo_r(number, piece):
    global Blockade
    
    if piece != None:
        for i in range (number):
        
            x, y = game_track_red[piece + i +1]
            z, t = game_track_red2[piece + i +1]

            if board[x][y] in {"r", "b", "g", "p"}:
                if board[z][t] in {"r", "b", "g", "p"}:
                    Blockade = False

            if (piece + i +1) > 71:
                Blockade = False
#Check to see if there is a blockade
def bloqueo_p(number, piece):
    global Blockade
    
    if piece != None:
        for i in range (number):
        
            x, y = game_track_purple[piece + i +1]
            z, t = game_track_purple2[piece + i +1]

            if board[x][y] in {"r", "b", "g", "p"}:
                if board[z][t] in {"r", "b", "g", "p"}:
                    Blockade = False

            if (piece + i +1) > 71:
                Blockade = False
#Check to see if there is a blockade
def bloqueo_g(number, piece):
    global Blockade
    
    if piece != None:
        for i in range (number):
        
            x, y = game_track_green[piece + i +1]
            z, t = game_track_green2[piece + i +1]

            if board[x][y] in {"r", "b", "g", "p"}:
                if board[z][t] in {"r", "b", "g", "p"}:
                    Blockade = False

            if (piece + i +1) > 71:
                Blockade = False
#Check to see if there is a blockade
def bloqueo_b(number, piece):
    global Blockade
    
    if piece != None:
        for i in range (number):
        
            x, y = game_track_blue[piece + i +1]
            z, t = game_track_blue2[piece + i +1]

            if board[x][y] in {"r", "b", "g", "p"}:
                if board[z][t] in {"r", "b", "g", "p"}:
                    Blockade = False

            if (piece + i +1) > 71:
                Blockade = False

#Randomly roll dice and bring men out onto board if a 5 is rolled.
def red_roll():
    global RedBase
    global Redpiece1
    global Redpiece2
    global Redpiece3
    global Redpiece4
    global move1_complete
    global move2_complete
    global has_rolled
    global Red_Turn
    global Purple_Turn
    global Green_Turn
    global Blue_Turn
    DiceRoll1 = random.randint (1, 6)
    DiceRoll2 = random.randint (1, 6)
    Show_num1(DiceRoll1, "r")
    Show_num2(DiceRoll2, "r")
    pygame.display.update() 

    if RedBase <= 0:
        move1_complete = False
        move2_complete = False    
        has_rolled = True 

    elif DiceRoll1 + DiceRoll2 == 5:
        move1_complete = False
        move2_complete = False
        has_rolled = True
        if (RedBase > 0):
            if board[5][10] == "s":
                clock_reset1()
                clock_reset2()
                move1_complete = True
                move2_complete = True
                has_rolled = True
                board[5][10] = "r"
                RedBase -= 1
                if RedBase == 3:
                    Redpiece1 = 0
                elif RedBase == 2:
                    Redpiece2 = 0
                elif RedBase == 1:
                    Redpiece3 = 0
                elif RedBase == 0:
                    Redpiece4 = 0
            elif board[5][9] == "s":
                clock_reset1()
                clock_reset2()
                move1_complete = True
                move2_complete = True
                has_rolled = True
                board[5][9] = "r" 
                RedBase -= 1
                if RedBase == 3:
                    Redpiece1 = 0
                elif RedBase == 2:
                    Redpiece2 = 0
                elif RedBase == 1:
                    Redpiece3 = 0
                elif RedBase == 0:
                    Redpiece4 = 0

    elif (DiceRoll1 == 5):
        move1_complete = False
        move2_complete = False
        has_rolled = True
        if (RedBase > 0):
            if board[5][10] == "s":
                clock_reset1()
                move1_complete = True
                board[5][10] = "r"
                RedBase -= 1
                if RedBase == 3:
                    Redpiece1 = 0
                elif RedBase == 2:
                    Redpiece2 = 0
                elif RedBase == 1:
                    Redpiece3 = 0
                elif RedBase == 0:
                    Redpiece4 = 0

                if (DiceRoll2 == 5):
                    if (RedBase > 0):
                        if board[5][9] == "s":
                            clock_reset2()
                            move2_complete = True
                            board[5][9] = "r"
                            RedBase -= 1
                            if RedBase == 3:
                                Redpiece1 = 0
                            elif RedBase == 2:
                                Redpiece2 = 0
                            elif RedBase == 1:
                                Redpiece3 = 0
                            elif RedBase == 0:
                                Redpiece4 = 0

            elif board[5][9] == "s":
                clock_reset1()
                move1_complete = True
                has_rolled = True
                board[5][9] = "r"
                RedBase -= 1
                if RedBase == 3:
                    Redpiece1 = 0
                elif RedBase == 2:
                    Redpiece2 = 0
                elif RedBase == 1:
                    Redpiece3 = 0
                elif RedBase == 0:
                    Redpiece4 = 0

    elif (DiceRoll2 == 5):
        move1_complete = False
        move2_complete = False
        has_rolled = True
        if (RedBase > 0):
            if board[5][10] == "s":
                clock_reset2() 
                move2_complete = True
                has_rolled = True
                board[5][10] = "r"
                RedBase -= 1
                if RedBase == 3:
                    Redpiece1 = 0
                elif RedBase == 2:
                    Redpiece2 = 0
                elif RedBase == 1:
                    Redpiece3 = 0
                elif RedBase == 0:
                    Redpiece4 = 0

            elif board[5][9] == "s":
                clock_reset2()
                move2_complete = True
                has_rolled = True
                board[5][9] = "r"
                RedBase -= 1
                if RedBase == 3:
                    Redpiece1 = 0
                elif RedBase == 2:
                    Redpiece2 = 0
                elif RedBase == 1:
                    Redpiece3 = 0
                elif RedBase == 0:
                    Redpiece4 = 0
    
    elif RedBase == 4:
        move1_complete = True
        move2_complete = True
        has_rolled = False
        Red_Turn = False
        Green_Turn = True 

    elif RedBase != 4:
        move1_complete = False
        move2_complete = False     
        has_rolled = True

    SubRBase()
#Randomly roll dice and bring men out onto board if a 5 is rolled.
def purple_roll():
    global PurpleBase
    global Purplepiece1
    global Purplepiece2
    global Purplepiece3
    global Purplepiece4
    global move1_complete
    global move2_complete
    global has_rolled
    global Red_Turn
    global Purple_Turn
    global Green_Turn
    global Blue_Turn
    DiceRoll1 = random.randint (1, 6)
    DiceRoll2 = random.randint (1, 6)
    Show_num1(DiceRoll1, "p")
    Show_num2(DiceRoll2, "p")

    if PurpleBase <= 0:
        move1_complete = False
        move2_complete = False    
        has_rolled = True 

    elif DiceRoll1 + DiceRoll2 == 5:
        move1_complete = False
        move2_complete = False
        has_rolled = True
        if (PurpleBase > 0):
            if board[18][13] == "s":
                clock_reset1()
                clock_reset2()
                move1_complete = True
                move2_complete = True
                has_rolled = True
                board[18][13] = "p"
                PurpleBase -= 1
                if PurpleBase == 3:
                    Purplepiece1 = 0
                elif PurpleBase == 2:
                    Purplepiece2 = 0
                elif PurpleBase == 1:
                    Purplepiece3 = 0
                elif PurpleBase == 0:
                    Purplepiece4 = 0

            elif board[18][14] == "s":
                clock_reset1()
                clock_reset2()
                move1_complete = True
                move2_complete = True
                has_rolled = True
                board[18][14] = "p" 
                PurpleBase -= 1
                if PurpleBase == 3:
                    Purplepiece1 = 0
                elif PurpleBase == 2:
                    Purplepiece2 = 0
                elif PurpleBase == 1:
                    Purplepiece3 = 0
                elif PurpleBase == 0:
                    Purplepiece4 = 0

    elif (DiceRoll1 == 5):
        has_rolled = True
        move1_complete = False
        move2_complete = False
        if (PurpleBase > 0):
            if board[18][13] == "s":
                clock_reset1()
                move1_complete = True
                board[18][13] = "p"
                PurpleBase -= 1
                if PurpleBase == 3:
                    Purplepiece1 = 0
                elif PurpleBase == 2:
                    Purplepiece2 = 0
                elif PurpleBase == 1:
                    Purplepiece3 = 0
                elif PurpleBase == 0:
                    Purplepiece4 = 0

                if (DiceRoll2 == 5):
                    if (PurpleBase > 0):
                        if board[18][14] == "s":
                            clock_reset2()
                            move2_complete = True
                            board[18][14] = "p"
                            PurpleBase -= 1
                            if PurpleBase == 3:
                                Purplepiece1 = 0
                            elif PurpleBase == 2:
                                Purplepiece2 = 0
                            elif PurpleBase == 1:
                                Purplepiece3 = 0
                            elif PurpleBase == 0:
                                Purplepiece4 = 0

            elif board[18][14] == "s":
                clock_reset1()
                move1_complete = True
                has_rolled = True
                board[18][14] = "p"
                PurpleBase -= 1
                if PurpleBase == 3:
                    Purplepiece1 = 0
                elif PurpleBase == 2:
                    Purplepiece2 = 0
                elif PurpleBase == 1:
                    Purplepiece3 = 0
                elif PurpleBase == 0:
                    Purplepiece4 = 0

    elif (DiceRoll2 == 5):
        move1_complete = False
        move2_complete = False
        has_rolled = True
        if (PurpleBase > 0):
            if board[18][13] == "s":
                clock_reset2() 
                move2_complete = True
                has_rolled = True
                board[18][13] = "p"
                PurpleBase -= 1
                if PurpleBase == 3:
                    Purplepiece1 = 0
                elif PurpleBase == 2:
                    Purplepiece2 = 0
                elif PurpleBase == 1:
                    Purplepiece3 = 0
                elif PurpleBase == 0:
                    Purplepiece4 = 0

            elif board[18][14] == "s":
                clock_reset2()
                move2_complete = True
                has_rolled = True
                board[18][14] = "p"
                PurpleBase -= 1
                if PurpleBase == 3:
                    Purplepiece1 = 0
                elif RedBase == 2:
                    Purplepiece2 = 0
                elif PurpleBase == 1:
                    Purplepiece3 = 0
                elif PurpleBase == 0:
                    Purplepiece4 = 0

    elif PurpleBase == 4:
        move1_complete = True
        move2_complete = True
        has_rolled = False 
        Purple_Turn = False
        Blue_Turn = True

    elif PurpleBase != 4:
        move1_complete = False
        move2_complete = False   
        has_rolled = True

    SubPBase()
#Randomly roll dice and bring men out onto board if a 5 is rolled.
def green_roll():
    global GreenBase
    global Greenpiece1
    global Greenpiece2
    global Greenpiece3
    global Greenpiece4
    global move1_complete
    global move2_complete
    global has_rolled
    global Red_Turn
    global Purple_Turn
    global Green_Turn
    global Blue_Turn
    DiceRoll1 = random.randint (1, 6)
    DiceRoll2 = random.randint (1, 6)
    Show_num1(DiceRoll1, "g")
    Show_num2(DiceRoll2, "g")

    if GreenBase <= 0:
        move1_complete = False
        move2_complete = False    
        has_rolled = True 

    elif DiceRoll1 + DiceRoll2 == 5:
        move1_complete = False
        move2_complete = False
        has_rolled = True
        if (GreenBase > 0):
            if board[13][6] == "s":
                clock_reset1()
                clock_reset2()
                move1_complete = True
                move2_complete = True
                has_rolled = True
                board[13][6] = "g"
                GreenBase -= 1
                if GreenBase == 3:
                    Greenpiece1 = 0
                elif GreenBase == 2:
                    Greenpiece2 = 0
                elif GreenBase == 1:
                    Greenpiece3 = 0
                elif GreenBase == 0:
                    Greenpiece4 = 0

            elif board[14][6] == "s":
                clock_reset1()
                clock_reset2()
                move1_complete = True
                move2_complete = True
                has_rolled = True
                board[14][6] = "g" 
                GreenBase -= 1
                if GreenBase == 3:
                    Greenpiece1 = 0
                elif GreenBase == 2:
                    Greenpiece2 = 0
                elif GreenBase == 1:
                    Greenpiece3 = 0
                elif GreenBase == 0:
                    Greenpiece4 = 0

    elif (DiceRoll1 == 5):
        has_rolled = True
        move1_complete = False
        move2_complete = False
        if (GreenBase > 0):
            if board[13][6] == "s":
                clock_reset1()
                move1_complete = True
                board[13][6] = "g"
                GreenBase -= 1
                if GreenBase == 3:
                    Greenpiece1 = 0
                elif GreenBase == 2:
                    Greenpiece2 = 0
                elif GreenBase == 1:
                    Greenpiece3 = 0
                elif GreenBase == 0:
                    Greenpiece4 = 0

                if (DiceRoll2 == 5):
                    if (GreenBase > 0):
                        if board[14][6] == "s":
                            clock_reset2()
                            move2_complete = True
                            board[14][6] = "g"
                            GreenBase -= 1
                            if GreenBase == 3:
                                Greenpiece1 = 0
                            elif GreenBase == 2:
                                Greenpiece2 = 0
                            elif GreenBase == 1:
                                Greenpiece3 = 0
                            elif GreenBase == 0:
                                Greenpiece4 = 0

            elif board[14][6] == "s":
                clock_reset1()
                move1_complete = True
                has_rolled = True
                board[14][6] = "g"
                GreenBase -= 1
                if GreenBase == 3:
                    Greenpiece1 = 0
                elif GreenBase == 2:
                    Greenpiece2 = 0
                elif GreenBase == 1:
                    Greenpiece3 = 0
                elif GreenBase == 0:
                    Greenpiece4 = 0

    elif (DiceRoll2 == 5):
        move1_complete = False
        move2_complete = False
        has_rolled = True
        if (GreenBase > 0):
            if board[13][6] == "s":
                clock_reset2() 
                move2_complete = True
                has_rolled = True
                board[13][6] = "g"
                GreenBase -= 1
                if GreenBase == 3:
                    Greenpiece1 = 0
                elif GreenBase == 2:
                    Greenpiece2 = 0
                elif GreenBase == 1:
                    Greenpiece3 = 0
                elif GreenBase == 0:
                    Greenpiece4 = 0

            elif board[14][6] == "s":
                clock_reset2()
                move2_complete = True
                has_rolled = True
                board[14][6] = "g"
                GreenBase -= 1
                if GreenBase == 3:
                    Greenpiece1 = 0
                elif GreenBase == 2:
                    Greenpiece2 = 0
                elif GreenBase == 1:
                    Greenpiece3 = 0
                elif GreenBase == 0:
                    Greenpiece4 = 0

    elif GreenBase == 4:
        move1_complete = True
        move2_complete = True
        has_rolled = False 
        Green_Turn = False
        Purple_Turn = True

    elif GreenBase != 4:
        move1_complete = False
        move2_complete = False   
        has_rolled = True

    SubGBase()
#Randomly roll dice and bring men out onto board if a 5 is rolled.
def blue_roll():
    global BlueBase
    global Bluepiece1
    global Bluepiece2
    global Bluepiece3
    global Bluepiece4
    global move1_complete
    global move2_complete
    global has_rolled
    global Red_Turn
    global Purple_Turn
    global Green_Turn
    global Blue_Turn
    DiceRoll1 = random.randint (1, 6)
    DiceRoll2 = random.randint (1, 6)
    Show_num1(DiceRoll1, "b")
    Show_num2(DiceRoll2, "b")

    if BlueBase <= 0:
        move1_complete = False
        move2_complete = False    
        has_rolled = True 

    elif DiceRoll1 + DiceRoll2 == 5:
        move1_complete = False
        move2_complete = False
        has_rolled = True
        if (BlueBase > 0):
            if board[10][17] == "s":
                clock_reset1()
                clock_reset2()
                move1_complete = True
                move2_complete = True
                has_rolled = True
                board[10][17] = "b"
                BlueBase -= 1
                if BlueBase == 3:
                    Bluepiece1 = 0
                elif BlueBase == 2:
                    Bluepiece2 = 0
                elif BlueBase == 1:
                    Bluepiece3 = 0
                elif BlueBase == 0:
                    Bluepiece4 = 0

            elif board[9][17] == "s":
                clock_reset1()
                clock_reset2()
                move1_complete = True
                move2_complete = True
                has_rolled = True
                board[9][17] = "b" 
                BlueBase -= 1
                if BlueBase == 3:
                    Bluepiece1 = 0
                elif BlueBase == 2:
                    Bluepiece2 = 0
                elif BlueBase == 1:
                    Bluepiece3 = 0
                elif BlueBase == 0:
                    Bluepiece4 = 0

    elif (DiceRoll1 == 5):
        has_rolled = True
        move1_complete = False
        move2_complete = False
        if (BlueBase > 0):
            if board[10][17] == "s":
                clock_reset1()
                move1_complete = True
                board[10][17] = "b"
                BlueBase -= 1
                if BlueBase == 3:
                    Bluepiece1 = 0
                elif BlueBase == 2:
                    Bluepiece2 = 0
                elif BlueBase == 1:
                    Bluepiece3 = 0
                elif BlueBase == 0:
                    Bluepiece4 = 0

                if (DiceRoll2 == 5):
                    if (BlueBase > 0):
                        if board[9][17] == "s":
                            clock_reset2()
                            move2_complete = True
                            board[9][17] = "b"
                            BlueBase -= 1
                            if BlueBase == 3:
                                Bluepiece1 = 0
                            elif BlueBase == 2:
                                Bluepiece2 = 0
                            elif BlueBase == 1:
                                Bluepiece3 = 0
                            elif BlueBase == 0:
                                Bluepiece4 = 0

            elif board[9][17] == "s":
                clock_reset1()
                move1_complete = True
                has_rolled = True
                board[9][17] = "b"
                BlueBase -= 1
                if BlueBase == 3:
                    Bluepiece1 = 0
                elif BlueBase == 2:
                    Bluepiece2 = 0
                elif BlueBase == 1:
                    Bluepiece3 = 0
                elif BlueBase == 0:
                    Bluepiece4 = 0

    elif (DiceRoll2 == 5):
        move1_complete = False
        move2_complete = False
        has_rolled = True
        if (BlueBase > 0):
            if board[10][17] == "s":
                clock_reset2() 
                move2_complete = True
                has_rolled = True
                board[10][17] = "b"
                BlueBase -= 1
                if BlueBase == 3:
                    Bluepiece1 = 0
                elif BlueBase == 2:
                    Bluepiece2 = 0
                elif BlueBase == 1:
                    Bluepiece3 = 0
                elif BlueBase == 0:
                    Bluepiece4 = 0

            elif board[9][17] == "s":
                clock_reset2()
                move2_complete = True
                has_rolled = True
                board[9][17] = "b"
                BlueBase -= 1
                if BlueBase == 3:
                    Bluepiece1 = 0
                elif BlueBase == 2:
                    Bluepiece2 = 0
                elif BlueBase == 1:
                    Bluepiece3 = 0
                elif BlueBase == 0:
                    Bluepiece4 = 0

    elif BlueBase == 4:
        move1_complete = True
        move2_complete = True
        has_rolled = False 
        Blue_Turn = False
        Red_Turn = True

    elif BlueBase != 4:
        move1_complete = False
        move2_complete = False   
        has_rolled = True

    SubBBase()

#Delete piece before advancing
def delete_piece(piece, color):
    global Redpiece1
    global Redpiece2
    global Redpiece3
    global Redpiece4

    global Purplepiece1
    global Purplepiece2
    global Purplepiece3
    global Purplepiece4

    global Greenpiece1
    global Greenpiece2
    global Greenpiece3
    global Greenpiece4

    global Bluepiece1
    global Bluepiece2
    global Bluepiece3
    global Bluepiece4
    
    global board

    if color == "r":
        x, y = game_track_red[piece]
        z, t = game_track_red2[piece]
    elif color == "p":
        x, y = game_track_purple[piece]
        z, t = game_track_purple2[piece]
    elif color == "g":
        x, y = game_track_green[piece]
        z, t = game_track_green2[piece]
    elif color == "b":
        x, y = game_track_blue[piece]
        z, t = game_track_blue2[piece]
    

    if board[x][y] == color:
        if (x, y) in {(1, 11), (1, 12), (5, 9), (5, 10), (5, 13), (5, 14), (9, 6), (9, 17), (10, 6), (10, 17), (11, 2), (11, 21), (12, 2), (12, 21), (13, 6), (13, 17), (14, 6), (14, 17), (18, 9), (18, 10), (18, 13), (18, 14), (22, 11), (22, 12)}:
            board[x][y] = "s"
        elif (x,y) in {(2,12), (3,12), (4,12), (5,12), (6,12), (7,12), (8,12), (2,11), (1,11), (2,11), (3,11), (4,11), (5,11), (6,11), (7,11), (8,11), (5,9), (5,10)}:
            board[x][y] = "t"
        elif (x,y) in {(10,5), (10,4), (10,3), (10,2), (13,2), (13,3), (13,4), (13,5), (13,6), (13,7), (13,8), (13,9), (15,9), (16,9), (17,9), (19,9), (20,9), (21,9), (22,9), (22,13), (21,13), (20,13), (19,13), (17,13), (16,13), (15,13), (14,14), (14,15), (14,16), (14,17), (14,18), (14,19), (14,20), (14,21), (10,21), (10,20), (10,19), (10,18), (10,16), (10,15), (10,14), (8,14), (7,14), (6,14), (4,14), (3,14), (2,14), (1,14), (2,12), (3,12), (4,12), (5,12), (6,12), (7,12), (8,12), (1, 10), (2,10), (3,10), (4,10), (6,10), (7,10), (8,10), (10,9), (10,8), (10,7)}:
            board[x][y] = "x"
        elif (x,y) in {(22,11), (21,11), (20,11), (19,11), (18,11), (17,11), (16,11), (15,11), (21,11), (20,11), (19,11), (18,11), (17,11), (16,11), (15,11)}:
            board[x][y] = "j"
        elif (x,y) in {(12,3), (12,4), (12,5), (12,6), (12,7), (12,8), (12,9), (11,3), (11,4), (11,5), (11,6), (11,7), (11,8), (11,9)}:
            board[x][y] = "q"
        elif (x,y) in {(12,20), (12,19), (12,18), (12,17), (12,16), (12,15), (12,14), (11,20), (11,19), (11,18), (11,17), (11,16), (11,15), (11,14)}:
            board[x][y] = "w"

    elif board[z][t] == color:
        if (z, t) in {(1, 11), (1, 12), (5, 9), (5, 10), (5, 13), (5, 14), (9, 6), (9, 17), (10, 6), (10, 17), (11, 2), (11, 21), (12, 2), (12, 21), (13, 6), (13, 17), (14, 6), (14, 17), (18, 9), (18, 10), (18, 13), (18, 14), (22, 11), (22, 12)}:
            board[z][t] = "s"
        elif (z,t) in {(2,12), (3,12), (4,12), (5,12), (6,12), (7,12), (8,12), (2,11), (1,11), (2,11), (3,11), (4,11), (5,11), (6,11), (7,11), (8,11), (5,9), (5,10)}:
            board[z][t] = "t"
        elif (z,t) in {(9,5), (9,4), (9,3), (9,2), (14,2), (14,3), (14,4), (14,5), (14,7), (14,8), (14,9), (15,10), (16,10), (17,10), (19,10), (20,10), (21,10), (22,10), (22,14), (21,14), (20,14), (19,14), (17,14), (16,14), (15,14), (13,14), (13,15), (13,16), (13,18), (13,19), (13,20), (13,21), (9,21), (9,20), (9,19), (9,18), (9,16), (9,15), (9,14), (8,13), (7,13), (6,13), (4,13), (3,13), (2,13), (1,13), (2,11), (3,11), (4,11), (5,11), (6,11), (7,11), (8,11), (1,9), (2,9), (3,9), (4,9), (6,9), (7,9), (8,9), (9,9), (9,8), (9,7)}:
            board[z][t] = "x"
        elif (z,t) in {(22,12), (21,12), (20,12), (19,12), (18,12), (17,12), (16,12), (15,12), (21,12), (20,12), (19,12), (18,12), (17,12), (16,12), (15,12)}:
            board[z][t] = "j"
        elif (z,t) in {(12,3), (12,4), (12,5), (12,6), (12,7), (12,8), (12,9), (11,3), (11,4), (11,5), (11,6), (11,7), (11,8), (11,9)}:
            board[z][t] = "q"
        elif (z,t) in {(12,20), (12,19), (12,18), (12,17), (12,16), (12,15), (12,14), (11,20), (11,19), (11,18), (11,17), (11,16), (11,15), (11,14)}:
            board[z][t] = "w"

#Print piece in new position acording to the dice roll.          
def move_forward_red(piece):
    global BlueBase
    global BlueBase
    global BlueHome
    global PurpleBase
    global PurpleHome
    global GreenBase
    global GreenHome
    global RedBase
    global RedHome

    global Bluepiece1
    global Bluepiece2
    global Bluepiece3
    global Bluepiece4

    global Purplepiece1
    global Purplepiece2
    global Purplepiece3
    global Purplepiece4

    global Greenpiece1
    global Greenpiece2
    global Greenpiece3
    global Greenpiece4

    global Redpiece1
    global Redpiece2
    global Redpiece3
    global Redpiece4


    if (piece) <= 70:

        x, y = game_track_red[piece]
        z, t = game_track_red2[piece]

        if board [x][y] == "r":
            safe_space(piece, "r")

        elif board [z][t] == "r":
            safe_space(piece, "r")


        elif board [x][y] == "g":
            if (x, y) not in {(1, 11), (1, 12), (5, 9), (5, 10), (5, 13), (5, 14), (9, 6), (9, 17), (10, 6), (10, 17), (11, 2), (11, 21), (12, 2), (12, 21), (13, 6), (13, 17), (14, 6), (14, 17), (18, 9), (18, 10), (18, 13), (18, 14), (22, 11), (22, 12)}:
                board [x][y] = "r"
                GreenBase +=1
                SubGBase()
                if (game_track_green[Greenpiece1]) == [x, y]:
                    Greenpiece1 = None
                elif (game_track_green[Greenpiece2]) == [x, y]:
                    Greenpiece2 = None
                elif (game_track_green[Greenpiece3]) == [x, y]:
                    Greenpiece3 = None
                elif (game_track_green[Greenpiece4]) == [x, y]:
                    Greenpiece4 = None
            else:
                safe_space(piece, "r")

        elif board [z][t] == "g":
            if (z, t) not in {(1, 11), (1, 12), (5, 9), (5, 10), (5, 13), (5, 14), (9, 6), (9, 17), (10, 6), (10, 17), (11, 2), (11, 21), (12, 2), (12, 21), (13, 6), (13, 17), (14, 6), (14, 17), (18, 9), (18, 10), (18, 13), (18, 14), (22, 11), (22, 12)}:
                board [z][t] = "r"
                GreenBase +=1
                SubGBase()
                if (game_track_green2[Greenpiece1]) == [z, t]:
                    Greenpiece1 = None
                elif (game_track_green2[Greenpiece2]) == [z, t]:
                    Greenpiece2 = None
                elif (game_track_green2[Greenpiece3]) == [z, t]:
                    Greenpiece3 = None
                elif (game_track_green2[Greenpiece4]) == [z, t]:
                    Greenpiece4 = None
            else:
                safe_space(piece, "r")

        elif board [x][y] == "p":
            if (x, y) not in {(1, 11), (1, 12), (5, 9), (5, 10), (5, 13), (5, 14), (9, 6), (9, 17), (10, 6), (10, 17), (11, 2), (11, 21), (12, 2), (12, 21), (13, 6), (13, 17), (14, 6), (14, 17), (18, 9), (18, 10), (18, 13), (18, 14), (22, 11), (22, 12)}:
                board [x][y] = "r"
                PurpleBase +=1
                SubPBase()
                if (game_track_purple[Purplepiece1]) == [x, y]:
                    Purplepiece1 = None
                elif (game_track_purple[Purplepiece2]) == [x, y]:
                    Purplepiece2 = None
                elif (game_track_purple[Purplepiece3]) == [x, y]:
                    Purplepiece3 = None
                elif (game_track_purple[Purplepiece4]) == [x, y]:
                    Purplepiece4 = None
            else:
                safe_space(piece, "r")

        elif board [z][t] == "p":
            if (z, t) not in {(1, 11), (1, 12), (5, 9), (5, 10), (5, 13), (5, 14), (9, 6), (9, 17), (10, 6), (10, 17), (11, 2), (11, 21), (12, 2), (12, 21), (13, 6), (13, 17), (14, 6), (14, 17), (18, 9), (18, 10), (18, 13), (18, 14), (22, 11), (22, 12)}:
                board [z][t] = "r"
                PurpleBase +=1
                SubPBase()
                if (game_track_purple2[Purplepiece1]) == [z, t]:
                    Purplepiece1 = None
                elif (game_track_purple2[Purplepiece2]) == [z, t]:
                    Purplepiece2 = None
                elif (game_track_purple2[Purplepiece3]) == [z, t]:
                    Purplepiece3 = None
                elif (game_track_purple2[Purplepiece4]) == [z, t]:
                    Purplepiece4 = None
            else:
                safe_space(piece, "r")

        elif board [x][y] == "b":
            if (x, y) not in {(1, 11), (1, 12), (5, 9), (5, 10), (5, 13), (5, 14), (9, 6), (9, 17), (10, 6), (10, 17), (11, 2), (11, 21), (12, 2), (12, 21), (13, 6), (13, 17), (14, 6), (14, 17), (18, 9), (18, 10), (18, 13), (18, 14), (22, 11), (22, 12)}:
                board [x][y] = "r"
                BlueBase +=1
                SubBBase()
                if (game_track_blue[Bluepiece1]) == [x, y]:
                    Bluepiece1 =  None
                elif (game_track_blue[Bluepiece2]) == [x, y]:
                    Bluepiece2 =  None
                elif (game_track_blue[Bluepiece3]) == [x, y]:
                    Redpiece3 = None
                elif (game_track_blue[Bluepiece4]) == [x, y]:
                    Bluepiece4 = None
            else:
                safe_space(piece, "r")

        elif board [z][t] == "b":
            if (z, t) not in {(1, 11), (1, 12), (5, 9), (5, 10), (5, 13), (5, 14), (9, 6), (9, 17), (10, 6), (10, 17), (11, 2), (11, 21), (12, 2), (12, 21), (13, 6), (13, 17), (14, 6), (14, 17), (18, 9), (18, 10), (18, 13), (18, 14), (22, 11), (22, 12)}:
                board [z][t] = "r"
                BlueBase +=1
                SubBBase() 
                if (game_track_blue[Bluepiece1]) == [z, t]:
                    Bluepiece1 =  None
                elif (game_track_blue[Bluepiece2]) == [z, t]:
                    Bluepiece2 =  None
                elif (game_track_blue[Bluepiece3]) == [z, t]:
                    Redpiece3 = None
                elif (game_track_blue[Bluepiece4]) == [z, t]:
                    Bluepiece4 = None
            else:
                safe_space(piece, "r")
        
        else:
            x, y = game_track_red[piece]
            board[x][y] = "r"
#Print piece in new position acording to the dice roll.          
def move_forward_purple(piece):
    global BlueBase
    global BlueBase
    global BlueHome
    global PurpleBase
    global PurpleHome
    global GreenBase
    global GreenHome
    global RedBase
    global RedHome

    global Bluepiece1
    global Bluepiece2
    global Bluepiece3
    global Bluepiece4

    global Purplepiece1
    global Purplepiece2
    global Purplepiece3
    global Purplepiece4

    global Greenpiece1
    global Greenpiece2
    global Greenpiece3
    global Greenpiece4

    global Redpiece1
    global Redpiece2
    global Redpiece3
    global Redpiece4

    if (piece) <= 70:

        x, y = game_track_purple[piece]
        z, t = game_track_purple2[piece]

        if board [x][y] == "p":
            safe_space(piece, "p")

        elif board [z][t] == "p":
            safe_space(piece, "p")


        elif board [x][y] == "g":
            if (x, y) not in {(1, 11), (1, 12), (5, 9), (5, 10), (5, 13), (5, 14), (9, 6), (9, 17), (10, 6), (10, 17), (11, 2), (11, 21), (12, 2), (12, 21), (13, 6), (13, 17), (14, 6), (14, 17), (18, 9), (18, 10), (18, 13), (18, 14), (22, 11), (22, 12)}:
                board [x][y] = "p"
                GreenBase +=1
                SubGBase()
                if (game_track_green[Greenpiece1]) == [x, y]:
                    Greenpiece1 = None
                elif (game_track_green[Greenpiece2]) == [x, y]:
                    Greenpiece2 = None
                elif (game_track_green[Greenpiece3]) == [x, y]:
                    Greenpiece3 = None
                elif (game_track_green[Greenpiece4]) == [x, y]:
                    Greenpiece4 = None
            else:
                safe_space(piece, "p")

        elif board [z][t] == "g":
            if (z, t) not in {(1, 11), (1, 12), (5, 9), (5, 10), (5, 13), (5, 14), (9, 6), (9, 17), (10, 6), (10, 17), (11, 2), (11, 21), (12, 2), (12, 21), (13, 6), (13, 17), (14, 6), (14, 17), (18, 9), (18, 10), (18, 13), (18, 14), (22, 11), (22, 12)}:
                board [z][t] = "p"
                GreenBase +=1
                SubGBase()
                if (game_track_green2[Greenpiece1]) == [z, t]:
                    Greenpiece1 = None
                elif (game_track_green2[Greenpiece2]) == [z, t]:
                    Greenpiece2 = None
                elif (game_track_green2[Greenpiece3]) == [z, t]:
                    Greenpiece3 = None
                elif (game_track_green2[Greenpiece4]) == [z, t]:
                    Greenpiece4 = None
            else:
                safe_space(piece, "p")

        elif board [x][y] == "r":
            if (x, y) not in {(1, 11), (1, 12), (5, 9), (5, 10), (5, 13), (5, 14), (9, 6), (9, 17), (10, 6), (10, 17), (11, 2), (11, 21), (12, 2), (12, 21), (13, 6), (13, 17), (14, 6), (14, 17), (18, 9), (18, 10), (18, 13), (18, 14), (22, 11), (22, 12)}:
                board [x][y] = "p"
                RedBase +=1
                SubRBase()
                if (game_track_red[Redpiece1]) == [x, y]:
                    Redpiece1 = None
                elif (game_track_red[Redpiece2]) == [x, y]:
                    Redpiece2 = None
                elif (game_track_red[Redpiece3]) == [x, y]:
                    Redpiece3 =  None
                elif (game_track_red[Redpiece4]) == [x, y]:
                    Redpiece4 = None
            else:
                safe_space(piece, "p")

        elif board [z][t] == "r":
            if (z, t) not in {(1, 11), (1, 12), (5, 9), (5, 10), (5, 13), (5, 14), (9, 6), (9, 17), (10, 6), (10, 17), (11, 2), (11, 21), (12, 2), (12, 21), (13, 6), (13, 17), (14, 6), (14, 17), (18, 9), (18, 10), (18, 13), (18, 14), (22, 11), (22, 12)}:
                board [z][t] = "p"
                RedBase +=1
                SubRBase()
                if (game_track_red2[Redpiece1]) == [z, t]:
                    Redpiece1 =  None
                elif (game_track_red2[Redpiece2]) == [z, t]:
                    Redpiece2 =  None
                elif (game_track_red2[Redpiece3]) == [z, t]:
                    Redpiece3 = None
                elif (game_track_red2[Redpiece4]) == [z, t]:
                    Redpiece4 = None
            else:
                safe_space(piece, "p")

        elif board [x][y] == "b":
            if (x, y) not in {(1, 11), (1, 12), (5, 9), (5, 10), (5, 13), (5, 14), (9, 6), (9, 17), (10, 6), (10, 17), (11, 2), (11, 21), (12, 2), (12, 21), (13, 6), (13, 17), (14, 6), (14, 17), (18, 9), (18, 10), (18, 13), (18, 14), (22, 11), (22, 12)}:
                board [x][y] = "p"
                BlueBase +=1
                SubBBase()
                if (game_track_blue[Bluepiece1]) == [x, y]:
                    Bluepiece1 =  None
                elif (game_track_blue[Bluepiece2]) == [x, y]:
                    Bluepiece2 =  None
                elif (game_track_blue[Bluepiece3]) == [x, y]:
                    Bluepiece3 = None
                elif (game_track_blue[Bluepiece4]) == [x, y]:
                    Bluepiece4 = None
            else:
                safe_space(piece, "p")

        elif board [z][t] == "b":
            if (z, t) not in {(1, 11), (1, 12), (5, 9), (5, 10), (5, 13), (5, 14), (9, 6), (9, 17), (10, 6), (10, 17), (11, 2), (11, 21), (12, 2), (12, 21), (13, 6), (13, 17), (14, 6), (14, 17), (18, 9), (18, 10), (18, 13), (18, 14), (22, 11), (22, 12)}:
                board [z][t] = "p"
                BlueBase +=1
                SubBBase()
                if (game_track_blue2[Bluepiece1]) == [z, t]:
                    Bluepiece1 =  None
                elif (game_track_blue2[Bluepiece2]) == [z, t]:
                    Bluepiece2 =  None
                elif (game_track_blue2[Bluepiece3]) == [z, t]:
                    Bluepiece3 = None
                elif (game_track_blue2[Bluepiece4]) == [z, t]:
                    Bluepiece4 = None
            else:
                safe_space(piece, "p")
        
        else:
            x, y = game_track_purple[piece]
            board[x][y] = "p"
#Print piece in new position acording to the dice roll.          
def move_forward_green(piece):
    global BlueBase
    global BlueBase
    global BlueHome
    global PurpleBase
    global PurpleHome
    global GreenBase
    global GreenHome
    global RedBase
    global RedHome

    global Bluepiece1
    global Bluepiece2
    global Bluepiece3
    global Bluepiece4

    global Purplepiece1
    global Purplepiece2
    global Purplepiece3
    global Purplepiece4

    global Greenpiece1
    global Greenpiece2
    global Greenpiece3
    global Greenpiece4

    global Redpiece1
    global Redpiece2
    global Redpiece3
    global Redpiece4

    if (piece) <= 70:

        x, y = game_track_green[piece]
        z, t = game_track_green2[piece]

        if board [x][y] == "g":
            safe_space(piece, "g")

        elif board [z][t] == "g":
            safe_space(piece, "g")


        elif board [x][y] == "p":
            if (x, y) not in {(1, 11), (1, 12), (5, 9), (5, 10), (5, 13), (5, 14), (9, 6), (9, 17), (10, 6), (10, 17), (11, 2), (11, 21), (12, 2), (12, 21), (13, 6), (13, 17), (14, 6), (14, 17), (18, 9), (18, 10), (18, 13), (18, 14), (22, 11), (22, 12)}:
                board [x][y] = "g"
                PurpleBase +=1
                SubGBase()
                if (game_track_purple[Purplepiece1]) == [x, y]:
                    Purplepiece1 = None
                elif (game_track_purple[Purplepiece2]) == [x, y]:
                    Purplepiece2 = None
                elif (game_track_purple[Purplepiece3]) == [x, y]:
                    Purplepiece3 =  None
                elif (game_track_purple[Purplepiece4]) == [x, y]:
                    Purplepiece4 = None
            else:
                safe_space(piece, "g")

        elif board [z][t] == "p":
            if (z, t) not in {(1, 11), (1, 12), (5, 9), (5, 10), (5, 13), (5, 14), (9, 6), (9, 17), (10, 6), (10, 17), (11, 2), (11, 21), (12, 2), (12, 21), (13, 6), (13, 17), (14, 6), (14, 17), (18, 9), (18, 10), (18, 13), (18, 14), (22, 11), (22, 12)}:
                board [x][y] = "g"
                PurpleBase +=1
                SubGBase()
                if (game_track_purple2[Purplepiece1]) == [z, t]:
                    Purplepiece1 = None
                elif (game_track_purple2[Purplepiece2]) == [z, t]:
                    Purplepiece2 = None
                elif (game_track_purple2[Purplepiece3]) == [z, t]:
                    Purplepiece3 =  None
                elif (game_track_purple2[Purplepiece4]) == [z, t]:
                    Purplepiece4 = None
            else:
                safe_space(piece, "g")

        elif board [x][y] == "r":
            if (x, y) not in {(1, 11), (1, 12), (5, 9), (5, 10), (5, 13), (5, 14), (9, 6), (9, 17), (10, 6), (10, 17), (11, 2), (11, 21), (12, 2), (12, 21), (13, 6), (13, 17), (14, 6), (14, 17), (18, 9), (18, 10), (18, 13), (18, 14), (22, 11), (22, 12)}:
                board [x][y] = "g"
                RedBase +=1
                SubRBase()
                if (game_track_red[Redpiece1]) == [x, y]:
                    Redpiece1 = None
                elif (game_track_red[Redpiece2]) == [x, y]:
                    Redpiece2 = None
                elif (game_track_red[Redpiece3]) == [x, y]:
                    Redpiece3 =  None
                elif (game_track_red[Redpiece4]) == [x, y]:
                    Redpiece4 = None
            else:
                safe_space(piece, "g")

        elif board [z][t] == "r":
            if (z, t) not in {(1, 11), (1, 12), (5, 9), (5, 10), (5, 13), (5, 14), (9, 6), (9, 17), (10, 6), (10, 17), (11, 2), (11, 21), (12, 2), (12, 21), (13, 6), (13, 17), (14, 6), (14, 17), (18, 9), (18, 10), (18, 13), (18, 14), (22, 11), (22, 12)}:
                board [z][t] = "g"
                RedBase +=1
                SubRBase()
                if (game_track_red2[Redpiece1]) == [z, t]:
                    Redpiece1 =  None
                elif (game_track_red2[Redpiece2]) == [z, t]:
                    Redpiece2 =  None
                elif (game_track_red2[Redpiece3]) == [z, t]:
                    Redpiece3 = None
                elif (game_track_red2[Redpiece4]) == [z, t]:
                    Redpiece4 = None
            else:
                safe_space(piece, "g")

        elif board [x][y] == "b":
            if (x, y) not in {(1, 11), (1, 12), (5, 9), (5, 10), (5, 13), (5, 14), (9, 6), (9, 17), (10, 6), (10, 17), (11, 2), (11, 21), (12, 2), (12, 21), (13, 6), (13, 17), (14, 6), (14, 17), (18, 9), (18, 10), (18, 13), (18, 14), (22, 11), (22, 12)}:
                board [x][y] = "g"
                BlueBase +=1
                SubBBase()
                if (game_track_blue[Bluepiece1]) == [x, y]:
                    Bluepiece1 =  None
                elif (game_track_blue[Bluepiece2]) == [x, y]:
                    Bluepiece2 =  None
                elif (game_track_blue[Bluepiece3]) == [x, y]:
                    Bluepiece3 = None
                elif (game_track_blue[Bluepiece4]) == [x, y]:
                    Bluepiece4 = None
            else:
                safe_space(piece, "g")

        elif board [z][t] == "b":
            if (z, t) not in {(1, 11), (1, 12), (5, 9), (5, 10), (5, 13), (5, 14), (9, 6), (9, 17), (10, 6), (10, 17), (11, 2), (11, 21), (12, 2), (12, 21), (13, 6), (13, 17), (14, 6), (14, 17), (18, 9), (18, 10), (18, 13), (18, 14), (22, 11), (22, 12)}:
                board [z][t] = "g"
                BlueBase +=1
                SubBBase()
                if (game_track_blue2[Bluepiece1]) == [z, t]:
                    Bluepiece1 =  None
                elif (game_track_blue2[Bluepiece2]) == [z, t]:
                    Bluepiece2 =  None
                elif (game_track_blue2[Bluepiece3]) == [z, t]:
                    Bluepiece3 = None
                elif (game_track_blue2[Bluepiece4]) == [z, t]:
                    Bluepiece4 = None
            else:
                safe_space(piece, "g")
        
        else:
            x, y = game_track_green[piece]
            board[x][y] = "g"
#Print piece in new position acording to the dice roll.          
def move_forward_blue(piece):
    global BlueBase
    global BlueHome
    global PurpleBase
    global PurpleHome
    global GreenBase
    global GreenHome
    global RedBase
    global RedHome

    global Bluepiece1
    global Bluepiece2
    global Bluepiece3
    global Bluepiece4

    global Purplepiece1
    global Purplepiece2
    global Purplepiece3
    global Purplepiece4

    global Greenpiece1
    global Greenpiece2
    global Greenpiece3
    global Greenpiece4

    global Redpiece1
    global Redpiece2
    global Redpiece3
    global Redpiece4

    if (piece) <= 70:

        x, y = game_track_blue[piece]
        z, t = game_track_blue2[piece]

        if board [x][y] == "b":
            safe_space(piece, "b")

        elif board [z][t] == "b":
            safe_space(piece, "b")


        elif board [x][y] == "p":
            if (x, y) not in {(1, 11), (1, 12), (5, 9), (5, 10), (5, 13), (5, 14), (9, 6), (9, 17), (10, 6), (10, 17), (11, 2), (11, 21), (12, 2), (12, 21), (13, 6), (13, 17), (14, 6), (14, 17), (18, 9), (18, 10), (18, 13), (18, 14), (22, 11), (22, 12)}:
                board [x][y] = "b"
                PurpleBase +=1
                SubPBase()
                if (game_track_purple[Purplepiece1]) == [x, y]:
                    Purplepiece1 = None
                elif (game_track_purple[Purplepiece2]) == [x, y]:
                    Purplepiece2 = None
                elif (game_track_purple[Purplepiece3]) == [x, y]:
                    Purplepiece3 =  None
                elif (game_track_purple[Purplepiece4]) == [x, y]:
                    Purplepiece4 = None
            else:
                safe_space(piece, "b")

        elif board [z][t] == "p":
            if (z, t) not in {(1, 11), (1, 12), (5, 9), (5, 10), (5, 13), (5, 14), (9, 6), (9, 17), (10, 6), (10, 17), (11, 2), (11, 21), (12, 2), (12, 21), (13, 6), (13, 17), (14, 6), (14, 17), (18, 9), (18, 10), (18, 13), (18, 14), (22, 11), (22, 12)}:
                board [x][y] = "b"
                PurpleBase +=1
                SubPBase()
                if (game_track_purple2[Purplepiece1]) == [z, t]:
                    Purplepiece1 = None
                elif (game_track_purple2[Purplepiece2]) == [z, t]:
                    Purplepiece2 = None
                elif (game_track_purple2[Purplepiece3]) == [z, t]:
                    Purplepiece3 =  None
                elif (game_track_purple2[Purplepiece4]) == [z, t]:
                    Purplepiece4 = None
            else:
                safe_space(piece, "b")

        elif board [x][y] == "r":
            if (x, y) not in {(1, 11), (1, 12), (5, 9), (5, 10), (5, 13), (5, 14), (9, 6), (9, 17), (10, 6), (10, 17), (11, 2), (11, 21), (12, 2), (12, 21), (13, 6), (13, 17), (14, 6), (14, 17), (18, 9), (18, 10), (18, 13), (18, 14), (22, 11), (22, 12)}:
                board [x][y] = "b"
                RedBase +=1
                SubRBase()
                if (game_track_red[Redpiece1]) == [x, y]:
                    Redpiece1 = None
                elif (game_track_red[Redpiece2]) == [x, y]:
                    Redpiece2 = None
                elif (game_track_red[Redpiece3]) == [x, y]:
                    Redpiece3 =  None
                elif (game_track_red[Redpiece4]) == [x, y]:
                    Redpiece4 = None
            else:
                safe_space(piece, "b")

        elif board [z][t] == "r":
            if (z, t) not in {(1, 11), (1, 12), (5, 9), (5, 10), (5, 13), (5, 14), (9, 6), (9, 17), (10, 6), (10, 17), (11, 2), (11, 21), (12, 2), (12, 21), (13, 6), (13, 17), (14, 6), (14, 17), (18, 9), (18, 10), (18, 13), (18, 14), (22, 11), (22, 12)}:
                board [z][t] = "b"
                RedBase +=1
                SubRBase()
                if (game_track_red2[Redpiece1]) == [z, t]:
                    Redpiece1 =  None
                elif (game_track_red2[Redpiece2]) == [z, t]:
                    Redpiece2 =  None
                elif (game_track_red2[Redpiece3]) == [z, t]:
                    Redpiece3 = None
                elif (game_track_red2[Redpiece4]) == [z, t]:
                    Redpiece4 = None
            else:
                safe_space(piece, "b")

        elif board [x][y] == "g":
            if (x, y) not in {(1, 11), (1, 12), (5, 9), (5, 10), (5, 13), (5, 14), (9, 6), (9, 17), (10, 6), (10, 17), (11, 2), (11, 21), (12, 2), (12, 21), (13, 6), (13, 17), (14, 6), (14, 17), (18, 9), (18, 10), (18, 13), (18, 14), (22, 11), (22, 12)}:
                board [x][y] = "b"
                GreenBase +=1
                SubGBase()
                if (game_track_green[Greenpiece1]) == [x, y]:
                    Greenpiece1 = None
                elif (game_track_green[Greenpiece2]) == [x, y]:
                    Greenpiece2 = None
                elif (game_track_green[Greenpiece3]) == [x, y]:
                    Greenpiece3 = None
                elif (game_track_green[Greenpiece4]) == [x, y]:
                    Greenpiece4 = None
            else:
                safe_space(piece, "b")

        elif board [z][t] == "g":
            if (z, t) not in {(1, 11), (1, 12), (5, 9), (5, 10), (5, 13), (5, 14), (9, 6), (9, 17), (10, 6), (10, 17), (11, 2), (11, 21), (12, 2), (12, 21), (13, 6), (13, 17), (14, 6), (14, 17), (18, 9), (18, 10), (18, 13), (18, 14), (22, 11), (22, 12)}:
                board [z][t] = "b"
                GreenBase +=1
                SubGBase()
                if (game_track_green2[Greenpiece1]) == [z, t]:
                    Greenpiece1 = None
                elif (game_track_green2[Greenpiece2]) == [z, t]:
                    Greenpiece2 = None
                elif (game_track_green2[Greenpiece3]) == [z, t]:
                    Greenpiece3 = None
                elif (game_track_green2[Greenpiece4]) == [z, t]:
                    Greenpiece4 = None
            else:
                safe_space(piece, "b")
        
        
        else:
            x, y = game_track_blue[piece]
            board[x][y] = "b"

#Change order of red pieces
def change_order_red():
    global Redpiece1
    global Redpiece2
    global Redpiece3
    global Redpiece4

    if Redpiece1 == None:
        if Redpiece4 != None:
            z = Redpiece4
            Redpiece4 = Redpiece1
            Redpiece1 = z
    if Redpiece1 == None:
        if Redpiece3 != None:
            z = Redpiece3
            Redpiece3 = Redpiece1
            Redpiece1 = z
    if Redpiece1 == None:
        if Redpiece2 != None:
            z = Redpiece2
            Redpiece2 = Redpiece1
            Redpiece1 = z
    if Redpiece2 == None:
        if Redpiece4 != None:
            z = Redpiece4
            Redpiece4 = Redpiece2
            Redpiece2 = z
    if Redpiece2 == None:
        if Redpiece3 != None:
            z = Redpiece3
            Redpiece3 = Redpiece2
            Redpiece2 = z
    if Redpiece3 == None:
        if Redpiece4 != None:
            z = Redpiece4
            Redpiece4 = Redpiece3
            Redpiece3 = z

    if (Redpiece4 and Redpiece1) != None:
        if (Redpiece4 > (Redpiece1)):
            z = Redpiece4
            Redpiece4 = Redpiece1
            Redpiece1 = z
    if (Redpiece4 and Redpiece2) != None:
        if Redpiece4 > (Redpiece2):
            z = Redpiece4
            Redpiece4 = Redpiece2
            Redpiece2 = z
    if (Redpiece4 and Redpiece3) != None:
        if Redpiece4 > (Redpiece3):
            z = Redpiece4
            Redpiece4 = Redpiece3
            Redpiece3 = z
    if (Redpiece3 and Redpiece1) != None:
        if Redpiece3 > (Redpiece1):
            z = Redpiece3
            Redpiece3 = Redpiece1
            Redpiece1 = z
    if (Redpiece3 and Redpiece2) != None:
        if Redpiece3 > (Redpiece2):
            z = Redpiece3
            Redpiece3 = Redpiece2
            Redpiece2 = z
    if (Redpiece2 and Redpiece1) != None:
        if Redpiece2 > (Redpiece1):
            z = Redpiece2
            Redpiece2 = Redpiece1
            Redpiece1 = z
#Change order of purple pieces
def change_order_purple():
    global Purplepiece1
    global Purplepiece2
    global Purplepiece3
    global Purplepiece4

    if Purplepiece1 == None:
        if Purplepiece4 != None:
            z = Purplepiece4
            Purplepiece4 = Purplepiece1
            Purplepiece1 = z
    if Purplepiece1 == None:
        if Purplepiece3 != None:
            z = Purplepiece3
            Purplepiece3 = Purplepiece1
            Purplepiece1 = z
    if Purplepiece1 == None:
        if Purplepiece2 != None:
            z = Purplepiece2
            Purplepiece2 = Purplepiece1
            Purplepiece1 = z
    if Purplepiece2 == None:
        if Purplepiece4 != None:
            z = Purplepiece4
            Purplepiece4 = Purplepiece2
            Purplepiece2 = z
    if Purplepiece2 == None:
        if Purplepiece3 != None:
            z = Purplepiece3
            Purplepiece3 = Purplepiece2
            Purplepiece2 = z
    if Purplepiece3 == None:
        if Purplepiece4 != None:
            z = Purplepiece4
            Purplepiece4 = Purplepiece3
            Purplepiece3 = z
    if (Purplepiece4 and Purplepiece1) != None:
        if (Purplepiece4 > (Purplepiece1)):
            z = Purplepiece4
            Purplepiece4 = Purplepiece1
            Purplepiece1 = z
    if (Purplepiece4 and Purplepiece2) != None:
        if Purplepiece4 > (Purplepiece2):
            z = Purplepiece4
            Purplepiece4 = Purplepiece2
            Purplepiece2 = z
    if (Purplepiece4 and Purplepiece3) != None:
        if Purplepiece4 > (Purplepiece3):
            z = Purplepiece4
            Purplepiece4 = Purplepiece3
            Purplepiece3 = z
    if (Purplepiece3 and Purplepiece1) != None:
        if Purplepiece3 > (Purplepiece1):
            z = Purplepiece3
            Purplepiece3 = Purplepiece1
            Purplepiece1 = z
    if (Purplepiece3 and Purplepiece2) != None:
        if Purplepiece3 > (Purplepiece2):
            z = Purplepiece3
            Purplepiece3 = Purplepiece2
            Purplepiece2 = z
    if (Purplepiece2 and Purplepiece1) != None:
        if Purplepiece2 > (Purplepiece1):
            z = Purplepiece2
            Purplepiece2 = Purplepiece1
            Purplepiece1 = z
#Change order of green pieces
def change_order_green():
    global Greenpiece1
    global Greenpiece2
    global Greenpiece3
    global Greenpiece4

    if Greenpiece1 == None:
        if Greenpiece4 != None:
            z = Greenpiece4
            Greenpiece4 = Greenpiece1
            Greenpiece1 = z
    if Greenpiece1 == None:
        if Greenpiece3 != None:
            z = Greenpiece3
            Greenpiece3 = Greenpiece1
            Greenpiece1 = z
    if Greenpiece1 == None:
        if Greenpiece2 != None:
            z = Greenpiece2
            Greenpiece2 = Greenpiece1
            Greenpiece1 = z
    if Greenpiece2 == None:
        if Greenpiece4 != None:
            z = Greenpiece4
            Greenpiece4 = Greenpiece2
            Greenpiece2 = z
    if Greenpiece2 == None:
        if Greenpiece3 != None:
            z = Greenpiece3
            Greenpiece3 = Greenpiece2
            Greenpiece2 = z
    if Greenpiece3 == None:
        if Greenpiece4 != None:
            z = Greenpiece4
            Greenpiece4 = Greenpiece3
            Greenpiece3 = z
    if (Greenpiece4 and Greenpiece1) != None:
        if (Greenpiece4 > (Greenpiece1)):
            z = Greenpiece4
            Greenpiece4 = Greenpiece1
            Greenpiece1 = z
    if (Greenpiece4 and Greenpiece2) != None:
        if Greenpiece4 > (Greenpiece2):
            z = Greenpiece4
            Greenpiece4 = Greenpiece2
            Greenpiece2 = z
    if (Greenpiece4 and Greenpiece3) != None:
        if Greenpiece4 > (Greenpiece3):
            z = Greenpiece4
            Greenpiece4 = Greenpiece3
            Greenpiece3 = z
    if (Greenpiece3 and Greenpiece1) != None:
        if Greenpiece3 > (Greenpiece1):
            z = Greenpiece3
            Greenpiece3 = Greenpiece1
            Greenpiece1 = z
    if (Greenpiece3 and Greenpiece2) != None:
        if Greenpiece3 > (Greenpiece2):
            z = Greenpiece3
            Greenpiece3 = Greenpiece2
            Greenpiece2 = z
    if (Greenpiece2 and Greenpiece1) != None:
        if Greenpiece2 > (Greenpiece1):
            z = Greenpiece2
            Greenpiece2 = Greenpiece1
            Greenpiece1 = z  
#Change order of blue pieces
def change_order_blue():
    global Bluepiece1
    global Bluepiece2
    global Bluepiece3
    global Bluepiece4

    if Bluepiece1 == None:
        if Bluepiece4 != None:
            z = Bluepiece4
            Bluepiece4 = Bluepiece1
            Bluepiece1 = z
    if Bluepiece1 == None:
        if Bluepiece3 != None:
            z = Bluepiece3
            Bluepiece3 = Bluepiece1
            Bluepiece1 = z
    if Bluepiece1 == None:
        if Bluepiece2 != None:
            z = Bluepiece2
            Bluepiece2 = Bluepiece1
            Bluepiece1 = z
    if Bluepiece2 == None:
        if Bluepiece4 != None:
            z = Bluepiece4
            Bluepiece4 = Bluepiece2
            Bluepiece2 = z
    if Bluepiece2 == None:
        if Bluepiece3 != None:
            z = Bluepiece3
            Bluepiece3 = Bluepiece2
            Bluepiece2 = z
    if Bluepiece3 == None:
        if Bluepiece4 != None:
            z = Bluepiece4
            Bluepiece4 = Bluepiece3
            Bluepiece3 = z
    if (Bluepiece4 and Bluepiece1) != None:
        if (Bluepiece4 > (Bluepiece1)):
            z = Bluepiece4
            Bluepiece4 = Bluepiece1
            Bluepiece1 = z
    if (Bluepiece4 and Bluepiece2) != None:
        if Bluepiece4 > (Bluepiece2):
            z = Bluepiece4
            Bluepiece4 = Bluepiece2
            Bluepiece2 = z
    if (Bluepiece4 and Bluepiece3) != None:
        if Bluepiece4 > (Bluepiece3):
            z = Bluepiece4
            Bluepiece4 = Bluepiece3
            Bluepiece3 = z
    if (Bluepiece3 and Bluepiece1) != None:
        if Bluepiece3 > (Bluepiece1):
            z = Bluepiece3
            Bluepiece3 = Bluepiece1
            Bluepiece1 = z
    if (Bluepiece3 and Bluepiece2) != None:
        if Bluepiece3 > (Bluepiece2):
            z = Bluepiece3
            Bluepiece3 = Bluepiece2
            Bluepiece2 = z
    if (Bluepiece2 and Bluepiece1) != None:
        if Bluepiece2 > (Bluepiece1):
            z = Bluepiece2
            Bluepiece2 = Bluepiece1
            Bluepiece1 = z  

def blockade_check(numb, Piece1, Piece2, Piece3, Piece4):
    global Blockade
    global Clear_Blockade
    
    counter = 0
    list_pieces = [Piece1, Piece2, Piece3, Piece4]

    for i in list_pieces:
        Blockade = True
        
        if i != None:
            if i <= 70:
                if Piece1 == Redpiece1:
                    bloqueo_r(numb, i)
                if Piece1 == Purplepiece1:
                    bloqueo_p(numb, i)
                if Piece1 == Bluepiece1:
                    bloqueo_b(numb, i)
                if Piece1 == Greenpiece1:
                    bloqueo_g(numb, i)



                if Blockade == False:
                    counter+=1
            if i >= 71:
                counter+=1
        if i == None:
            counter+=1
    
    if counter == 4:
        Clear_Blockade = True

#Game events in continuous loop
while not game_over:   
    draw()
    drawb()

    for event in pygame.event.get():
        print(event)
        #Exit out of game
        if event.type == pygame.QUIT:
            sys.exit()

        #if key is pressed
        if event.type == pygame.KEYDOWN:

            #if space bar is pressed
            if event.key == pygame.K_SPACE:
                if has_rolled == False:
                    if Red_Turn == True:
                        clock_reset1()
                        clock_reset2()
                        move1_complete = False
                        move2_complete = False
                        red_roll()
                        change_order_red()
                    elif Green_Turn == True:
                        clock_reset1()
                        clock_reset2()
                        move1_complete = False
                        move2_complete = False
                        green_roll()
                        change_order_green()
                    elif Purple_Turn == True:
                        clock_reset1()
                        clock_reset2()
                        move1_complete = False
                        move2_complete = False
                        purple_roll()
                        change_order_purple()
                    elif Blue_Turn == True:
                        clock_reset1()
                        clock_reset2()
                        move1_complete = False
                        move2_complete = False
                        blue_roll()
                        change_order_blue()      
            

            #if 1 key is pressed RED TURN
            if event.key == pygame.K_1:
                if Redpiece1 != None:
                    if Red_Turn == True:
                        if (has_rolled == True):
                            if (move1_complete == False):
                                Blockade = True
                                jump = advance1()
                                bloqueo_r(jump, Redpiece1)
                                if (Blockade == True):
                                    delete_piece(Redpiece1, "r")
                                    red_read1(Redpiece1)
                                    AdRHome()
                                    move_forward_red(Redpiece1)
                                    clock_reset1()
                                    move1_complete = True
                                if (Blockade == False): 
                                    jump = advance1() 
                                    blockade_check(jump, Redpiece1, Redpiece2, Redpiece3, Redpiece4)
                                    if Clear_Blockade == True:
                                        move1_complete = True
                                        Clear_Blockade = False

                            elif (move2_complete == False):
                                Blockade = True
                                jump = advance2()
                                bloqueo_r(jump, Redpiece1)                        
                                if (Blockade == True):
                                    delete_piece(Redpiece1, "r")
                                    red_read2(Redpiece1)
                                    AdRHome()
                                    move_forward_red(Redpiece1) 
                                    clock_reset2()
                                    move2_complete = True
                                if (Blockade == False):
                                    jump = advance2() 
                                    blockade_check(jump, Redpiece1, Redpiece2, Redpiece3, Redpiece4)
                                    if Clear_Blockade == True:
                                        move2_complete = True
                                        Clear_Blockade = False
                            if move1_complete and move2_complete == True:
                                has_rolled = False
                                Red_Turn = False
                                Green_Turn = True
            #if 2 key is pressed RED TURN
            if event.key == pygame.K_2:
                if Redpiece2 != None:
                    if Red_Turn == True:
                        if Redpiece2 != Redpiece1:    
                            if (has_rolled == True):
                                if (move1_complete == False):
                                    Blockade = True
                                    jump = advance1()
                                    bloqueo_r(jump, Redpiece2)
                                    if (Blockade == True):
                                        delete_piece(Redpiece2, "r")
                                        red_read1(Redpiece2)
                                        AdRHome()
                                        move_forward_red(Redpiece2)
                                        clock_reset1()
                                        move1_complete = True
                                    if (Blockade == False):
                                        jump = advance1() 
                                        blockade_check(jump, Redpiece1, Redpiece2, Redpiece3, Redpiece4)
                                        if Clear_Blockade == True:
                                            move1_complete = True
                                            Clear_Blockade = False

                                elif (move2_complete == False):
                                    Blockade = True
                                    jump = advance2()
                                    bloqueo_r(jump, Redpiece2)                        
                                    if (Blockade == True):
                                        delete_piece(Redpiece2, "r")
                                        red_read2(Redpiece2)
                                        AdRHome()
                                        move_forward_red(Redpiece2) 
                                        clock_reset2()
                                        move2_complete = True
                                    if (Blockade == False):
                                        jump = advance2() 
                                        blockade_check(jump, Redpiece1, Redpiece2, Redpiece3, Redpiece4) 
                                        if Clear_Blockade == True:
                                            move2_complete = True
                                            Clear_Blockade = False

                                if move1_complete and move2_complete == True:
                                    has_rolled = False
                                    Red_Turn = False
                                    Green_Turn = True
            #If key 3 is pressed RED TURN
            if event.key == pygame.K_3:
                if Redpiece3 != None:
                    if Red_Turn == True:
                        if Redpiece3 != Redpiece2:
                            if Redpiece3 != Redpiece1:
                                if (has_rolled == True):
                                    if (move1_complete == False):
                                        Blockade = True
                                        jump = advance1()
                                        bloqueo_r(jump, Redpiece3)
                                        if (Blockade == True):
                                            delete_piece(Redpiece3, "r")
                                            red_read1(Redpiece3)
                                            AdRHome()
                                            move_forward_red(Redpiece3)
                                            clock_reset1()
                                            move1_complete = True
                                        if (Blockade == False):
                                            
                                            jump = advance1() 
                                            blockade_check(jump, Redpiece1, Redpiece2, Redpiece3, Redpiece4)
                                            if Clear_Blockade == True:
                                                move1_complete = True
                                                Clear_Blockade = False

                                    elif (move2_complete == False):
                                        Blockade = True
                                        jump = advance2()
                                        bloqueo_r(jump, Redpiece3)                        
                                        if (Blockade == True):
                                            delete_piece(Redpiece3, "r")
                                            red_read2(Redpiece3)
                                            AdRHome()
                                            move_forward_red(Redpiece3) 
                                            clock_reset2()
                                            move2_complete = True
                                        if (Blockade == False):
                                            jump = advance2() 
                                            blockade_check(jump, Redpiece1, Redpiece2, Redpiece3, Redpiece4)
                                            if Clear_Blockade == True:
                                                move2_complete = True
                                                Clear_Blockade = False
                                    if move1_complete and move2_complete == True:
                                        has_rolled = False
                                        Red_Turn = False
                                        Green_Turn = True
            #If key 4 is pressed RED TURN
            if event.key == pygame.K_4:
                if Redpiece4 != None:
                    if Red_Turn == True:
                        if Redpiece4 != Redpiece3:
                            if Redpiece4 != Redpiece2:
                                if Redpiece4 != Redpiece1:
                                    if (has_rolled == True):
                                        if (move1_complete == False):
                                            Blockade = True
                                            jump = advance1()
                                            bloqueo_r(jump, Redpiece4)
                                            if (Blockade == True):
                                                delete_piece(Redpiece4, "r")
                                                red_read1(Redpiece4)
                                                AdRHome()
                                                move_forward_red(Redpiece4)
                                                clock_reset1()
                                                move1_complete = True
                                            if (Blockade == False):
                                                jump = advance1() 
                                                blockade_check(jump, Redpiece1, Redpiece2, Redpiece3, Redpiece4)
                                                if Clear_Blockade == True:
                                                    move1_complete = True
                                                    Clear_Blockade = False

                                        elif (move2_complete == False):
                                            Blockade = True
                                            jump = advance2()
                                            bloqueo_r(jump, Redpiece4)                        
                                            if (Blockade == True):
                                                delete_piece(Redpiece4, "r")
                                                red_read2(Redpiece4)
                                                AdRHome()
                                                move_forward_red(Redpiece4) 
                                                clock_reset2()
                                                move2_complete = True
                                            if (Blockade == False):
                                                jump = advance2() 
                                                blockade_check(jump, Redpiece1, Redpiece2, Redpiece3, Redpiece4) 
                                                if Clear_Blockade == True:
                                                    move2_complete = True
                                                    Clear_Blockade = False
                                        if move1_complete and move2_complete == True:
                                            has_rolled = False
                                            Red_Turn = False
                                            Green_Turn = True


            #if 1 key is pressed GREEN TURN
            if event.key == pygame.K_1:
                if Greenpiece1 != None:
                    if Green_Turn == True:
                        if (has_rolled == True):
                            if (move1_complete == False):
                                Blockade = True
                                jump = advance1()
                                bloqueo_g(jump, Greenpiece1)
                                if (Blockade == True):
                                    delete_piece(Greenpiece1, "g")
                                    green_read1(Greenpiece1)
                                    AdGHome()
                                    move_forward_green(Greenpiece1)
                                    clock_reset1()
                                    move1_complete = True
                                if (Blockade == False): 
                                    jump = advance1() 
                                    blockade_check(jump, Greenpiece1, Greenpiece2, Greenpiece3, Greenpiece4)
                                    if Clear_Blockade == True:
                                        move1_complete = True
                                        Clear_Blockade = False

                            elif (move2_complete == False):
                                Blockade = True
                                jump = advance2()
                                bloqueo_g(jump, Greenpiece1)                        
                                if (Blockade == True):
                                    delete_piece(Greenpiece1, "g")
                                    green_read2(Greenpiece1)
                                    AdGHome()
                                    move_forward_green(Greenpiece1) 
                                    clock_reset2()
                                    move2_complete = True
                                if (Blockade == False):
                                    jump = advance2() 
                                    blockade_check(jump, Greenpiece1, Greenpiece2, Greenpiece3, Greenpiece4)
                                    if Clear_Blockade == True:
                                        move2_complete = True
                                        Clear_Blockade = False
                            if move1_complete and move2_complete == True:
                                has_rolled = False
                                Green_Turn = False
                                Purple_Turn = True
            #if 2 key is pressed GREEN TURN
            if event.key == pygame.K_2:
                if Greenpiece2 != None:
                    if Green_Turn == True:
                        if Greenpiece2 != Greenpiece1:    
                            if (has_rolled == True):
                                if (move1_complete == False):
                                    Blockade = True
                                    jump = advance1()
                                    bloqueo_g(jump, Greenpiece2)
                                    if (Blockade == True):
                                        delete_piece(Greenpiece2, "g")
                                        green_read1(Greenpiece2)
                                        AdGHome()
                                        move_forward_green(Greenpiece2)
                                        clock_reset1()
                                        move1_complete = True
                                    if (Blockade == False): 
                                        jump = advance1() 
                                        blockade_check(jump, Greenpiece1, Greenpiece2, Greenpiece3, Greenpiece4)
                                        if Clear_Blockade == True:
                                            move1_complete = True
                                            Clear_Blockade = False

                                elif (move2_complete == False):
                                    Blockade = True
                                    jump = advance2()
                                    bloqueo_g(jump, Greenpiece2)                        
                                    if (Blockade == True):
                                        delete_piece(Greenpiece2, "g")
                                        green_read2(Greenpiece2)
                                        AdGHome()
                                        move_forward_green(Greenpiece2) 
                                        clock_reset2()
                                        move2_complete = True
                                    if (Blockade == False):
                                        jump = advance2() 
                                        blockade_check(jump, Greenpiece1, Greenpiece2, Greenpiece3, Greenpiece4)
                                        if Clear_Blockade == True:
                                            move2_complete = True
                                            Clear_Blockade = False
                                if move1_complete and move2_complete == True:
                                    has_rolled = False
                                    Green_Turn = False
                                    Purple_Turn = True
            #If key 3 is pressed GREEN TURN
            if event.key == pygame.K_3:
                if Greenpiece3 != None:
                    if Green_Turn == True:
                        if Greenpiece3 != Greenpiece2:
                            if Greenpiece3 != Greenpiece1:
                                if (has_rolled == True):
                                    if (move1_complete == False):
                                        Blockade = True
                                        jump = advance1()
                                        bloqueo_g(jump, Greenpiece3)
                                        if (Blockade == True):
                                            delete_piece(Greenpiece3, "g")
                                            green_read1(Greenpiece3)
                                            AdGHome()
                                            move_forward_green(Greenpiece3)
                                            clock_reset1()
                                            move1_complete = True
                                        if (Blockade == False): 
                                            jump = advance1() 
                                            blockade_check(jump, Greenpiece1, Greenpiece2, Greenpiece3, Greenpiece4)
                                            if Clear_Blockade == True:
                                                move1_complete = True
                                                Clear_Blockade = False

                                    elif (move2_complete == False):
                                        Blockade = True
                                        jump = advance2()
                                        bloqueo_g(jump, Greenpiece3)                        
                                        if (Blockade == True):
                                            delete_piece(Greenpiece3, "g")
                                            green_read2(Greenpiece3)
                                            AdGHome()
                                            move_forward_green(Greenpiece3) 
                                            clock_reset2()
                                            move2_complete = True
                                        if (Blockade == False):
                                            jump = advance2() 
                                            blockade_check(jump, Greenpiece1, Greenpiece2, Greenpiece3, Greenpiece4)
                                            if Clear_Blockade == True:
                                                move2_complete = True
                                                Clear_Blockade = False
                                    if move1_complete and move2_complete == True:
                                        has_rolled = False
                                        Green_Turn = False
                                        Purple_Turn = True
            #If key 4 is pressed GREEN TURN
            if event.key == pygame.K_4:
                if Greenpiece4 != None:
                    if Green_Turn == True:
                        if Greenpiece4 != Greenpiece3:
                            if Greenpiece4 != Greenpiece2:
                                if Greenpiece4 != Greenpiece1:
                                    if (has_rolled == True):
                                        if (move1_complete == False):
                                            Blockade = True
                                            jump = advance1()
                                            bloqueo_g(jump, Greenpiece4)
                                            if (Blockade == True):
                                                delete_piece(Greenpiece4, "g")
                                                green_read1(Greenpiece4)
                                                AdGHome()
                                                move_forward_green(Greenpiece4)
                                                clock_reset1()
                                                move1_complete = True
                                            if (Blockade == False): 
                                                jump = advance1() 
                                                blockade_check(jump, Greenpiece1, Greenpiece2, Greenpiece3, Greenpiece4)
                                                if Clear_Blockade == True:
                                                    move1_complete = True
                                                    Clear_Blockade = False

                                        elif (move2_complete == False):
                                            Blockade = True
                                            jump = advance2()
                                            bloqueo_g(jump, Greenpiece4)                        
                                            if (Blockade == True):
                                                delete_piece(Greenpiece4, "g")
                                                green_read2(Greenpiece4)
                                                AdGHome()
                                                move_forward_green(Greenpiece4) 
                                                clock_reset2()
                                                move2_complete = True
                                            if (Blockade == False):
                                                jump = advance2() 
                                                blockade_check(jump, Greenpiece1, Greenpiece2, Greenpiece3, Greenpiece4)
                                                if Clear_Blockade == True:
                                                    move2_complete = True
                                                    Clear_Blockade = False
                                        if move1_complete and move2_complete == True:
                                            has_rolled = False
                                            Green_Turn = False
                                            Purple_Turn = True
         
 
            #if 1 key is pressed PURPLE TURN
            if event.key == pygame.K_1:
                if Purplepiece1 != None:
                    if Purple_Turn == True:
                        if (has_rolled == True):
                            if (move1_complete == False):
                                Blockade = True
                                jump = advance1()
                                bloqueo_p(jump, Purplepiece1)
                                if (Blockade == True):
                                    delete_piece(Purplepiece1, "p")
                                    purple_read1(Purplepiece1)
                                    AdPHome()
                                    move_forward_purple(Purplepiece1)
                                    clock_reset1()
                                    move1_complete = True
                                if (Blockade == False): 
                                    jump = advance1() 
                                    blockade_check(jump, Purplepiece1, Purplepiece2, Purplepiece3, Purplepiece4)
                                    if Clear_Blockade == True:
                                        move1_complete = True
                                        Clear_Blockade = False

                            elif (move2_complete == False):
                                Blockade = True
                                jump = advance2()
                                bloqueo_p(jump, Purplepiece1)                        
                                if (Blockade == True):
                                    delete_piece(Purplepiece1, "p")
                                    purple_read2(Purplepiece1)
                                    AdPHome()
                                    move_forward_purple(Purplepiece1) 
                                    clock_reset2()
                                    move2_complete = True
                                if (Blockade == False):
                                    jump = advance2() 
                                    blockade_check(jump, Purplepiece1, Purplepiece2, Purplepiece3, Purplepiece4)
                                    if Clear_Blockade == True:
                                        move2_complete = True
                                        Clear_Blockade = False
                            if move1_complete and move2_complete == True:
                                has_rolled = False
                                Purple_Turn = False
                                Blue_Turn = True
            #if 2 key is pressed PURPLE TURN
            if event.key == pygame.K_2:
                if Purplepiece2 != None:
                    if Purple_Turn == True:
                        if Purplepiece2 != Purplepiece1:    
                            if (has_rolled == True):
                                if (move1_complete == False):
                                    Blockade = True
                                    jump = advance1()
                                    bloqueo_p(jump, Purplepiece2)
                                    if (Blockade == True):
                                        delete_piece(Purplepiece2, "p")
                                        purple_read1(Purplepiece2)
                                        AdPHome()
                                        move_forward_purple(Purplepiece2)
                                        clock_reset1()
                                        move1_complete = True
                                    if (Blockade == False): 
                                        jump = advance1() 
                                        blockade_check(jump, Purplepiece1, Purplepiece2, Purplepiece3, Purplepiece4)
                                        if Clear_Blockade == True:
                                            move1_complete = True
                                            Clear_Blockade = False

                                elif (move2_complete == False):
                                    Blockade = True
                                    jump = advance2()
                                    bloqueo_p(jump, Purplepiece2)                        
                                    if (Blockade == True):
                                        delete_piece(Purplepiece2, "p")
                                        purple_read2(Purplepiece2)
                                        AdPHome()
                                        move_forward_purple(Purplepiece2) 
                                        clock_reset2()
                                        move2_complete = True
                                    if (Blockade == False):
                                        jump = advance2() 
                                        blockade_check(jump, Purplepiece1, Purplepiece2, Purplepiece3, Purplepiece4)
                                        if Clear_Blockade == True:
                                            move2_complete = True
                                            Clear_Blockade = False
                                if move1_complete and move2_complete == True:
                                    has_rolled = False
                                    Purple_Turn = False
                                    Blue_Turn = True
            #If key 3 is pressed PURPLE TURN
            if event.key == pygame.K_3:
                if Purplepiece3 != None:
                    if Purple_Turn == True:
                        if Purplepiece3 != Purplepiece2:
                            if Purplepiece3 != Purplepiece1:
                                if (has_rolled == True):
                                    if (move1_complete == False):
                                        Blockade = True
                                        jump = advance1()
                                        bloqueo_p(jump, Purplepiece3)
                                        if (Blockade == True):
                                            delete_piece(Purplepiece3, "p")
                                            purple_read1(Purplepiece3)
                                            AdPHome()
                                            move_forward_purple(Purplepiece3)
                                            clock_reset1()
                                            move1_complete = True
                                        if (Blockade == False): 
                                            jump = advance1() 
                                            blockade_check(jump, Purplepiece1, Purplepiece2, Purplepiece3, Purplepiece4)
                                            if Clear_Blockade == True:
                                                move1_complete = True
                                                Clear_Blockade = False

                                    elif (move2_complete == False):
                                        Blockade = True
                                        jump = advance2()
                                        bloqueo_p(jump, Purplepiece3)                        
                                        if (Blockade == True):
                                            delete_piece(Purplepiece3, "p")
                                            purple_read2(Purplepiece3)
                                            AdPHome()
                                            move_forward_purple(Purplepiece3) 
                                            clock_reset2()
                                            move2_complete = True
                                        if (Blockade == False):
                                            jump = advance2() 
                                            blockade_check(jump, Purplepiece1, Purplepiece2, Purplepiece3, Purplepiece4)
                                            if Clear_Blockade == True:
                                                move2_complete = True
                                                Clear_Blockade = False
                                    if move1_complete and move2_complete == True:
                                        has_rolled = False
                                        Purple_Turn = False
                                        Blue_Turn = True
            #If key 4 is pressed PURPLE TURN
            if event.key == pygame.K_4:
                if Purplepiece4 != None:
                    if Purple_Turn == True:
                        if Purplepiece4 != Purplepiece3:
                            if Purplepiece4 != Purplepiece2:
                                if Purplepiece4 != Purplepiece1:
                                    if (has_rolled == True):
                                        if (move1_complete == False):
                                            Blockade = True
                                            jump = advance1()
                                            bloqueo_p(jump, Purplepiece4)
                                            if (Blockade == True):
                                                delete_piece(Purplepiece4, "p")
                                                purple_read1(Purplepiece4)
                                                AdPHome()
                                                move_forward_purple(Purplepiece4)
                                                clock_reset1()
                                                move1_complete = True
                                            if (Blockade == False): 
                                                jump = advance1() 
                                                blockade_check(jump, Purplepiece1, Purplepiece2, Purplepiece3, Purplepiece4)
                                                if Clear_Blockade == True:
                                                    move1_complete = True
                                                    Clear_Blockade = False

                                        elif (move2_complete == False):
                                            Blockade = True
                                            jump = advance2()
                                            bloqueo_p(jump, Purplepiece4)                        
                                            if (Blockade == True):
                                                delete_piece(Purplepiece4, "p")
                                                purple_read2(Purplepiece4)
                                                AdPHome()
                                                move_forward_purple(Purplepiece4) 
                                                clock_reset2()
                                                move2_complete = True
                                            if (Blockade == False):
                                                jump = advance2() 
                                                blockade_check(jump, Purplepiece1, Purplepiece2, Purplepiece3, Purplepiece4)
                                                if Clear_Blockade == True:
                                                    move2_complete = True
                                                    Clear_Blockade = False
                                        if move1_complete and move2_complete == True:
                                            has_rolled = False
                                            Purple_Turn = False
                                            Blue_Turn = True


            #if 1 key is pressed Blue TURN
            if event.key == pygame.K_1:
                if Bluepiece1 != None:
                    if Blue_Turn == True:
                        if (has_rolled == True):
                            if (move1_complete == False):
                                Blockade = True
                                jump = advance1()
                                bloqueo_b(jump, Bluepiece1)
                                if (Blockade == True):
                                    delete_piece(Bluepiece1, "b")
                                    blue_read1(Bluepiece1)
                                    AdBHome()
                                    move_forward_blue(Bluepiece1)
                                    clock_reset1()
                                    move1_complete = True
                                if (Blockade == False): 
                                    jump = advance1() 
                                    blockade_check(jump, Bluepiece1, Bluepiece2, Bluepiece3, Bluepiece4)
                                    if Clear_Blockade == True:
                                        move1_complete = True
                                        Clear_Blockade = False

                            elif (move2_complete == False):
                                Blockade = True
                                jump = advance2()
                                bloqueo_b(jump, Bluepiece1)                        
                                if (Blockade == True):
                                    delete_piece(Bluepiece1, "b")
                                    blue_read2(Bluepiece1)
                                    AdBHome()
                                    move_forward_blue(Bluepiece1) 
                                    clock_reset2()
                                    move2_complete = True
                                if (Blockade == False):
                                    jump = advance2() 
                                    blockade_check(jump, Bluepiece1, Bluepiece2, Bluepiece3, Bluepiece4)
                                    if Clear_Blockade == True:
                                        move2_complete = True
                                        Clear_Blockade = False
                            if move1_complete and move2_complete == True:
                                has_rolled = False
                                Blue_Turn = False
                                Red_Turn = True         
            #if 2 key is pressed BLUE TURN
            if event.key == pygame.K_2:
                if Bluepiece2 != None:
                    if Blue_Turn == True:
                        if Bluepiece2 != Bluepiece1:    
                            if (has_rolled == True):
                                if (move1_complete == False):
                                    Blockade = True
                                    jump = advance1()
                                    bloqueo_b(jump, Bluepiece2)
                                    if (Blockade == True):
                                        delete_piece(Bluepiece2, "b")
                                        blue_read1(Bluepiece2)
                                        AdBHome()
                                        move_forward_blue(Bluepiece2)
                                        clock_reset1()
                                        move1_complete = True
                                    if (Blockade == False): 
                                        jump = advance1() 
                                        blockade_check(jump, Bluepiece1, Bluepiece2, Bluepiece3, Bluepiece4)
                                        if Clear_Blockade == True:
                                            move1_complete = True
                                            Clear_Blockade = False

                                elif (move2_complete == False):
                                    Blockade = True
                                    jump = advance2()
                                    bloqueo_b(jump, Bluepiece2)                        
                                    if (Blockade == True):
                                        delete_piece(Bluepiece2, "b")
                                        blue_read2(Bluepiece2)
                                        AdBHome()
                                        move_forward_blue(Bluepiece2) 
                                        clock_reset2()
                                        move2_complete = True
                                    if (Blockade == False):
                                        jump = advance2() 
                                        blockade_check(jump, Bluepiece1, Bluepiece2, Bluepiece3, Bluepiece4)
                                        if Clear_Blockade == True:
                                            move2_complete = True
                                            Clear_Blockade = False
                                if move1_complete and move2_complete == True:
                                    has_rolled = False
                                    Blue_Turn = False
                                    Red_Turn = True                    
            #If key 3 is pressed BLUE TURN
            if event.key == pygame.K_3:
                if Bluepiece3 != None:
                    if Blue_Turn == True:
                        if Bluepiece3 != Bluepiece2:
                            if Bluepiece3 != Bluepiece1:
                                if (has_rolled == True):
                                    if (move1_complete == False):
                                        Blockade = True
                                        jump = advance1()
                                        bloqueo_b(jump, Bluepiece3)
                                        if (Blockade == True):
                                            delete_piece(Bluepiece3, "b")
                                            blue_read1(Bluepiece3)
                                            AdBHome()
                                            move_forward_blue(Bluepiece3)
                                            clock_reset1()
                                            move1_complete = True
                                        if (Blockade == False): 
                                            jump = advance1() 
                                            blockade_check(jump, Bluepiece1, Bluepiece2, Bluepiece3, Bluepiece4)
                                            if Clear_Blockade == True:
                                                move1_complete = True
                                                Clear_Blockade = False

                                    elif (move2_complete == False):
                                        Blockade = True
                                        jump = advance2()
                                        bloqueo_b(jump, Bluepiece3)                        
                                        if (Blockade == True):
                                            delete_piece(Bluepiece3, "b")
                                            blue_read2(Bluepiece3)
                                            AdBHome()
                                            move_forward_blue(Bluepiece3) 
                                            clock_reset2()
                                            move2_complete = True
                                        if (Blockade == False):
                                            jump = advance2() 
                                            blockade_check(jump, Bluepiece1, Bluepiece2, Bluepiece3, Bluepiece4)
                                            if Clear_Blockade == True:
                                                move2_complete = True
                                                Clear_Blockade = False
                                    if move1_complete and move2_complete == True:
                                        has_rolled = False
                                        Blue_Turn = False
                                        Red_Turn = True
            #If key 4 is pressed BLUE TURN
            if event.key == pygame.K_4:             
                if Bluepiece4 != None:
                    if Blue_Turn == True:
                        if Bluepiece4 != Bluepiece3:
                            if Bluepiece4 != Bluepiece2:
                                if Purplepiece4 != Bluepiece1:
                                    if (has_rolled == True):
                                        if (move1_complete == False):
                                            Blockade = True
                                            jump = advance1()
                                            bloqueo_b(jump, Bluepiece4)
                                            if (Blockade == True):
                                                delete_piece(Bluepiece4, "b")
                                                blue_read1(Bluepiece4)
                                                AdBHome()
                                                move_forward_blue(Bluepiece4)
                                                clock_reset1()
                                                move1_complete = True
                                            if (Blockade == False): 
                                                jump = advance1() 
                                                blockade_check(jump, Bluepiece1, Bluepiece2, Bluepiece3, Bluepiece4)
                                                if Clear_Blockade == True:
                                                    move1_complete = True
                                                    Clear_Blockade = False

                                        elif (move2_complete == False):
                                            Blockade = True
                                            jump = advance2()
                                            bloqueo_b(jump, Bluepiece4)                        
                                            if (Blockade == True):
                                                delete_piece(Bluepiece4, "b")
                                                blue_read2(Bluepiece4)
                                                AdBHome()
                                                move_forward_blue(Bluepiece4) 
                                                clock_reset2()
                                                move2_complete = True
                                            if (Blockade == False):
                                                jump = advance2() 
                                                blockade_check(jump, Bluepiece1, Bluepiece2, Bluepiece3, Bluepiece4)
                                                if Clear_Blockade == True:
                                                    move2_complete = True
                                                    Clear_Blockade = False
                                        if move1_complete and move2_complete == True:
                                            has_rolled = False
                                            Blue_Turn = False
                                            Red_Turn = True
                             
    pygame.display.update() 


########           TO DO LIST         ####################

#move forward 20 after kills (Big gold 20 and continue turn like normal)
#move forward 1o after making it home (Big gold 10 and continue turn like normal)
#kill when coming out of home and 2 pieces are already there
#double rolls (bloqueo and roll again)

#make individual spaces more clear

#############################################################################################################
