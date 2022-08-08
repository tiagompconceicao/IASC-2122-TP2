from optimizationAlgorithms.OptimizationAlgorithm import OptimizationAlgorithm
from problem.Problem import Problem
from state.State import State
import numpy as np

class StochasticHillClimbingUSucessor(OptimizationAlgorithm):
    def __init__(self):
        pass

    # def plan(self,problem:Problem):
    #     current: State = problem.getInitialState()
    #     iterations = 1
    #     while True:
    #         neighbors = problem.getNeighbors(current)

    #         #For-loop with n loops, where n is the number of neighbors generated
    #         #Get a random neighbor
    #         #Compare with current and decide which one is better with better value function
    #         for neighbor in range(len(neighbors)):
    #             randomNeighbor = np.random.choice(neighbors,1)[0]
    #             if problem.valueFunction(randomNeighbor) > problem.valueFunction(current):
    #                 current = randomNeighbor
    #                 break
    #             neighbors.pop(neighbors.index(randomNeighbor))
            
    #         #If the current state isn't the randomNeighbor that means that none of the neighbors has a better value function that the current
    #         if randomNeighbor != current:
    #             return current,iterations
                
    #         iterations += 1 

    def plan(self,problem:Problem):
        current: State = problem.getInitialState()
        iterations = 0
        fValues = []
        while True:
            
            #Get a random neighbor from the current state
            #Will never return the same neighbor twice
            randomNeighbor = problem.getRandomNeighbor(current)

            #If the random neighbor is None that meas that there no more neighbors available for the current state
            if randomNeighbor is None:
                return current,iterations,fValues

            
            if problem.valueFunction(randomNeighbor) > problem.valueFunction(current):
                current = randomNeighbor


            fValues.append(problem.valueFunction(current))                
            iterations += 1 