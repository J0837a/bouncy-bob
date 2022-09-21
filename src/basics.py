import pygame as game
import os

def loadFromAssets(file):
    return game.image.load(os.path.join("Assets", file))