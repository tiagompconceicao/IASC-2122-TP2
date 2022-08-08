from state.State import State
import random


class TravellerState(State):
    x_min, x_max = 8, 16
    y_min, y_max = 6, 12
    numberOfCities: int
    def __init__(self,numberOfCities,configuration = []):
        self.numberOfCities = numberOfCities
        if len(configuration) == 0:
            configuration = self.generateConfiguration()
        super().__init__(configuration)

    def generateConfiguration(self):
        config = []
        for i in range(self.numberOfCities):
            x = random.uniform(self.x_min,self.x_max)
            y = random.uniform(self.y_min,self.y_max)
            config.append((x,y))
        return config