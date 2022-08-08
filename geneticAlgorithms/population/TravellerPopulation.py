from geneticAlgorithms.population.Population import Population
from state.TravellerState import TravellerState

class TravellerPopulation(Population):
    def __init__(self):
        super().__init__()

    def generatePopulation(self, numberOfIndividuals, numberOfCities):
        ts = TravellerState(numberOfCities)
        population = []
        for i in range(numberOfIndividuals):
            population.append(ts.generateConfiguration())
        return population