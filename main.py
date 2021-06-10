import sys, pygame
import time
from pygame.locals import*
import random

width=400
height=400
Color_screen= "#06273a"
Color_line= "#797e66"
Color_snake = "#461815"
Color_frog = "#4f772d"
Cell_size = 20
X_Cell = 10
Y_Cell = 10
X_Tail_Cell = -1
Y_Tail_Cell = -1

GAME_ON = True
SNAKE_FACE_DIRECTION = None
GAME_BOARD = [0]*400
FROG_POS = -1
snake_pos_list = []
op_directions ={
    'left': 'right',
    "right": "left",
    'down': 'up',
    'up': 'down',
}

screen=pygame.display.set_mode((width,height))

def get_cell_pos(index):
    y, x = index//20, index%20
    return (x, y)

def get_index_from_xy(x, y):
    index = y*20 + x
    return index

def generate_frog_pos():
    while True:
        pos_index = random.randint(0, 399)
        if pos_index not in snake_pos_list:
            return pos_index

def draw_frog(index):
    global FROG_POS
    x, y = get_cell_pos(index)
    pygame.draw.rect(screen, Color_frog, pygame.Rect((Cell_size*x)+1, (Cell_size*y)+1, Cell_size-1, Cell_size-1))
    FROG_POS = index

def draw_sanke():
    global X_Tail_Cell, Y_Tail_Cell, snake_pos_list
    for pos in snake_pos_list:
        x, y = get_cell_pos(pos)
        pygame.draw.rect(screen, Color_snake, pygame.Rect((Cell_size*x)+1, (Cell_size*y)+1, Cell_size-1, Cell_size-1))
    if X_Tail_Cell != -1:
        pygame.draw.rect(screen, Color_screen, pygame.Rect((Cell_size*X_Tail_Cell)+1, (Cell_size*Y_Tail_Cell)+1, Cell_size-1, Cell_size-1))
    pygame.display.flip()
    return True

def check_game_over():
    global X_Cell , Y_Cell, snake_pos_list, GAME_ON
    index =get_index_from_xy(X_Cell, Y_Cell)
    if index in snake_pos_list:
        print("Game Over")
        GAME_ON= False
    elif (X_Cell>19 or X_Cell<0 or Y_Cell>19 or Y_Cell<0):
        print("Game Over")
        GAME_ON= False
    else:
        snake_pos_list.append(index)

def snake_speed(direction):
    global X_Cell, Y_Cell, X_Tail_Cell, Y_Tail_Cell
    if len(snake_pos_list)>0:
        X_Tail_Cell, Y_Tail_Cell = get_cell_pos(snake_pos_list.pop(0))
    if direction == "down":
        Y_Cell += 1
        check_game_over()
        if not draw_sanke():
            Y_Cell -= 1
    elif direction == "up":
        Y_Cell -= 1
        check_game_over()
        if not draw_sanke():
            Y_Cell += 1
    elif direction == "right":
        X_Cell += 1
        check_game_over()
        if not draw_sanke():
            X_Cell -= 1
    elif direction == "left":
        X_Cell -= 1
        # snake_pos_list.append(get_index_from_xy(X_Cell, Y_Cell))
        check_game_over()
        if not draw_sanke():
            X_Cell += 1
    snake_face = get_index_from_xy(X_Cell, Y_Cell)
    if snake_face == FROG_POS:
        draw_frog(generate_frog_pos())
        snake_pos_list.insert(0 ,get_index_from_xy(X_Tail_Cell, Y_Tail_Cell))
        draw_sanke()


def main():
    global Y_Cell, X_Cell, SNAKE_FACE_DIRECTION, op_directions, GAME_ON
    screen.fill(Color_screen)
    for times in range(1, 20):
        changer = Cell_size * times
        pygame.draw.line(screen, Color_line, (changer,0), (changer,400))
        pygame.draw.line(screen, Color_line, (0,changer), (400, changer))
    draw_sanke()
    draw_frog(generate_frog_pos())
    prev_direction = None
    while True:
        if GAME_ON :
            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit(0)
                elif event.type == KEYDOWN:
                    key_pressed = pygame.key.name(event.key)
                    if key_pressed == "down":
                        SNAKE_FACE_DIRECTION = "down"
                    elif key_pressed == "up":
                        SNAKE_FACE_DIRECTION = "up"
                    elif key_pressed == "right":
                        SNAKE_FACE_DIRECTION = "right"
                    elif key_pressed == "left":
                        SNAKE_FACE_DIRECTION = "left"
            if prev_direction==None:
                prev_direction=SNAKE_FACE_DIRECTION
            elif op_directions[prev_direction] != SNAKE_FACE_DIRECTION:
                prev_direction= SNAKE_FACE_DIRECTION
            else:
                SNAKE_FACE_DIRECTION= prev_direction
            snake_speed(SNAKE_FACE_DIRECTION)
            print(snake_pos_list)
            time.sleep(0.40)      
main()