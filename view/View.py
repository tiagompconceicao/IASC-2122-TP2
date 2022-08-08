

from matplotlib import pyplot as plt


class View:
    def __init__(self):
        pass
    
    def draw(self,data):
        pass

    def drawFValueEvoluation(self, data, numberOfIterations):            
        plt.plot(range(numberOfIterations), data)
        plt.show()
