from amplpy import AMPL, Environment
import os
import sys
sys.path.append(os.getcwd())
from env_path import ENV_PATH

ampl = AMPL(Environment(ENV_PATH))
experiment_name = "cutting_stock"
ampl.read(os.path.join(os.getcwd(),experiment_name, experiment_name+'.mod'))
ampl.readData(os.path.join(os.getcwd(),experiment_name, experiment_name+'.dat'))

ampl.solve()
totalcost = ampl.getObjective('Total_cost')
print("Objective is:", totalcost.value())
buy = ampl.getVariable('Buy')
df = buy.getValues()
print(df)