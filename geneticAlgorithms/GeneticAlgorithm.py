from geneticAlgorithms.operators.Crossover import Crossover
from geneticAlgorithms.operators.Mutation import Mutation
from geneticAlgorithms.operators.Selection import Selection
import numpy as np

class GeneticAlgorithm:
    selection: Selection
    crossover: function
    mutation: function
    __maxGenerations: int

    def __init__(self, maxGenerations,crossoverName,mutationName, possibleValues=None):
        self.__maxGenerations = maxGenerations
        self.selection = Selection()
        self.crossover = Crossover().getCrossoverbyName(crossoverName)
        self.mutation = Mutation(possibleValues).getMutationByName(mutationName)

    def plan(self,population,fitness,goal):
        currentPopulation = population
        t = self.__maxGenerations
        while t != 0:
            if self.__isGoalAccomplished(currentPopulation,fitness,goal):
                return self.__getBestFirstIndividual(currentPopulation,fitness),(self.__maxGenerations - t)

            newPopulation = []
            self.selection.buildSelection(currentPopulation,fitness)
            for index in range(0,len(population),2):
                firstIndividual = self.selection.selectRandom()
                secondIndividual = self.selection.selectRandom()
                firstIndividual,secondIndividual = self.crossover(firstIndividual,secondIndividual)

                prob = np.random.uniform(0.01,0.05)
                res1,res2 = np.random.choice([True,False],2,p=[prob,1-prob])
                if res1:
                    pass
                    firstIndividual = self.mutation(firstIndividual)
                if res2:
                    pass
                    secondIndividual = self.mutation(secondIndividual)

                newPopulation.append(firstIndividual)
                newPopulation.append(secondIndividual)

            currentPopulation = newPopulation

            t -= 1
        return self.__getBestFirstIndividual(currentPopulation,fitness),(self.__maxGenerations - t)

    def __isGoalAccomplished(self, population, fitness, goal):
        for individual in population:
            if fitness(individual) == goal:
                return True
        return False

    def __getBestFirstIndividual(self, population, fitness):
        bestIndividual = population[0]
        for individual in population:
            if fitness(individual) > fitness(bestIndividual):
                bestIndividual = individual
        return bestIndividual
    