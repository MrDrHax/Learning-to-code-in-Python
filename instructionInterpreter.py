from player import Player
import time

class Interpreter():
     def __init__(self, inClass : dict):
          """
          creates a code interpreter from string to running in a safe enviorment
          inClass must be method class directory
          """
          self.instructions = ''
          self.playerClass = inClass

     def runInstrucionset(self, toRun : str, internalVariables : dict = None):
          '''
          gets a set of instructions and runs it as native. 
          
          The dict type will be used to limit range, use with care.

          Returns finished runin if sucsesfull, else, it will return the exception.
          '''
          self.instructions = toRun

          
          self.playerClass = internalVariables

          self.playerClass['running'] = self.running
          self.playerClass['time'] = time


          try:
               exec(self.instructions, self.playerClass)
               return 'Code finished running'
          except NameError as e:
               if e == 'Completed':
                    print ('done')
               else:
                    print(e)
          except Exception as e:
               print(e)
               return e

     def running(self, string):
          print(string)

