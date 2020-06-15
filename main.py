import pygame, sys

class mainGame:

     def __init__(self, screenSize = (100,100)):
          pygame.init() # iniciar pygame
          pygame.display.set_caption("Learn python") # ponerle arriba

          self.screenSurface = pygame.display.set_mode(screenSize)
          self.FPS = pygame.time.Clock()

     def _main(self):
          print('lol')

     def _center_msg(self, msg):
          for i, line in enumerate(msg.splitlines()):
               msg_image =  pygame.font.Font(
                    pygame.font.get_default_font(), 12).render(
                         line, False, (255,255,255), (0,0,0))
          
               msgim_center_x, msgim_center_y = msg_image.get_size()
               msgim_center_x //= 2
               msgim_center_y //= 2
          
               self.screenSurface.blit(msg_image, (
                    self.screenSize[0] // 2-msgim_center_x,
                    self.screenSize[1] // 2-msgim_center_y+i*22))

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

game = mainGame((800,900))

game.runGame()