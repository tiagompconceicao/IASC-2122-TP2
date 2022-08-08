from optimizationAlgorithms.OptimizationAlgorithm import OptimizationAlgorithm
from problem.Problem import Problem
import numpy as np
import math

from state.State import State

class SimulatedAnnealing(OptimizationAlgorithm):
    def __init__(self):
        super().__init__()
    
    #TODO   Testar
    def plan(self,problem: Problem, schedule):
        fValues = []
        current: State = problem.getInitialState()
        t = 0
        while True:
            T = 0
            T = schedule(t)
            if round(T, 4) == 0:
                return current,t, fValues
                
            next = problem.getRandomNeighbor(current)   
            if next is None:
                return current,t,fValues

            deltaE = problem.valueFunction(next) - problem.valueFunction(current)
            if deltaE > 0:
               current = next
            else:
                #Probability to next become the current
                prob = math.exp((deltaE/T))
                result = np.random.choice(a=[True,False],p = [prob, 1 - prob])
                if result:
                    current = next 
            fValues.append(problem.valueFunction(current))        
            t += 1
