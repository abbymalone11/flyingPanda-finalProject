import pygame, simpleGE, random


class LblScore(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.text = "Score: 0"
        self.center = (100, 100)
        self.fgColor = "black"
        self.clearBack = True

class LblTimer(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.text = "Time: 5"
        self.center = (550, 100)
        self.fgColor = "black"
        self.clearBack = True

class Panda(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("panda.png")
        self.setSize(100, 100)
        self.position = (100, 100)       
    
    def process(self):
        self.addForce(.1, 270)
        if self.scene.isKeyPressed(pygame.K_SPACE):
            self.dy = 0
            self.addForce(5, 90)    
    def reset(self):
        self.x = random.randint(0, self.scene.background.get_width())
        self.y = 20
        self.dy = random.randint(5, 15)
         
    def checkBounds(self):
        if self.bottom > self.scene.background.get_height():
            self.reset()
        
class Barrier(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.colorRect("green", (80, 200))
        self.position = (600, 0)    
        self.dx = -3
        
    def checkBounds(self):
        #only check for leave left
        if self.x < 0:
            self.scene.reset()
            
class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.Panda = Panda(self)
        self.setImage("forest.jpg")
        self.upperBarrier = Barrier(self)
        self.lowerBarrier = Barrier(self)
        self.gap = 400
        self.reset()
        self.sprites = [self.Panda, self.upperBarrier, self.lowerBarrier]
        self.score = 0
        self.lblScore = LblScore()

        self.timer = simpleGE.Timer()
        self.timer.totalTime = 10
        self.lblTimer = LblTimer()

    def reset(self):        
        self.topPosition = random.randint(0, 200)
        self.bottomPosition = self.topPosition + self.gap
        self.upperBarrier.position = (640, self.topPosition)
        self.lowerBarrier.position = (640, self.bottomPosition)
     
    def process(self):
        super().process()
        if self.Panda.collidesWith(self.upperBarrier) or self.Panda.collidesWith(self.lowerBarrier):
            self.Panda.reset()
            self.score += 100
            self.lblScore.text = f"Score: {self.score}"
            
        self.lblTimer.text = f"Time Left: {self.timer.getTimeLeft():.2f}"
        if self.timer.getTimeLeft() < 0:
            print(f"Score: {self.score}")
            self.stop()
        
class Instructions(simpleGE.Scene):
    def __init__(self, prevScore):
        super().__init__()
        self.prevScore = prevScore
        self.setImage("forest.jpg")
        self.response = None
        self.directions = simpleGE.MultiLabel()
        self.directions.textLines = [
            "You are a Panda",
            "Move up with the space key",
            "Go through the barriers",
            "Each barrier passed is 100 points",
            "Good Luck!"
        ]
        self.directions.center = (320, 240)
        self.directions.size = (500, 250)
        self.btnPlay = simpleGE.Button()
        self.btnPlay.text = "Play"
        self.btnPlay.center = (100, 400)
        self.btnPlay.onClick = self.playClicked  # Event handler
        self.btnQuit = simpleGE.Button()
        self.btnQuit.text = "Quit"
        self.btnQuit.center = (540, 400)
        self.lblScore = simpleGE.Label()
        self.lblScore.text = f"Last score: {self.prevScore}"
        self.lblScore.center = (320, 400)
        self.sprites = [self.directions,
                        self.btnPlay,
                        self.btnQuit,
                        self.lblScore]       

    def playClicked(self):
        self.response = "Play"

class GameOver(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("forest.jpg")
        self.lblScore = simpleGE.Label()
        self.lblScore.text = "Score: 0"
        self.lblScore.center = (320, 100)
        self.lblScore.fgColor = "white"
        
        self.btnQuit = simpleGE.Button()
        self.btnQuit.text = "Quit"
        self.btnQuit.center = (100, 240)
        
        self.btnAgain = simpleGE.Button()
        self.btnAgain.text = "Play Again"
        self.btnAgain.center = (450, 240)
        
        self.sprites = [self.lblScore, 
                        self.btnQuit, 
                        self.btnAgain]
        
    def setScore(self, score):
        self.lblScore.text = f"Score: {score}"
        
    def process(self):
        super().process()
        if self.btnQuit.clicked:
            self.next = "quit"
            self.stop()
        if self.btnAgain.clicked:
            self.next = "again"
            self.stop()

def main():
    #keepGoing = True
    lastScore = 0
    #while keepGoing:
    instructions = Instructions(lastScore)
    instructions.start()
    if instructions.response == "Play":
        print("game playing")
        #game = Game()
        #game.start()
            #lastScore = game.score
            #gameOver = GameOver()
            #gameOver.setScore(game.score)
            #sgameOver.start()
        
    #if gameOver.next == "quit":
            #keepGoing = False

        

if __name__ == "__main__":
    main()

