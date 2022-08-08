from geneticAlgorithms.operators.Crossover import Crossover
from geneticAlgorithms.GeneticAlgorithm import GeneticAlgorithm
from geneticAlgorithms.operators.Selection import Selection
from geneticAlgorithms.population.QueenPopulation import QueenPopulation
from geneticAlgorithms.population.TravellerPopulation import TravellerPopulation
from view.TravellerView import TravellerView
from view.QueensView import QueensView
import numpy as np
import math
import pygad

#Fitness function for the N-Queens problem and its auxiliary functions
def fitnessQueens(individual, individualIdx=None):
        individual = np.array(individual)
        individual = individual.astype(int)
        score = 0
        for columnIndex in range(len(individual)):
            queen = individual[columnIndex]
            if (not(hasDiagonalsNeighbors(individual,columnIndex,queen))) & (not(hasHorintalNeighbors(individual,columnIndex,queen))):
                score += 1
        return score

def hasDiagonalsNeighbors(config, columnIndexToWatch,queen):
    for columnIndex in range(len(config)):
        CollumnDistance = math.sqrt((columnIndex - columnIndexToWatch) ** 2)
        if columnIndex == columnIndexToWatch:
            continue
        if ((config[columnIndex] == (queen + CollumnDistance))):
            return True
        if ((config[columnIndex] == (queen - CollumnDistance))):
            return True
    return False

def hasHorintalNeighbors(config, columnIndexToWatch, queen):
    for columnIndex in range(len(config)):
        if columnIndex == columnIndexToWatch:
            continue
        if config[columnIndex] == queen:
            return True
    return False


#Fitness function for the traveller problem and its auxiliary functions
def fitnessCities(individual,individualIdx=None):
        distanceSum = 0
        for cityIndex in range(len(individual) - 1):
            distanceSum += calculateDistance(individual[cityIndex],individual[cityIndex + 1])

        #Only remains to calculate the distance from the last city to the first one
        distanceSum += calculateDistance(individual[len(individual) - 1],individual[0])
        return (len(individual)/distanceSum)

def calculateDistance(city1,city2):
        aux = ((city1[0] - city2[0]) ** 2) + ((city1[1] - city2[1]) ** 2)
        return math.sqrt(aux)



#Main function
def main():
    crossover="uniformCrossover"
    mutation = "mutateOneChild"
    possibleValues=np.arange(16)

    
    genetic = GeneticAlgorithm(500,crossover,mutation,possibleValues)
    queens = QueenPopulation()
    traveller = TravellerPopulation()
    view = QueensView()
    population = queens.generatePopulation(10,16)
    population2 = traveller.generatePopulation(100,10)
    res,iterations = genetic.plan(population,fitnessQueens,16)
    res2,iterations2 = genetic.plan(population2,fitnessCities,len(population[0]))
    print(res)
    print(fitnessQueens(res))
    print("in %d iterations" % iterations)


    ga_instance = pygad.GA(num_generations=50,
                       num_parents_mating=1,
                       fitness_func=fitnessQueens,
                       initial_population=population,
                       sol_per_pop=1,
                       num_genes=10,
                       parent_selection_type="sss",
                       keep_parents=1,
                       crossover_type="single_point",
                       mutation_type="random",
                       mutation_percent_genes=5)
    ga_instance.run()
    res3 = ga_instance.best_solution()
    print(res3)

#Execute main function
main()