from amplpy import AMPL, Environment
import os
import sys
sys.path.append(os.getcwd())
from env_path import ENV_PATH

experiment_name = "Investement"

ampl = AMPL(Environment(ENV_PATH))
ampl.read(os.path.join(os.getcwd(),experiment_name, experiment_name + '.mod'))
ampl.readData(os.path.join(os.getcwd(),experiment_name, experiment_name + '.dat'))
ampl.solve()


totalcost = ampl.getObjective('Total_gain')
print("Objective is:", totalcost.value())
x = ampl.getVariable('x')
x = x.getValues()
y = ampl.getVariable('y')
y = y.getValues()
print(x, y)