from basics import bulletHitInvader
import pygame
import random
class laser:
    def __init__(self, shooter, player):
        self.rect = pygame.Rect(shooter.x + (shooter.waist // 2), shooter.y - (shooter.height // 2), 2, 10)
        self.collisions = True
        self.randomEvents = False
        self.x = 0
        self.y = 0
        self.isPlayer = player
        self.className = "Laser"

    def draw(self, window):
        if self.isPlayer:
            pygame.draw.rect(window, (0, 0, 255), self)
            self.rect.y -= 5
        else:
            pygame.draw.rect(window, (255, 0, 0), self)
            self.rect.y += 5
        self.y = self.rect.y
        self.x = self.rect.x

    def collisionCheck(self, targets):
        for x in range(len(targets)):
            objectClass = targets[x]
            if self.rect.colliderect(objectClass.rect) and self.rect != objectClass.rect:
                if self.isPlayer:
                    pygame.event.post(pygame.event.Event(bulletHitInvader))
                    targets.remove(objectClass)
                    targets.remove(self)
                    break
                elif objectClass.className == "Player":
                    targets.remove(objectClass)
                    targets.remove(self)
                    pygame.quit()
                    break

class imageObjectRect:
    def __init__(self, image, height, waist, x, y):
        self.image = image
        self.height = height
        self.waist = waist
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, self.height, self.waist)
        self.collisions = False
        self.randomEvents = False
        self.className = "Basic Class"

        self.image = pygame.transform.scale(self.image, (self.height, self.waist))

    def draw(self, window):
        window.blit(self.image, (self.x, self.y))

    def rotate(self, amount):
        self.image = pygame.transform.rotate(self.image, amount)


class player(imageObjectRect):
    def __init__(self, image, height, waist, x, y):
        imageObjectRect.__init__(self, image, height, waist, x, y)
        self.shotCooldown = 0
        self.className = "Player"

class invader(imageObjectRect):
    def __init__(self, image, height, waist, x, y, boost):
        imageObjectRect.__init__(self, image, height, waist, x, y)
        self.randomEvents = True
        self.className = "Invader"
        self.boost = boost

    def boxSync(self):
        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self, window):
        window.blit(self.image, (self.x, self.y))

        if self.x > 890:
            self.y += 30
            self.x = 20

        self.x += 1 + self.boost

        self.boxSync()

    def randomEvent(self, objects):
        if random.random() < 0.005:
            objects.append(laser(self, False))

