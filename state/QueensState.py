from state.State import State
import random


class QueensState(State):

    numberOfQueens: int

    def __init__(self,numberOfQueens, configuration=[]):
        self.numberOfQueens = numberOfQueens
        if len(configuration) == 0:
            configuration = self.generateConfiguration()
        super().__init__(configuration)

    def generateConfiguration(self):
        config = []
        for i in range(self.numberOfQueens):
            config.append(self.__generateQueen())
        return config
    
    def __generateQueen(self):
        return random.randint(0,self.numberOfQueens - 1)