from state import State

class Problem:
    __initialState: State

    def __init__(self, initalState: State):
        self.__initialState = initalState

    def valueFunction(self,s):
        pass

    def getRandomNeighbor(self,s):
        pass

    def getNeighbors(self,s):
        pass  

    def getInitialState(self):
        return self.__initialState