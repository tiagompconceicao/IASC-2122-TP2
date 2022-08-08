import numpy as np


class Mutation:
    __possibleValues:list
    def __init__(self,possibleValues=None):
        self.__possibleValues = possibleValues

    def getMutationByName(self,name):
        if name == "mutateOrder":
            return self.mutateOrder
        elif name == "mutateOneChild":
            return self.mutateOneChild
        else:
            return None  

    def mutateOrder(self, child):
        indexes = np.random.randint(0,len(child)-1,size=2)
        aux = child[indexes[0]]
        child[indexes[0]] = child[indexes[1]]
        child[indexes[1]] = aux
        return child

    def mutateOneChild(self, child):
        index = np.random.randint(0,len(child)-1)
        value = np.random.choice(self.__possibleValues)
        child[index] = value
        return child
