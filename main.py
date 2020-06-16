import pygame, sys
from classXYCordinates import Vector2
from images.imageDict import Images
from levelLoader import Level
from player import Player

class mainGame:

     def __init__(self, screenSize = (640,320)):
          """The main part of the game

          takes in the values of the screen, as a touple in (X,Y) format. 
          default is (640,320)

          ! this just starts pygame, it does not run anything else, to run pygame use mainGame.runGame()
          """
          self.sprites = Images()
          self.screenSize = screenSize

          pygame.init() # start pygame
          pygame.display.set_caption("Learn python") # add text to window

          self.screenSurface = pygame.display.set_mode(screenSize)
          self.FPS = pygame.time.Clock()

          

     def _center_msg(self, msg):
          """ creates a centalized msg on screen"""
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

     def drawObject(self, pos = Vector2(), img = "grass tile.png"):
          self.screenSurface.blit(self.sprites.images[img], (pos.X * 32,pos.Y * 32))

     def drawLevel(self,level = Level()):
          self.currentLevel = level
          self.player = Player(self.currentLevel ,self.drawObject)
          for x in range(0,level.width): 
               for y in range(0,level.height):
                    try:
                         if level.level[y][x] == 'G':
                              self.screenSurface.blit(self.sprites.images["grass tile.png"], (x * 32,y * 32))
                         elif level.level[y][x] == 'W':
                              self.screenSurface.blit(self.sprites.images["water tile.png"], (x * 32,y * 32))
                         elif level.level[y][x] == 'M':
                              self.screenSurface.blit(self.sprites.images["grass tile.png"], (x * 32,y * 32))
                              self.screenSurface.blit(self.sprites.images["flag-2.png"], (x * 32,y * 32))
                              self.player.flagPos = Vector2(x,y)
                         elif level.level[y][x] == 'P':
                              self.screenSurface.blit(self.sprites.images["grass tile.png"], (x * 32,y * 32))
                              self.screenSurface.blit(self.sprites.images["Player-1.png"], (x * 32,y * 32))
                              self.player.pos = Vector2(x,y)
                         elif level.level[y][x] == 'S':
                              self.screenSurface.blit(self.sprites.images["grass tile.png"], (x * 32,y * 32))
                              self.screenSurface.blit(self.sprites.images["Crystal.png"], (x * 32,y * 32))
                              self.player.totalCrystalCount += 1
                    except Exception as e:
                         print ('error in', x,y , e)
          
          pygame.display.update()
                    
game = mainGame()

game.drawLevel()

game.runGame()