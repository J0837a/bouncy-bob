import pygame as game
import os

Width, Height = 900, 500
Window = game.display.set_mode((Width, Height))
game.display.set_caption("Bouncy Bob") #Add a cool lil title thing later
FPS = 60

def loadFromAssets(file):
    return game.image.load(os.path.join("Assets", file))

yellowShip = loadFromAssets("spaceship_yellow.png")
yellowShip = game.transform.scale(yellowShip, (50, 40))
yellowShip = game.transform.rotate(yellowShip, 90)
redShip = loadFromAssets("spaceship_red.png")
redShip = game.transform.scale(redShip, (50, 40))
redShip = game.transform.rotate(redShip, -90)

def draw_window():
    Window.fill((0, 255, 0))
    Window.blit(yellowShip, (200, 200))
    Window.blit(redShip, (600, 200))
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