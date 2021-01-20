from amplpy import AMPL, Environment
import os
import sys
sys.path.append(os.getcwd())
from env_path import ENV_PATH

experiment_name = "zero_sum"

ampl = AMPL(Environment(ENV_PATH))
ampl.read(os.path.join(os.getcwd(),experiment_name, experiment_name + '.mod'))
ampl.readData(os.path.join(os.getcwd(),experiment_name, experiment_name + '.dat'))
ampl.solve()


totalcost = ampl.getObjective('Max_cost')
print("Difference in objectives is:", totalcost.value())
u = ampl.getVariable('u')
u = u.getValues()
t = ampl.getVariable('t')
t = t.getValues()
print("Objectives are {}, {}".format(u, t))
x = ampl.getVariable('p')
x = x.getValues()
y = ampl.getVariable('q')
y = y.getValues()
print(x, y)