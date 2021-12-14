import pygame  as pg
import pygame_gui as gui
from engine import *

def main():
    """This is the Game's main function"""
    pg.init()
    pg.display.set_caption('Game')
    window_surface = pg.display.set_mode((800, 600))
    clock = pg.time.Clock()

    is_running = True

    game = Game()
    
    while is_running:
        #going over 30 fps is not needed
        time_delta = clock.tick(30)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                is_running = False
        
        ongoing = game.update(window_surface)
        print("game over") if not ongoing else None   #game over...

        pg.display.update()
        

if __name__ == '__main__':
    main()
