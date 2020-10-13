from amplpy import AMPL, Environment
import os
experiment_name = "zero_sum"
lecture_nr = 1

ampl = AMPL(Environment('C:\\Users\\cmata\\Desktop\\Linear Programming\\ampl.mswin64'))
ampl.read(os.path.join(os.getcwd(),'Lecture'+str(lecture_nr), experiment_name + '.mod'))
ampl.readData(os.path.join(os.getcwd(),'Lecture'+str(lecture_nr), experiment_name + '.dat'))
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