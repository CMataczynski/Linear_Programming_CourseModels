# set CITIES;
option solver cplex;
param N;

param c{1..N, 1..N};

var x{1..N, 1..N} >= 0, <= 1, integer;
var u{1..N} >= 1, integer;

minimize Distance: sum{i in 1..N, j in 1..N} c[i,j]*x[i,j];

subject to HorizontalConstraint {i in 1..N}:
    sum{j in 1..N} x[i,j] = 1
;

subject to VerticalConstraint {j in 1..N}:
    sum{i in 1..N} x[i,j] = 1
;

subject to StartingPoint:
    u[1] = 1
;

subject to UConstraint {i in 2..N}:
    2 <= u[i] <= N
;

subject to UConstraint2 {i in 2..N, j in 2..N}:
    u[i] - u[j] + 1 <=  (N-1) * (1-x[i,j])
;
