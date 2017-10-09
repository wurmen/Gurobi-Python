
# Controlling Air Pollution example
- 本範例為講義第三章p25.26題目
<img src="https://github.com/wurmen/Gurobi-Python/blob/master/python-gurobi%20%20model/picture/Controlling%20Air%20Pollution%20example/Controlling%20Air%20Pollution%2012.png" width="750">

# Import gurobipy


```python
from gurobipy import*
```

# Model


```python
m=Model("controlling air pollution_type2")
```

# Add parameters
**c**:每個方法的成本<br>
**p**:每個方法可以減少的量<br>
**r**:每個汙染物至少要被減少的量<br>


```python
c=[8,10,7,6,11,9]
p=[[12,9,25,20,17,13],
  [35,42,18,31,56,49],
  [37,53,28,24,29,20]]
r=[60,150,125]
```

# Add decision variables


```python
x={}
for j in range(6):
    x[j]=m.addVar(lb=0,ub=1,name="x_%d"%j)
```

# Update


```python
m.update()
```

# Add objective and constraints

<img src="https://github.com/wurmen/Gurobi-Python/blob/master/python-gurobi%20%20model/picture/Controlling%20Air%20Pollution%20example/Controlling%20Air%20Pollution%202.png" width="300">


```python
m.setObjective(quicksum(c[j]*x[j] for j in range(6)),GRB.MINIMIZE)
for i in range(3):
    m.addConstr(quicksum(p[i][j]*x[j] for j in range(6))>=r[i],"c0")
```

# Result


```python
m.optimize()
print("Obj:",m.objVal)
for v in m.getVars():
    print("%s:%.3f"%(v.varName,v.x))
```

    Optimize a model with 3 rows, 6 columns and 18 nonzeros
    Coefficient statistics:
      Matrix range     [9e+00, 6e+01]
      Objective range  [6e+00, 1e+01]
      Bounds range     [1e+00, 1e+00]
      RHS range        [6e+01, 2e+02]
    Presolve time: 0.00s
    Presolved: 3 rows, 6 columns, 18 nonzeros
    
    Iteration    Objective       Primal Inf.    Dual Inf.      Time
           0    0.0000000e+00   6.171875e+00   0.000000e+00      0s
           4    3.2154631e+01   0.000000e+00   0.000000e+00      0s
    
    Solved in 4 iterations and 0.01 seconds
    Optimal objective  3.215463133e+01
    ('Obj:', 32.154631330359486)
    x1:1.000
    x2:0.623
    x3:0.343
    x4:1.000
    x5:0.048
    x6:1.000
    


```python

```
