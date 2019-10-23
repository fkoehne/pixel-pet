from aenum import Enum, MultiValue
class PetState(Enum):
    
    _init_ = 'value fullname'
    _settings_ = MultiValue

    FACE = 1, 'Robot Face'
    RADIO = 2, 'Web Radio'
    LIGHT = 3, "Flashlight"

    def __int__(self):
        return self.value

    def __increment__(self):
        stateCount = 3
        nextState = PetState.__int__(self) + 1
        if nextState > stateCount:
            nextState = 1
        return PetState(nextState)
