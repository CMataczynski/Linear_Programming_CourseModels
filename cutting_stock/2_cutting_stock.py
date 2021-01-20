from amplpy import AMPL, Environment
import os

ampl = AMPL(Environment('C:\\Users\\cmata\\Desktop\\Linear Programming\\ampl.mswin64'))
experiment_name = "cutting_stock"
ampl.read(os.path.join(os.getcwd(),experiment_name, experiment_name+'.mod'))
ampl.readData(os.path.join(os.getcwd(),experiment_name, experiment_name+'.dat'))

ampl.solve()
totalcost = ampl.getObjective('Total_cost')
print("Objective is:", totalcost.value())
buy = ampl.getVariable('Buy')
df = buy.getValues()
print(df)