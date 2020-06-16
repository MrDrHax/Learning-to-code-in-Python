from classXYCordinates import Vector2

class Player:
     def __init__(self):
          self.pos = Vector2()
          self.flagPos = Vector2()
          self.facing = 'down'
          self.totalCrystalCount = 0
          self.crystalsCollected = 0