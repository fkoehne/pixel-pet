
from Radio import Radio
from RobotFace import RobotFace

class PetState():

    def __init__(self, sense):     
        self.sense = sense
        self.FACE = 1, RobotFace(sense)
        self.RADIO = 2, Radio(sense)
        
        self.stateList = (self.FACE, self.RADIO)
        
        # Start with the face
        self.current = self.FACE  

    def __increment__(self):
        stateCount = 2
        self.current[1].deselect()
        nextState = self.current[0] + 1
        if nextState > stateCount:
            nextState = 1
        
        self.current = self.stateList[nextState - 1]
        self.current[1].select()


