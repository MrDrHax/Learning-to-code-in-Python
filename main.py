import pygame, sys
from classXYCordinates import Vector2
from images.imageDict import Images
from levelLoader import Level
from player import Player

class mainGame:

     def __init__(self, screenSize = (640,320)):
          self.sprites = Images()
          print(self.sprites.images)
          self.screenSize = screenSize

          pygame.init() # iniciar pygame
          pygame.display.set_caption("Learn python") # ponerle arriba

          self.screenSurface = pygame.display.set_mode(screenSize)
          self.FPS = pygame.time.Clock()

          self.player = Player()

     def _center_msg(self, msg):
          for i, line in enumerate(msg.splitlines()):
               msg_image =  pygame.font.Font(
                    pygame.font.get_default_font(), 12).render(
                         line, False, (255,255,255), (0,0,0))
          
               msgim_center_x, msgim_center_y = msg_image.get_size()
               msgim_center_x //= 2
               msgim_center_y //= 2
          
               self.screenSurface.blit(msg_image, ( self.screenSize[0] // 2-msgim_center_x, self.screenSize[1] // 2-msgim_center_y+i*22))

     def runGame(self):

          while True:
               for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                         self.Quitify()
                    # elif event.type == pygame.KEYDOWN:

               
               pygame.display.update()
               self.FPS.tick(15)
	
     def Quitify(self):
	     self._center_msg("Exiting...")
	     pygame.display.update()
	     pygame.quit()
	     sys.exit("user exit")

     def drawLevel(self,level = Level()):
          self.currentLevel = level
          for y in range(0,level.width):
               for x in range(0,level.height):
                    try:
                         if level.level[x][y] == 'G':
                              self.screenSurface.blit(self.sprites.images["grass tile.png"], (y * 32,x * 32))
                         elif level.level[x][y] == 'W':
                              self.screenSurface.blit(self.sprites.images["water tile.png"], (y * 32,x * 32))
                         elif level.level[x][y] == 'M':
                              self.screenSurface.blit(self.sprites.images["grass tile.png"], (y * 32,x * 32))
                              self.screenSurface.blit(self.sprites.images["flag-2.png"], (y * 32,x * 32))
                              self.player.flagPos = Vector2(x,y)
                         elif level.level[x][y] == 'P':
                              self.screenSurface.blit(self.sprites.images["grass tile.png"], (y * 32,x * 32))
                              self.screenSurface.blit(self.sprites.images["Player-1.png"], (y * 32,x * 32))
                              self.player.pos = Vector2(x,y)
                              self.currentLevel[x][y] = 'G'
                         elif level.level[x][y] == 'S':
                              self.screenSurface.blit(self.sprites.images["grass tile.png"], (y * 32,x * 32))
                              self.screenSurface.blit(self.sprites.images["Crystal.png"], (y * 32,x * 32))
                              self.player.flagPos = Vector2(x,y)
                              self.player.totalCrystalCount += 1
                    except:
                         print ('error in', x,y)
                    

game = mainGame()

coords = Vector2(10,20)
print (coords.X)

game.drawLevel()

print(game.player.totalCrystalCount)

game.runGame()