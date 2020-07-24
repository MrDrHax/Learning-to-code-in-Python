from classXYCordinates import Vector2
import pygame, time

class Player:
     def __init__(self, level, draw, msgDrawer):
          """Player class.
          Only one stance should exist, as more than 1 might interfear. Use from main.py only
          
          Existing commands are:
               move() -> moves the plaver one tile to the front, if whater is non existant
               rotateLeft() -> rotates the player left
               rotateRight() -> rotates the player right
               """
          self.pos = Vector2()
          self.flagPos = Vector2()
          self.facing = 'down'
          self.totalCrystalCount = 0
          self.crystalsCollected = 0
          self.level = level.level
          self.width = level.width
          self.height = level.height
          self.draw = draw #draw object para que pueda dibujar cosas el jugador
          self.drawMsg = msgDrawer # allows text to be written
          self.completed = False
          self.waitTime = 1

     def move(self, spaces = 1):
          """Moves the player on the direction its facing."""

          self.draw(Vector2(20, self.height * 32 + 30) , "", False, Vector2(1000,20))

          self.drawMsg("move()", Vector2(20, self.height * 32 + 30), size = 20)

          time.sleep(self.waitTime)
          
          if self.facing == 'down':
               try:
                    if self.level[self.pos.Y + 1][self.pos.X] != 'W':
                         self.draw(self.pos)
                         self.pos.Y += 1
                         self.drawPlayer()
                         if self.level[self.pos.Y + 1][self.pos.X] != 'M':
                              if self.crystalsCollected == self.totalCrystalCount:
                                   self.draw(self.flagPos, "flag-1.png")
                              else:
                                   self.draw(self.flagPos, "flag-2.png")
                    else:
                         print('there is water there, you will get drowned')
               except:
                    print('out of bounds')
          elif self.facing == 'right':
               try:
                    if self.level[self.pos.Y][self.pos.X + 1] != 'W':
                         self.draw(self.pos)
                         self.pos.X += 1
                         self.drawPlayer()
                         if self.level[self.pos.Y + 1][self.pos.X] != 'M':
                              if self.crystalsCollected == self.totalCrystalCount:
                                   self.draw(self.flagPos, "flag-1.png")
                              else:
                                   self.draw(self.flagPos, "flag-2.png")
                    else:
                         print('there is water there, you will get drowned')
               except:
                    print('out of bounds')
          elif self.facing == 'left':
               try:
                    if self.level[self.pos.Y][self.pos.X - 1] != 'W':
                         self.draw(self.pos)
                         self.pos.X -= 1
                         self.drawPlayer()
                         if self.level[self.pos.Y + 1][self.pos.X] != 'M':
                              if self.crystalsCollected == self.totalCrystalCount:
                                   self.draw(self.flagPos, "flag-1.png")
                              else:
                                   self.draw(self.flagPos, "flag-2.png")
                    else:
                         print('there is water there, you will get drowned')
               except:
                    print('out of bounds')
          elif self.facing == 'up':
               try:
                    if self.level[self.pos.Y - 1][self.pos.X] != 'W':
                         self.draw(self.pos)
                         self.pos.Y -= 1
                         self.drawPlayer()
                         if self.level[self.pos.Y + 1][self.pos.X] != 'M':
                              if self.crystalsCollected == self.totalCrystalCount:
                                   self.draw(self.flagPos, "flag-1.png")
                              else:
                                   self.draw(self.flagPos, "flag-2.png")
                    else:
                         print('there is water there, you will get drowned')
               except:
                    print('out of bounds')
          else:
               print ('error, not facing an accepted direction')
          try:
               if self.level[self.pos.Y][self.pos.X] == 'S':
                    self.crystalsCollected += 1
                    self.level[self.pos.Y] = self.level[self.pos.Y][:self.pos.X] + 'G' + self.level[self.pos.Y][self.pos.X + 1:] # Used to replace a character in a string, to delete the crystal and not having doubles.

                    self.draw(Vector2(self.width * 32 + 7,101) , str(self.crystalsCollected) + ' / ' + str(self.totalCrystalCount), False, Vector2(64,12)) # updates the amount of crystals collected

                    if self.crystalsCollected == self.totalCrystalCount:
                         self.draw(self.flagPos, "flag-1.png")
                         
               elif self.level[self.pos.Y][self.pos.X] == 'M' and self.crystalsCollected == self.totalCrystalCount:
                    self.draw(Vector2(20, self.height * 32 + 30) , "", False, Vector2(1000,20))
                    self.drawMsg("level completed, congratulations!", Vector2(20, self.height * 32 + 30), size = 20)
                    print('level finished, congratulations')
                    self.completed = True
                    raise NameError('Completed')
          
          except NameError as e:
               raise NameError('Completed')
          except:
               print ('somehow youve done it, and player is out of bounds')
     
     def rotateLeft(self):
          """Rotates..."""
          self.draw(Vector2(20, self.height * 32 + 30) , "", False, Vector2(1000,20))
          self.drawMsg("rotateLeft()", Vector2(20, self.height * 32 + 30), size = 20)
          time.sleep(self.waitTime)
          if self.facing == 'left':
               self.facing = 'down'
          elif self.facing == 'down':
               self.facing = 'right'
          elif self.facing == 'right':
               self.facing = 'up'
          elif self.facing == 'up':
               self.facing = 'left'
          self.drawPlayer()

     def rotateRight(self):
          """Rotates..."""
          self.draw(Vector2(20, self.height * 32 + 30) , "", False, Vector2(1000,20))
          self.drawMsg("rotateRight()", Vector2(20, self.height * 32 + 30), size = 20)
          time.sleep(self.waitTime)
          if self.facing == 'left':
               self.facing = 'up'
          elif self.facing == 'down':
               self.facing = 'left'
          elif self.facing == 'right':
               self.facing = 'down'
          elif self.facing == 'up':
               self.facing = 'right'
          self.drawPlayer()

     def getFacing(self):
          return self.facing

     def getPlayerPos(self):
          return self.pos

     def getFlagPos(self):
          return self.flagPos

     def getCristalsCollected(self):
          return self.crystalsCollected

     def getCristalsTotal(self):
          return self.totalCrystalCount

     def setDelayTime(self, delay = 1):
          self.waitTime = delay
     
     def drawPlayer(self):
          """Helper to draw the player always on the screen the correct way."""
          self.draw(self.pos)
          if self.level[self.pos.Y][self.pos.X] == 'M':
               if self.crystalsCollected == self.totalCrystalCount:
                    self.draw(self.pos, "flag-1.png")
               else:
                    self.draw(self.pos, "flag-2.png")
          if self.facing == 'down':
               self.draw(self.pos, "Player-1.png")
          elif self.facing == 'left':
               self.draw(self.pos, "Player-4.png")
          elif self.facing == 'right':
               self.draw(self.pos, "Player-2.png")
          elif self.facing == 'up':
               self.draw(self.pos, "Player-3.png")

          for event in pygame.event.get():
               if event.type == pygame.QUIT:
                    self.Quitify()
                    
          pygame.display.update()
