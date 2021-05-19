import sys, pygame
from pygame.locals import*

width=400
height=400
Color_screen= "#06273a"
Color_line= "#797e66"

def main():
    screen=pygame.display.set_mode((width,height))
    screen.fill(Color_screen)
    for times in range(1, 20):
        changer = 20 * times
        pygame.draw.line(screen, Color_line, (changer,0), (changer,400))
        pygame.draw.line(screen, Color_line, (0,changer), (400, changer))
    
    pygame.display.flip()
    while True:
        for events in pygame.event.get():
            if events.type == QUIT:

                sys.exit(0)
main()