import sys, pygame
from pygame.locals import*

width=400
height=400
Color_screen= "#06273a"
Color_line= "#797e66"
Color_snake = "#461815"
Cell_size = 20
X_Cell = 10
Y_Cell = 10
X_Tail_Cell = -1
Y_Tail_Cell = -1

screen=pygame.display.set_mode((width,height))

def draw_sanke():
    global X_Tail_Cell, Y_Tail_Cell
    if X_Cell>19 or X_Cell<0 or Y_Cell>19 or Y_Cell<0:
        return False
    pygame.draw.rect(screen, Color_snake, pygame.Rect((Cell_size*X_Cell)+1, (Cell_size*Y_Cell)+1, Cell_size-1, Cell_size-1))
    if X_Tail_Cell != -1:
        pygame.draw.rect(screen, Color_screen, pygame.Rect((Cell_size*X_Tail_Cell)+1, (Cell_size*Y_Tail_Cell)+1, Cell_size-1, Cell_size-1))
    X_Tail_Cell = X_Cell
    Y_Tail_Cell = Y_Cell
    pygame.display.flip()
    return True

def main():
    global Y_Cell, X_Cell
    screen.fill(Color_screen)
    for times in range(1, 20):
        changer = Cell_size * times
        pygame.draw.line(screen, Color_line, (changer,0), (changer,400))
        pygame.draw.line(screen, Color_line, (0,changer), (400, changer))
    draw_sanke()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit(0)
            elif event.type == KEYDOWN:
                key_pressed = pygame.key.name(event.key)
                if key_pressed == "down":
                    Y_Cell += 1
                    if not draw_sanke():
                        Y_Cell -= 1
                elif key_pressed == "up":
                    Y_Cell -= 1
                    if not draw_sanke():
                        Y_Cell += 1
                elif key_pressed == "right":
                    X_Cell += 1
                    if not draw_sanke():
                        X_Cell -= 1
                elif key_pressed == "left":
                    X_Cell -= 1
                    if not draw_sanke():
                        X_Cell += 1
main()