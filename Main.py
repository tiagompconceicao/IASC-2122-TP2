from matplotlib.pyplot import draw
from optimizationAlgorithms.SimulatedAnnealing import SimulatedAnnealing
from optimizationAlgorithms.StochasticHillClimbing import StochasticHillClimbing
from optimizationAlgorithms.StochasticHillClimbingWithUniqueSucessor import StochasticHillClimbingUSucessor
from problem.QueensProblem import QueenProblem
from problem.TravellerProblem import TravellerProblem
from state.QueensState import QueensState
from state.TravellerState import TravellerState
from view.QueensView import QueensView
from view.TravellerView import TravellerView
import math
import numpy as np

def schedule(t):
    return math.exp((-t/30)+2)

state = TravellerState(15)
problem = TravellerProblem(state)
view = TravellerView()
hill = StochasticHillClimbing()
hill2 = StochasticHillClimbingUSucessor()
annealing = SimulatedAnnealing()
solution,numOfIterations,values = hill.plan(problem)
solution2,numOfIterations2,values2 = hill2.plan(problem)
solution3, numOfIterations3,values3 = annealing.plan(problem,schedule)

v1 = problem.valueFunction(solution)
v2 = problem.valueFunction(solution2)
v3 = problem.valueFunction(solution3)

print("FIRST")
print(v1)
print(numOfIterations)
print("SECOND")
print(v2)
print(numOfIterations2)
print("THIRD")
print(v3)
print(numOfIterations3)

view.draw(solution2.config)