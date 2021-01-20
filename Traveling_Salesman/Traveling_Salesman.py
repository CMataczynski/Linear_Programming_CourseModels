from amplpy import AMPL, Environment
import os
import sys
sys.path.append(os.getcwd())
from env_path import ENV_PATH

experiment_name = "Traveling_Salesman"

ampl = AMPL(Environment(ENV_PATH))
ampl.read(os.path.join(os.getcwd(),experiment_name, experiment_name + '.mod'))
ampl.readData(os.path.join(os.getcwd(),experiment_name, experiment_name + '.dat'))
ampl.solve()


distance = ampl.getObjective('Distance')
print("Difference in objectives is:", distance.value())
u = ampl.getVariable('u')
u = u.getValues()
print(u)