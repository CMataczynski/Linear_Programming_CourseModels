set NUTR;
set FOOD;

param cost {FOOD} > 0;
param min_req {NUTR} >= 0;
param amt {NUTR, FOOD} >= 0;

var Buy{j in FOOD} >= 0;

minimize Total_cost: sum{j in FOOD} cost[j] * Buy[j];

subject to Diet{i in NUTR}:
    min_req[i] <= sum {j in FOOD} amt[i,j] * Buy[j];