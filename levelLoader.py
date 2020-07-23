class Level:
     def __init__(self, txtFile = 'levels/default.txt'):
          """Loads level from txt file. 
          see how to format in  _levelInstructions.txt
          to add a level, add relative path.
          """
          try:
               with open(txtFile) as file:
                    lines = file.read().splitlines()
                    self.height = int(lines[0])
                    del lines[0]
                    self.width = int(lines[0])
                    del lines[0]
                    self.level = lines
          except:
               print ('********** error, file ' + txtFile + ' file NOT FOUND, continuing with default file...')
               with open('levels/default.txt') as file:
                    lines = file.read().splitlines()
                    self.height = int(lines[0])
                    del lines[0]
                    self.width = int(lines[0])
                    del lines[0]
                    self.level = lines

