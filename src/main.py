from classes import *
from basics import *
import pygame as game
game.font.init()
game.mixer.init()

Width, Height = 900, 500
Window = game.display.set_mode((Width, Height))
game.display.set_caption("Bouncy Bob") #Add a cool lile title thing later
FPS = 60
Backround = game.transform.scale(loadFromAssets("space.png"), (Width, Height))
Player = player(loadFromAssets("spaceship_red.png"), 20, 20, 450, 450)
Player.rotate(180)
gameFont = game.font.SysFont('comicsans', 20)

objects = [Player]

levels = [{"Invaders": 5}, {"Invaders": 10}, {"Invaders": 20}, {"Invaders": 40}]

def createInvaders(amount, boost):
    spacing = (900 / amount)

    for x in range(amount):
        Invader = invader(loadFromAssets("spaceship_yellow.png"), 20, 20, (x * spacing), 100, boost)
        objects.append(Invader)

def draw_window(score, level):
    Window.blit(Backround, (0, 0))
    for i in objects:
        i.draw(Window)
        if i.collisions:
            i.collisionCheck(objects)
        if i.randomEvents:
            i.randomEvent(objects)

        scoreDisplay = gameFont.render("Score: " + str(score), 1, (128, 0, 128))
        levelDisplay = gameFont.render("Level: " + str(level + 1), 1, (128, 0, 128))
        Window.blit(scoreDisplay, (10, 10))
        Window.blit(levelDisplay, (10, 30))

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
    level = 0
    invaders = levels[level]["Invaders"]
    createInvaders(invaders, (.25 * level))
    score = 0
    while play:
        clock.tick(FPS)
        Player.shotCooldown -= 1
        for event in game.event.get():
            if event.type == game.QUIT:
                play = False
            if event.type == bulletHitInvader:
                invaders -= 1
                score += 1
        if invaders < 1:
            level += 1
            invaders = levels[level]["Invaders"]
            createInvaders(invaders, (.25 * level))


        handleMovement()
        outOfBoundsCheck(objects)
        draw_window(score, level )

    game.quit()

if __name__ == "__main__":
    master()