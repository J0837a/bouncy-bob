import pygame as game
import os

import pygame.constants

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

def draw_window(red,  yellow):
    Window.fill((0, 255, 0))
    Window.blit(yellowShip, (yellow.x, yellow.y))
    Window.blit(redShip, (red.x, yellow.y))
    game.display.update()

def master():
    red = game.Rect(100 , 300, 50, 40)
    yellow = game.Rect(100 , 300, 50, 40)

    clock = game.time.Clock()
    play = True
    while play:
        clock.tick(FPS)
        for event in game.event.get():
            if event.type == game.QUIT:
                play = False

        keys_pressed = game.key.get_pressed()
        if keys_pressed[pygame.K_a]:
            red.x -= 1

        yellow.x += 3
        draw_window(red, yellow)

    game.quit()

if __name__ == "__main__":
    master()