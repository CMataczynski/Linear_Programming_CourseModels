set BETH;
set ANN;

param reward{BETH, ANN};

var p {ANN} >= 0;
var q {BETH} >= 0;
var u;
var t;

minimize Max_cost: u - t;

subject to UConstraint {i in ANN}:
   u >= sum {j in BETH} q[j] * reward[j, i];

subject to TConstraint {j in BETH}:
   t <= sum {i in ANN} p[i] * reward[j, i];


subject to ProbabilityConstraintAnn:
    sum{j in ANN} p[j] = 1;

subject to ProbabilityConstraintBeth:
    sum{j in BETH} q[j] = 1;


# var M;
# minimize Max_Cost: M;
# subject to M_def {i in PEOPLE}:
# M >= sum {j in PROJECTS} cost[i,j] * Assign[i,j];