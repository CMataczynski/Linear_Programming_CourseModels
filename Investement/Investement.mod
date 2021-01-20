set INVESTEMENTS;
param G1;
param p;
param K;
param bounds{1..K};
param Q {1..K, INVESTEMENTS};

var x {INVESTEMENTS} >= 0, <= G1;
var y {i in 0..K-1} >= 0;

maximize Total_gain: sum{j in INVESTEMENTS} Q[K,j] * x[j] + (1 + p) * y[K-1];

subject to First_year: y[0] = 0;

subject to Summary{j in 1..K-1}: 
    -1 * sum {i in INVESTEMENTS} Q[j,i]*x[i] + y[j] - (1+p)*y[j-1] =  bounds[j];
