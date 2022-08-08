import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np
from state.QueensState import QueensState
from view.View import View


class QueensView(View):
    def __init__(self):
        super().__init__()
        

    def prepareData(self, array, numOfQueens):
        new_array = np.zeros((numOfQueens, numOfQueens))
        for i in range(numOfQueens):
            new_array[i][array[i]] = 1
        print(new_array)
        return new_array


    def draw(self, array, numOfQueens):
        # create discrete colormap
        data = self.prepareData(array,numOfQueens)
        cmap = colors.ListedColormap(['white','grey'])
        bounds = [0,1,1]
        norm = colors.BoundaryNorm(bounds, cmap.N)

        fig, ax = plt.subplots()
        ax.imshow(data, cmap=cmap, norm=norm)

        # draw gridlines
        ax.grid(which='major', axis='both', linestyle='-', color='k', linewidth=2)
        
        ax.set_xticks(np.arange(-0.5, numOfQueens - 0.5, 1))
        ax.set_yticks(np.arange(-0.5, numOfQueens - 0.5, 1))
        labels_x = [item.get_text() for item in ax.get_xticklabels()]
        labels_y = [item.get_text() for item in ax.get_yticklabels()]
        for i in range(numOfQueens):
            labels_x[i] = i
            labels_y[i] = i
        ax.set_xticklabels(labels_x)
        ax.set_yticklabels(labels_y)

        plt.show()