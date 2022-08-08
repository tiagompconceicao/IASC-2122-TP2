import matplotlib.pyplot as plt
import numpy as np
from view.View import View

class TravellerView(View):

    def __init__(self):
        pass
    def __separateCoordinates(self,values):
        x_values = np.zeros( len(values) + 1 )
        y_values = np.zeros( len(values) + 1 )
        for i in range(len(values)):
            x_values[i] = values[i][0]
            y_values[i] = values[i][1]

        #The last city will connect with the first
        x_values[len(x_values) - 1] = values[0][0]
        y_values[len(y_values) - 1] = values[0][1]
        return x_values,y_values

    def draw(self,data):
        x_values,y_values = self.__separateCoordinates(data)
        plt.scatter(x_values,y_values)
        plt.plot(x_values, y_values)
        plt.show()