from classXYCordinates import Vector2
import pygame

class Player:
     def __init__(self, level, draw):
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
          self.draw = draw #draw object para que pueda dibujar cosas el jugador

     def move(self, spaces = 1):
          """Moves the player on the direction its facing. Returns True if is on goal && has collected all gems."""
          if self.facing == 'down':
               try:
                    if self.level[self.pos.Y + 1][self.pos.X] != 'W':
                         self.draw(self.pos)
                         self.pos.Y += 1
                         self.drawPlayer()
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
                    print('level finished, congratulations')
                    return(True)

          except:
               print ('somehow youve done it, and player is out of bounds')
     
     def rotateLeft(self):
          """Rotates..."""
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
          if self.facing == 'left':
               self.facing = 'up'
          elif self.facing == 'down':
               self.facing = 'left'
          elif self.facing == 'right':
               self.facing = 'down'
          elif self.facing == 'up':
               self.facing = 'right'
          self.drawPlayer()
     
     def drawPlayer(self):
          """Helper to draw the player always on the screen the correct way."""
          self.draw(self.pos)
          if self.level[self.pos.Y][self.pos.X] == 'M':
               if self.crystalsCollected == self.totalCrystalCount:
                    self.draw(self.pos, "flag-1.png")
               else:
                    self.draw(self.pos, "flag-2.png")

          if self.facing == 'left':
               self.draw(self.pos, "Player-1.png")
          elif self.facing == 'down':
               self.draw(self.pos, "Player-4.png")
          elif self.facing == 'right':
               self.draw(self.pos, "Player-2.png")
          elif self.facing == 'up':
               self.draw(self.pos, "Player-3.png")
          pygame.display.update()
