import pygame


class laser:
    def __init__(self, shooter):
        self.rect = pygame.Rect(shooter.x + (shooter.waist // 2), shooter.y - (shooter.height // 2), 10, 10)

    def draw(self, window):
        pygame.draw.rect(window, (255, 0, 0), self)
        self.rect.y -= 3


class imageObjectRect:
    def __init__(self, image, height, waist, x, y):
        self.image = image
        self.height = height
        self.waist = waist
        self.x = x
        self.y = y
        self.rect = pygame.Rect(300, 300, self.height, self.waist)

        self.image = pygame.transform.scale(self.image, (self.height, self.waist))

    def draw(self, window):
        window.blit(self.image, (self.x, self.y))

    def rotate(self, amount):
        self.image = pygame.transform.rotate(self.image, amount)


class player(imageObjectRect):
    def __init__(self, image, height, waist, x, y):
        imageObjectRect.__init__(self, image, height, waist, x, y)
        self.shots = 0

