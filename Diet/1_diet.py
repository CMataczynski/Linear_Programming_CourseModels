from amplpy import AMPL, Environment
import os
import sys
sys.path.append(os.getcwd())
from env_path import ENV_PATH


ampl = AMPL(Environment(ENV_PATH))

ampl.read(os.path.join(os.getcwd(),'Diet', 'diet.mod'))
ampl.readData(os.path.join(os.getcwd(),'Diet', 'diet.dat'))

ampl.solve()
totalcost = ampl.getObjective('Total_cost')
print("Objective is:", totalcost.value())
buy = ampl.getVariable('Buy')
df = buy.getValues()
print(df)