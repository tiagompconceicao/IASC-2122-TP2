from numpy.lib.financial import fv
from optimizationAlgorithms.OptimizationAlgorithm import OptimizationAlgorithm
from problem.Problem import Problem
import numpy as np
from state.State import State


class StochasticHillClimbing(OptimizationAlgorithm):
    def __init__(self):
        super().__init__()

    def plan(self,problem:Problem):
        current: State = problem.getInitialState()
        iterations = 0
        fValues = []
        while True:
            neighbors = problem.getNeighbors(current)
            betterNeighbors = []

            #Get a random neighbor with better value function
            for neighbor in neighbors:
                if problem.valueFunction(neighbor) > problem.valueFunction(current):
                    betterNeighbors.append(neighbor)

            #If there are not better neighbors, return current
            if len(betterNeighbors) == 0:
                return current,iterations,fValues

            #Otherwise, a random better neighbors becomes the current state
            current = np.random.choice(betterNeighbors,1)[0]
            fValues.append(problem.valueFunction(current))
            iterations += 1 

        