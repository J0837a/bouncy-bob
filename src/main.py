from basics import *
import pygame as game

game.font.init()
game.mixer.init()

Width, Height = 900, 500
Window = game.display.set_mode((Width, Height))
game.display.set_caption("Bouncy Bob") #Add a cool lile title thing later
FPS = 60

def draw_window():
    game.display.update()


def master():
    clock = game.time.Clock()
    play = True
    while play:
        clock.tick(FPS)
        for event in game.event.get():
            if event.type == game.QUIT:
                play = False

        draw_window()

    game.quit()

if __name__ == "__main__":
    master()