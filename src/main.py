from classes import *
from basics import *
import pygame as game

Width, Height = 900, 500
Window = game.display.set_mode((Width, Height))
game.display.set_caption("Bouncy Bob") #Add a cool lile title thing later
FPS = 60


Player = player(loadFromAssets("spaceship_red.png"), 50, 50, 450, 450)
Player.rotate(180)

objects = [Player]

def createInvaders(amount):
    spacing = 900 / amount

    for x in range(amount):
        Invader = imageObjectRect(loadFromAssets("spaceship_yellow.png"), 50, 50, (x * spacing) + 100, 100)
        objects.append(Invader)

def draw_window():
    Window.fill((0, 255, 0))
    for i in objects:
        i.draw(Window)
    game.display.update()


def handleMovement():
    global laser
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_a]:
        if Player.x < 40:
            return
        Player.x -= 4
    if pressed[pygame.K_d]:
        if Player.x > 860:
            return
        Player.x += 4
    if pressed[pygame.K_w]:
        if Player.shots > 3:
            return
        objects.append(laser(Player))
        Player.shots += 1

def master():
    clock = game.time.Clock()
    play = True
    createInvaders(5)
    while play:
        clock.tick(FPS)
        for event in game.event.get():
            if event.type == game.QUIT:
                play = False

        handleMovement()
        draw_window()

    game.quit()

if __name__ == "__main__":
    master()