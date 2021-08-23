import pygame.freetype
import os
dirname = os.path.dirname(__file__)
fontPath = os.path.join(dirname, '../assets/arcadeFont.ttf')

pygame.freetype.init()

PYCADE_FONT = pygame.freetype.Font(fontPath, 24)
