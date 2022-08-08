import numpy as np
from numpy.core.fromnumeric import cumprod


class Crossover:
    def __init__(self):
        pass

    def getCrossoverbyName(self, name):
        if name == "crossWithOrderPreservation":
            return self.crossWithOrderPreservation
        elif name == "onePointCrossover":
            return self.onePointCrossover
        elif name == "twoPointsCrossover":
            return self.twoPointsCrossover
        elif name == "uniformCrossover":
            return self.uniformCrossover
        else:
            return None  

    #Para cada 2 individuos da população
    #Dividir cada individuo em 3 partes
    #Parte central de cada individuo copiada para novos individuos
    #Copiar restante informação não repetida do anterior individuo para o novo, começando pela terceira parte
    #Adicionar novos individuos num array
    #retornar array

    #The parameters represents two individuals from the population
    #Will return 2 individuals
    #Useful for Traveller
    def crossWithOrderPreservation(self, firstIndividual, secondIndividual, firstCutpoint=None, secondCutPoint=None):
        #if firstCutPoint is None:
            #firstCutPoint = random
        #if secondCutPoint is None:
            #secondCutPoint = random

        # print(firstIndividual)
        # print(secondIndividual)
        
        # #firstCenter = firstIndSplited[1]
        # #secondCenter = secondIndSplited[1]


        # firstIndividual = firstIndSplited[2] + firstIndSplited[0] + firstIndSplited[1]
        # secondIndividual = secondIndSplited[2] + secondIndSplited[0] + secondIndSplited[1]
        # print(firstIndividual)
        # print(secondIndividual)
        
        # for index in range(len(firstIndividual)):
        #     if firstIndividual[index] not in secondCenter:
        #         pass
        pass
        
        # # for individualIndex in range(len(firstIndividual)):
        
    def onePointCrossover(self,firstIndividual,secondIndividual, cutPoint=None):
        if cutPoint is None:
            cutPoint = np.random.randint(1,len(firstIndividual)-2,size=1)[0]
        aux = firstIndividual[cutPoint:]
        firstIndividual[cutPoint:] = secondIndividual[cutPoint:]
        secondIndividual[cutPoint:] = aux
        return firstIndividual,secondIndividual

    def twoPointsCrossover(self):
        pass

    def uniformCrossover(self,firstIndividual,secondIndividual):
        mask = np.random.choice([0,1],len(firstIndividual),p=[0.5 , 0.5])
        newFirstIndividual = []
        newSecondIndividual = []
        for index in range(len(firstIndividual)):
            if mask[index] == 1:
                newFirstIndividual.append(secondIndividual[index])
                newSecondIndividual.append(firstIndividual[index])
            else:
                newFirstIndividual.append(firstIndividual[index])
                newSecondIndividual.append(secondIndividual[index])
        return newFirstIndividual,newSecondIndividual