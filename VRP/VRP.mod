# set CITIES;
option solver cplex;

param N;
param K;
param C;

param c{1..N, 1..N};
param d{1..N};

var x{1..N, 1..N} >= 0, <= 1, integer;
var u{1..N-1};

minimize Distance: sum{i in 1..N, j in 1..N} c[i,j]*x[i,j];

subject to HorizontalConstraint {i in 2..N}:
    sum{j in 1..N} x[i,j] = 1
;

subject to VerticalConstraint {j in 2..N}:
    sum{i in 1..N} x[i,j] = 1
;

subject to BaseHorizontalConstraint:
    sum{j in 2..N} x[1, j] = K
;

subject to BaseVerticalConstraint:
    sum{i in 2..N} x[i, 1] = K
;

subject to UConstraint {i in 1..N-1}:
    d[i] <= u[i] <= C
;

subject to UConstraint2 {i in 2..N, j in 2..N: i!=j}:
    u[j-1] - u[i-1] + C * (1 - x[i,j]) >=  d[j-1]
;
