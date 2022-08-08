import numpy as np

class Selection:
    __probs: list
    __population: list
    def __init__(self):
        pass

    def buildSelection(self, population, fitness):
        self.__probs = []
        self.__population = population
        populationFitness = []
        totalFitness = 0
        for individual in population:
            individualFitness = fitness(individual)
            populationFitness.append(individualFitness)
            totalFitness += individualFitness

        for individualIndex  in range(len(population)):
            self.__probs.append(populationFitness[individualIndex]/totalFitness)
    
    def selectRandom(self):
        indexes = np.arange(len(self.__population))
        newIndividualIndex = np.random.choice(indexes,1,p=self.__probs)[0]
        return self.__population[newIndividualIndex]
