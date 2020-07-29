import os
import pygame, sys

class levelLoad():
     totalFiles = {}
     def __init__(self):
          """Cretes a file level dictionary ready to be used in pygame. 

          ONLY .txt FILES ARE SUPPORTED"""
          print('loading files')
          files = []
          for root, dirs, foundFiles in os.walk("levelSaves", topdown=False):
               for name in foundFiles:
                    if name.endswith('.txt'):
                         files.append(name)

          for file in files:
               levelLoad.totalFiles[file[:-4]] = 'levelSaves/' + file
          print('files loaded')

     def loadLvlIntoCash(self,level : str):
          '''
          load string level into cash.
          do not insert .txt
          '''
          try:
               levelLoaded = open(levelLoad.totalFiles[level])  
          except Exception as e:
               print('error reading file: ' + level + ' --- Exception ---', e )
               return None

          try:
               cash = open(levelLoad.totalFiles['_cashFile'],'x')
          except:
               cash = open(levelLoad.totalFiles['_cashFile'],'w+')

          txtTransfer = levelLoaded.read()

          cash.write(txtTransfer)

          levelLoaded.close()
          cash.close()
          print('level loaded into cash')
     
     def saveLevel(self, safeToLvl : str):
          '''
          Save from cash to specified level. Level has to exist from before.
          do not insert .txt
          '''
          try:
               levelLoaded = open(levelLoad.totalFiles[safeToLvl], 'w+')  
          except Exception as e:
               print('error reading file: ' + safeToLvl + ' --- Exception ---', e )
               return None

          cash = open(levelLoad.totalFiles['_cashFile'])

          txtTransfer = cash.read()

          levelLoaded.write(txtTransfer)

          levelLoaded.close()
          cash.close()
          print('level saved from cash to: ' + safeToLvl)

     def updateCash(self, saveString : str):
          '''
          Save from string to cash, overwrites everything!
          '''

          cash = open(levelLoad.totalFiles['_cashFile'], 'w+')

          cash.write(saveString)

          cash.close()

     def cashToString(self):
          '''
          Returns a string of the cash.
          Lines are already split.
          '''
          with open(levelLoad.totalFiles['_cashFile']) as cash:
               toReturn = cash.read()
               toReturn = toReturn.splitlines()

          return toReturn
