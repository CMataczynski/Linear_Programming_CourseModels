from amplpy import AMPL, Environment
import os

ampl = AMPL(Environment('C:\\Users\\cmata\\Desktop\\Linear Programming\\ampl.mswin64'))

ampl.read(os.path.join(os.getcwd(),'Lecture1', 'diet.mod'))
ampl.readData(os.path.join(os.getcwd(),'Lecture1', 'diet.dat'))

ampl.solve()
totalcost = ampl.getObjective('Total_cost')
print("Objective is:", totalcost.value())
buy = ampl.getVariable('Buy')
df = buy.getValues()
print(df)