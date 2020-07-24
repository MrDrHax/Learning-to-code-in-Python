import pygame, sys, configparser, os, time, subprocess, random
from classXYCordinates import Vector2
from images.imageDict import Images
from levelLoader import Level
from player import Player
from instructionInterpreter import Interpreter as SendCode
from fileMannager import levelLoad as LevelLoad

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

          self.levelLoader = LevelLoad()
          self.sendCode = SendCode({})

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
     
     def drawMsg(self, msg = '', pos = Vector2(), colour = (255,255,255), size = 12):
          """Creates a msg on screen at Vector2 coordinates from top left corner.
          
          colour in RGB touple (0,0,0 is black, 255,255,255 white)
          size is font zize"""
          for i, line in enumerate(msg.splitlines()):
               msg_image =  pygame.font.Font(
                    pygame.font.get_default_font(), size).render(
                         line, False, colour)
          
               self.screenSurface.blit(msg_image, ( pos.X, pos.Y + i * (size+5)))

     def runGame(self):
          """Main function of pygame. All events are handeled here"""
          
          while True:
               if self.player.completed:
                    time.sleep(5)
                    self.changeLevel()
               for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                         self.Quitify()

                    if event.type == pygame.KEYDOWN:
                         if event.key == pygame.K_w:
                              self.player.move()
                         if event.key == pygame.K_a:
                              self.player.rotateLeft()
                         if event.key == pygame.K_d:
                              self.player.rotateRight()
                         if event.key == pygame.K_l:
                              self.levelStringToRun = self.levelLoader.cashToString()
                         if event.key == pygame.K_p:
                              self.changeLevel(0)
                              self.levelStringToRun = self.levelLoader.cashToString()
                              self.sendCode.runInstrucionset(self.levelStringToRun, {
                                   'move': self.player.move , 
                                   'rotateLeft': self.player.rotateLeft, 
                                   'rotateRight': self.player.rotateRight, 
                                   'getFacing': self.player.getFacing, 
                                   'getPlayerPos': self.player.getPlayerPos, 
                                   'getFlagPos': self.player.getFlagPos, 
                                   'getCristalsCollected': self.player.getCristalsCollected, 
                                   'getCristalsTotal': self.player.getCristalsTotal,
                                   'setDelayTime': self.player.setDelayTime
                              })
                         if event.key == pygame.K_n:
                              self.changeLevel()
                         if event.key == pygame.K_b:
                              self.changeLevel(-1)
                         if event.key == pygame.K_r:
                              self.changeLevel(0)
               
               pygame.display.update()
               self.FPS.tick(15)
	
     def Quitify(self):
          """Quits, what did you expect?
          """
          self._center_msg("Exiting...")
          pygame.display.update()
          pygame.quit()
          sys.exit("user exit")

     def drawObject(self, pos = Vector2(), img = "grass tile.png", image = True, size = Vector2()):
          """Draws an image from dictionary of images. 
          Takes in agument pos as Vector2 type.(position is with tileset, not pixelwise) 
          img argument is the image name. If left blank, default is grass tile.
          if image is False, img will be drawn as text, in the posisiton of vector2 on pixel coordinates, not tile coordinates."""
          if image:
               self.screenSurface.blit(self.sprites.images[img], (pos.X * 32,pos.Y * 32))
          else:
               pygame.draw.rect(self.screenSurface, (0,0,0) , (pos.X,pos.Y, size.X, size.Y))
               self.drawMsg(img, pos) #Vector2(10, self.currentLevel.height * 32 + 10))


     def drawLevel(self,level = Level()):
          """ draws a level of type level.
          Usage:
               drawLevel(Level('nameOfLevel.txt'))
               -> if 'level' argument is left blank, default level will be loaded
               -> level takes in a Level() class
               """

          self.currentLevel = level

          # cooses at random place of flag, also can choose special crystals before drawing anything
          possibleLocations = []

          for x in range(0,level.width): 
               for y in range(0,level.height):
                    try:
                         if self.currentLevel.level[y][x] == 'A':
                              if random.randint(0,100) > 60:
                                   s = list(self.currentLevel.level[y])
                                   s[x] = 'S'
                                   self.currentLevel.level[y] = ''.join(s)
                              else:
                                   s = list(self.currentLevel.level[y])
                                   s[x] = 'G'
                                   self.currentLevel.level[y] = ''.join(s)
                         elif self.currentLevel.level[y][x] == 'N':
                              possibleLocations.append([x,y])

                    except Exception as e:
                         print('error in file cleaning: ', e)

          if possibleLocations:
               print('randomizing flag pos')
               chosen = random.randint(0,possibleLocations.__len__()-1)

               xy = possibleLocations[chosen]

               y = possibleLocations[chosen][1]
               x = possibleLocations[chosen][0]

               s = list(self.currentLevel.level[y])
               s[x] = 'M'
               self.currentLevel.level[y] = ''.join(s)

               del possibleLocations[chosen]

               for i in possibleLocations:
                    y = i[1]
                    x = i[0]

                    s = list(self.currentLevel.level[y])
                    s[x] = 'G'
                    self.currentLevel.level[y] = ''.join(s)


          self.player = Player(self.currentLevel ,self.drawObject, self.drawMsg)

          # rezizes the screen zize to fit the level and extra stuff
          self.screenSize = (self.currentLevel.width * 32 + 64, self.currentLevel.height * 32 + 64)
          self.screenSurface = pygame.display.set_mode(self.screenSize)

          for x in range(0,level.width): 
               for y in range(0,level.height):
                    try:
                         if self.currentLevel.level[y][x] == 'G':
                              self.screenSurface.blit(self.sprites.images["grass tile.png"], (x * 32,y * 32))

                         elif self.currentLevel.level[y][x] == 'W':
                              self.screenSurface.blit(self.sprites.images["water tile.png"], (x * 32,y * 32))

                         elif self.currentLevel.level[y][x] == 'M':
                              self.screenSurface.blit(self.sprites.images["grass tile.png"], (x * 32,y * 32))

                              self.screenSurface.blit(self.sprites.images["flag-2.png"], (x * 32,y * 32))
                              self.player.flagPos = Vector2(x,y)

                         elif self.currentLevel.level[y][x] == 'P':
                              self.screenSurface.blit(self.sprites.images["grass tile.png"], (x * 32,y * 32))
                              self.screenSurface.blit(self.sprites.images["Player-1.png"], (x * 32,y * 32))
                              self.player.pos = Vector2(x,y)

                         elif self.currentLevel.level[y][x] == 'S':
                              self.screenSurface.blit(self.sprites.images["grass tile.png"], (x * 32,y * 32))
                              self.screenSurface.blit(self.sprites.images["Crystal.png"], (x * 32,y * 32))
                              self.player.totalCrystalCount += 1

                    except Exception as e:
                         print ('error in', x , y , e)

          if self.player.totalCrystalCount == 0:
               self.screenSurface.blit(self.sprites.images["flag-1.png"], (self.player.flagPos.X * 32,self.player.flagPos.Y * 32))
          
          self.screenSurface.blit(self.sprites.images["Crystal.png"], (self.currentLevel.width * 32 + 16, 16))
          self.drawMsg("Crystals\nobtained:\n\n" + str(self.player.crystalsCollected) + ' / ' + str(self.player.totalCrystalCount), Vector2(self.currentLevel.width * 32 + 7, 50))
          self.drawMsg("Currently running:", Vector2(10, self.currentLevel.height * 32 + 10))
          pygame.display.update()

     def configVars(self):
          """
          Updates ini file, if there is none, it creates a new one
          """
          self.config = configparser.ConfigParser()

          try:
               with open('config.ini', 'x') as configFile:
                    self.config['Player info'] = {'current level' : 0}
                    self.config['Progression'] = {'0' : False}

                    self.config.write(configFile)

          except:
               print('config file already exists, oppening')
          
          self.config = configparser.ConfigParser()
          self.config.read('config.ini')

          print('leading level: ', self.config['Player info']['current level'])

     def updateLevel(self, levelInt : int):
          """
          Updates ini current level variable to 'levelInt'
          """
          self.config['Player info']['current level'] = str(levelInt)
          with open('config.ini', 'w') as configFile:
               self.config.write(configFile)

     def updateLevelStatus(self, levelInt : int, completed : bool):
          """
          Updates ini current level variable to 'levelInt'
          """

          self.config['Progression'][str(levelInt)] = str(completed)
          with open('config.ini', 'w') as configFile:
               self.config.write(configFile)

     def changeLevel(self, amount : int = 1, save = True):
          """
          Changes the level entirely to one that is in a save file

          Usagge:
               amount -> amount of levels to change (default +1), can be negative
               save -> if file is saved before changing cash (level is saved into corresponding txt file)

          """
          levelToChange = int(self.config['Player info']['current level']) + amount

          # if level does not exist, do not procede 
          try:
               # first we save the current level
               try:
                    if save:
                         self.levelLoader.saveLevel('lvl' + str(self.config['Player info']['current level']))
                         self.updateLevelStatus(int(self.config['Player info']['current level']), self.player.completed)
               except Exception as e:
                    print('unable to save, unknown error...',e)
               # then we load the next level
               self.levelLoader.loadLvlIntoCash('lvl' + str(levelToChange))
          except:
               print('level does not exist... ID: ' + str(levelToChange))

          # if it does exist, first update current level ID in config
          self.updateLevel(levelToChange)

          # then, load level assets, to change screen
          self.drawLevel(Level('levels/lvl' + str(levelToChange) + '.txt'))

          # oppen the txt file from the file mannager level loader 
          dirname = os.path.dirname(__file__)
          filename = os.path.join(dirname, self.levelLoader.totalFiles['_cashFile'])
          if sys.platform == "win32":
               os.startfile(filename)
          else: # in case it is not windows.... 
               opener ="open" if sys.platform == "darwin" else "xdg-open"
               subprocess.call([opener, filename])