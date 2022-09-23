from basics import *
import pygame as game
import random as rand

game.font.init()
game.mixer.init()

Width, Height = 900, 500
Window = game.display.set_mode((Width, Height))
game.display.set_caption("Bouncy Bob") #Add a cool lile title thing later
FPS = 60
gameFont = game.font.SysFont('comicsans', 20)
bg = game.transform.scale(loadFromAssets("bg.jpg"), (Width, Height))

objects = [player()]

def spawnPipes():
    center = rand.randint(30, 470)
    objects.append(wall(center - 50, True))
    objects.append(wall(center + 50, False))
    objects.append(scoreMarker())

def tick():
    Window.blit(bg, (0, 0))
    for obj in objects:
        if obj.nick == "Player":
            obj.tick(Window, objects)
        else:
            obj.tick(Window)

        if obj.rect.x < -30:
            objects.remove(obj)

    scoreDisplay = gameFont.render("Score: " + str(objects[0].score), 1, (128, 0, 128))
    Window.blit(scoreDisplay, (10, 10))

    game.display.update()

def master():
    clock = game.time.Clock()
    play = True
    spawnPipes()
    while play:
        clock.tick(FPS)
        for event in game.event.get():
            if event.type == game.QUIT:
                play = False
            if event.type == hitWall:
                play = False
            if event.type == passCheckpoint and len(objects) < 5:
                objects[0].score += 1
                spawnPipes()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            if objects[0].cooldownTicks < 0:
                objects[0].jumping = True
                objects[0].jumpTicks = 10
                objects[0].cooldownTicks = 10

        tick()

    game.quit()

if __name__ == "__main__":
    master()