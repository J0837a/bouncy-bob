from classes import *
from basics import *
import pygame as game

Width, Height = 900, 500
Window = game.display.set_mode((Width, Height))
game.display.set_caption("Bouncy Bob") #Add a cool lile title thing later
FPS = 60
Backround = game.transform.scale(loadFromAssets("space.png"), (Width, Height))
bulletHit = game.USEREVENT + 1
# game.event.post(game.event.Event(bulletHit)) to do this event ig
Player = player(loadFromAssets("spaceship_red.png"), 20, 20, 450, 450)
Player.rotate(180)

objects = [Player]

def createInvaders(amount):
    spacing = (900 / amount)

    for x in range(amount):
        Invader = invader(loadFromAssets("spaceship_yellow.png"), 20, 20, (x * spacing), 100)
        objects.append(Invader)

def draw_window():
    Window.blit(Backround, (0, 0))
    for i in objects:
        i.draw(Window)
        if i.collisions:
            i.collisionCheck(objects)
        if i.randomEvents:
            i.randomEvent(objects)
    game.display.update()

def outOfBoundsCheck(objects):
    for i in objects:
        if (i.x < 0 or i.y < 0) or (i.x > Width or i.y > Height):
            objects.remove(i)


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
        if Player.shotCooldown > 0:
            return
        objects.append(laser(Player, True))
        Player.shotCooldown = 20

def master():
    clock = game.time.Clock()
    play = True
    createInvaders(10)
    while play:
        clock.tick(FPS)
        Player.shotCooldown -= 1
        for event in game.event.get():
            if event.type == game.QUIT:
                play = False

        handleMovement()
        outOfBoundsCheck(objects)
        draw_window()

    game.quit()

if __name__ == "__main__":
    master()