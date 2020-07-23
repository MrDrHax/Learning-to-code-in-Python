import os, pygame

class Images:
     images = {}

     def __init__(self):
          """Cretes an image dictionary ready to be used in pygame. 

          ONLY PNG IMAGES ARE SUPPORTED"""
          print('loading images')
          sprites = []
          for root, dirs, files in os.walk("images", topdown=False):
               for name in files:
                    if name.endswith('.png'):
                         sprites.append(name)

          for sprite in sprites:
               Images.images[sprite] = pygame.image.load(os.path.join('images', sprite))
          print('images loaded')