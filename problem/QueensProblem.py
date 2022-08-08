import numpy as np
from numpy.lib.function_base import append
from problem.Problem import Problem
from state.QueensState import QueensState
from state.State import State
import math

class QueenProblem(Problem):
    currentState: QueensState
    currentNeighbors: list
    def __init__(self, initalState: State):
        self.currentState = initalState
        self.currentNeighbors = self.getNeighbors(initalState)
        super().__init__(initalState)

    def valueFunction(self, state: QueensState):
        score = 0
        for columnIndex in range(state.numberOfQueens):
            queen = state.config[columnIndex]
            if (not(self.__hasDiagonalsNeighbors(state.config,columnIndex,queen))) & (not(self.__hasHorintalNeighbors(state.config,columnIndex,queen))):
                score += 1
        return score

    def getRandomNeighbor(self, state: QueensState):
        if state != self.currentState:
            self.currentState = state
            self.currentNeighbors = self.getNeighbors(state)
        if len(self.currentNeighbors) == 0:
            return None
        neighborsIndexes = range(len(self.currentNeighbors))
        randomNeighbor = self.currentNeighbors.pop(np.random.choice(neighborsIndexes,1)[0])
        return randomNeighbor
        

    def getNeighbors(self, state: QueensState):
        neighbors = []
        for queenIndex in range(len(state.config)):
            queen = state.config[queenIndex]
            possiblePositions = [newQueen for newQueen in range(state.numberOfQueens) if newQueen != queen]
            for position in possiblePositions:
                new = self.__changeQueenPosition(state,queenIndex,position)
                neighbors.append(new)

        return neighbors

    def __changeQueenPosition(self,state:QueensState,queenIndex, newPosition):
            newConfig = state.config.copy()
            newConfig[queenIndex] = newPosition
            return QueensState(state.numberOfQueens,newConfig)

    def __hasDiagonalsNeighbors(self,config, columnIndexToWatch,queen):
        for columnIndex in range(len(config)):
            CollumnDistance = math.sqrt((columnIndex - columnIndexToWatch) ** 2)
            if columnIndex == columnIndexToWatch:
                continue
            if ((config[columnIndex] == (queen + CollumnDistance))):
                return True
            if ((config[columnIndex] == (queen - CollumnDistance))):
                return True
        return False

    def __hasHorintalNeighbors(self,config, columnIndexToWatch, queen):
        for columnIndex in range(len(config)):
            if columnIndex == columnIndexToWatch:
                continue
            if config[columnIndex] == queen:
                return True
        return False