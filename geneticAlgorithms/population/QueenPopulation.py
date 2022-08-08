

from geneticAlgorithms.population.Population import Population
from state.QueensState import QueensState


class QueenPopulation(Population):
    def __init__(self):
        super().__init__()

    def generatePopulation(self, numberOfIndividuals, numberOfQueens):
        queen = QueensState(numberOfQueens)
        population = []
        for i in range(numberOfIndividuals):
            population.append(queen.generateConfiguration())
        return population