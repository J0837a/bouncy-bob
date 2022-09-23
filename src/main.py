from basics import *
import pygame as game
import random as rand

game.font.init()
game.mixer.init()

Width, Height = 900, 500
Window = game.display.set_mode((Width, Height))
game.display.set_caption("Bouncy Bob") #Add a cool lile title thing later
FPS = 60

objects = [player()]

def spawnPipes():
    center = rand.randint(30, 470)
    objects.append(wall(center - 40, True))
    objects.append(wall(center + 40, False))
    objects.append(scoreMarker())
def tick():
    Window.fill((255, 255, 255))
    for obj in objects:
        obj.tick(Window)

    game.display.update()

def checkPlayerHits():
    pass

def master():
    clock = game.time.Clock()
    play = True
    spawnPipes()
    while play:
        clock.tick(FPS)
        for event in game.event.get():
            if event.type == game.QUIT:
                play = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            if objects[0].cooldownTicks < 0:
                objects[0].jumping = True
                objects[0].jumpTicks = 10
                objects[0].cooldownTicks = 10

        checkPlayerHits()
        tick()

    game.quit()

if __name__ == "__main__":
    master()