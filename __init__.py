import main

game = main.mainGame((700,400))

game.drawLevel()

game.configVars()

game.changeLevel(0,False)

game.startTkInter()

game.runGame()
