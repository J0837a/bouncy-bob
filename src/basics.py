import pygame
import os

passCheckpoint = pygame.USEREVENT + 1
hitWall = pygame.USEREVENT + 2

def loadFromAssets(file):
    return pygame.image.load(os.path.join("Assets", file))

def buildAnimationTable(base, frames, delay):
    tbl = []
    for i in range(frames):
        for x in range(delay):
            tbl.append(loadFromAssets(base + "/" + base + "-" + str(i) + ".png"))
    return tbl

class wall:
    def __init__(self, y, top):
        self.nick = "Wall"
        self.x = 800
        self.y = y
        self.top = top
        self.animationFrame = 0
        self.animationTable = buildAnimationTable("tile", 6, 7)

        if top:
            self.rect = pygame.Rect(800, 0, 30, 0 + y)
            self.resize = abs((0 + y))
        else:
            self.rect = pygame.Rect(800, y, 30, 500 - y)
            self.resize = abs((500 - y))

    def tick(self, window):
        #pygame.draw.rect(window, (0, 0, 255), self)
        currentFrame = self.animationTable[self.animationFrame]
        currentFrame = pygame.transform.scale(currentFrame, (50, self.resize))
        if self.top:
            currentFrame = pygame.transform.rotate(currentFrame, 180)
            window.blit(currentFrame, (self.x, 30))
        else:
            window.blit(currentFrame, (self.x, self.y - 30))

        self.animationFrame += 1

        if self.animationFrame >= len(self.animationTable):
            self.animationFrame = 0

        self.rect.x -= 2
        self.x -= 2

class scoreMarker:
    def __init__(self):
        self.nick = "Score"
        self.x = 800
        self.rect = pygame.Rect(800 + 15, 0, 15, 500)

    def tick(self, window):
        self.rect.x -= 2

class player:
    def __init__(self):
        self.nick = "Player"
        self.x = 300
        self.y = 250
        self.rect = pygame.Rect(self.x + 15, self.y, 25, 25)
        self.jumping = False

        #Jumping Shit
        self.jumpTicks = 0
        self.cooldownTicks = -1
        self.score = 0

        #Animation Shit
        self.animationFrame = 0
        self.animationTable = buildAnimationTable("IDFhrw", 21, 5)

    def tick(self, window, objects):
        currentFrame = self.animationTable[self.animationFrame]
        currentFrame = pygame.transform.scale(currentFrame, (50, 50))
        window.blit(currentFrame, (self.x, self.y))
        self.animationFrame += 1

        if self.animationFrame >= len(self.animationTable):
            self.animationFrame = 0

        if self.jumping and self.jumpTicks < 0:
            self.jumping = False

        if not self.jumping:
            self.y += 3
        else:
            self.y -= 3
            self.jumpTicks -= 1

        self.cooldownTicks -= 1
        self.rect.y = self.y + 15

        for obj in objects:
            if self.rect.colliderect(obj.rect):
                if obj.nick == "Wall":
                    pygame.event.post(pygame.event.Event(hitWall))
                elif obj.nick == "Score":
                    pygame.event.post(pygame.event.Event(passCheckpoint))
