
class PetState():
        
    FACE = 1, 'Robot Face'
    RADIO = 2, 'Web Radio'
    LIGHT = 3, "Flashlight"

    def __init__(self,value):
        self.value = value        

    def __int__(self):
        return self.value

    def __increment__(self):
        stateCount = 3
        nextState = PetState.__int__(self) + 1
        if nextState > stateCount:
            nextState = 1
        return PetState(nextState)
