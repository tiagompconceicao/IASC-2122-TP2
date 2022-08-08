from problem.Problem import Problem
import math
from state.TravellerState import TravellerState 
import numpy as np

class TravellerProblem(Problem):
    
    currentState: TravellerState
    currentNeighbors: list

    def __init__(self,initialState: TravellerState):
        self.currentState = initialState
        self.currentNeighbors = self.getNeighbors(initialState)
        super().__init__(initialState)

    def valueFunction(self,state:TravellerState):
        distanceSum = 0
        for cityIndex in range(len(state.config) - 1):
            distanceSum += self.__calculateDistance(state.config[cityIndex],state.config[cityIndex + 1])


        #Only remains to calculate the distance from the last city to the first one
        distanceSum += self.__calculateDistance(state.config[len(state.config) - 1],state.config[0])
        return -distanceSum

    def getNeighbors(self, state: TravellerState):
        neighbors = []
        for cityIndex in range(len(state.config)):
            neighbor = self.__switchTwoNeighborCities(state,cityIndex)
            neighbors.append(neighbor)
        return neighbors

    def getRandomNeighbor(self, state: TravellerState):
        if state != self.currentState:
            self.currentState = state
            self.currentNeighbors = self.getNeighbors(state)
        if len(self.currentNeighbors) == 0:
            return None
        neighborsIndexes = range(len(self.currentNeighbors))
        randomNeighbor = self.currentNeighbors.pop(np.random.choice(neighborsIndexes,1)[0])
        return randomNeighbor

    def __switchTwoNeighborCities(self, state:TravellerState, firstCityIndex):
        newConfig = state.config.copy()
        if firstCityIndex == state.numberOfCities - 1:
            auxCity = newConfig[0]
            newConfig[0] = newConfig[firstCityIndex]
            newConfig[firstCityIndex] = auxCity
        else:
            auxCity = newConfig[firstCityIndex + 1]
            newConfig[firstCityIndex + 1] = newConfig[firstCityIndex]
            newConfig[firstCityIndex] = auxCity

        return TravellerState(state.numberOfCities,newConfig)

    def __calculateDistance(self, city1,city2):
        aux = ((city1[0] - city2[0]) ** 2) + ((city1[1] - city2[1]) ** 2)
        return math.sqrt(aux)
