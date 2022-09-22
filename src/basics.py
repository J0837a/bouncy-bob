import pygame as game
import os

bulletHitInvader = game.USEREVENT + 1

def loadFromAssets(file):
    return game.image.load(os.path.join("Assets", file))