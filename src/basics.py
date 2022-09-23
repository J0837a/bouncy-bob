import pygame
import os

passCheckpoint = pygame.USEREVENT + 1
hitWall = pygame.USEREVENT + 2

def loadFromAssets(file):
    return pygame.image.load(os.path.join("Assets", file))

class wall:
    def __init__(self, y, top):
        self.x = 800
        self.y = y

        if top:
            self.rect = pygame.Rect(800, 0, 30, 0 + y)
        else:
            self.rect = pygame.Rect(800, y, 30, 500 - y)

    def tick(self, window):
        pygame.draw.rect(window, (0, 0, 255), self)
        self.rect.x -= 2

class scoreMarker:
    def __init__(self):
        self.x = 800
        self.rect = pygame.Rect(800 + 15, 0, 15, 500)

    def tick(self, window):
        pygame.draw.rect(window, (255, 0, 0), self)
        self.rect.x -= 2

class player:
    def __init__(self):
        self.x = 300
        self.y = 250
        self.rect = pygame.Rect(self.x, self.y, 30, 30)
        self.jumping = False
        self.jumpTicks = 0
        self.cooldownTicks = -1

    def tick(self, window):
        pygame.draw.rect(window, (0, 255, 0), self)

        if self.jumping and self.jumpTicks < 0:
            self.jumping = False

        if not self.jumping:
            self.rect.y += 3
        else:
            self.rect.y -= 3
            self.jumpTicks -= 1

        self.cooldownTicks -= 1

