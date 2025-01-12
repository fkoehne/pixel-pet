
from Radio import Radio
from RobotFace import RobotFace
from Life import Life
from MusicPlayer import MusicPlayer

class PetState():

    def __init__(self, sense):     
        self.sense = sense
        self.FACE = 1, RobotFace(sense)
        self.RADIO = 2, Radio(sense)
        self.LIFE = 3, Life(sense, 8, 8)
        self.MUSICPLAYER = 4, MusicPlayer(sense)

        self.stateList = (self.FACE, self.RADIO, self.LIFE, self.MUSICPLAYER)
        
        # Start with some state
        self.current = self.MUSICPLAYER
        self.current[1].select()  


    def increment(self):
        """Cycles through the robot states sequentially and
           triggers their deselection and selection.

        """        
        self.current[1].deselect()
        nextState = self.current[0] + 1
        if nextState > len(self.stateList):
            nextState = 1
        
        self.current = self.stateList[nextState - 1]
        self.current[1].select()

    def signal(self, code):
        self.current[1].signal(code)
        
    def loop(self):
        self.current[1].loop()  

    def sleep(self):
        self.current[1].deselect()
        self.current = self.FACE
        self.current[1].select()

