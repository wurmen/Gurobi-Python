# Controlling Air Pollution example
- 本範例為講義第三章p25.26題目

# Import gurobipy


```python
from gurobipy import*
```

# Model


```python
m=Model("controlling air pullution")
```

# Add decision variable


```python
x1=m.addVar(lb=0,ub=1,name="x1")
x2=m.addVar(lb=0,ub=1,name="x2")
x3=m.addVar(lb=0,ub=1,name="x3")
x4=m.addVar(lb=0,ub=1,name="x4")
x5=m.addVar(lb=0,ub=1,name="x5")
x6=m.addVar(lb=0,ub=1,name="x6")
```

# Update


```python
m.update()
```

# Add objective and constraints


```python
m.setObjective(8*x1+10*x2+7*x3+6*x4+11*x5+9*x6,GRB.MINIMIZE)

m.addConstr(12*x1+9*x2+25*x3+20*x4+17*x5+13*x6>=60,"c0")
m.addConstr(35*x1+42*x2+18*x3+31*x4+56*x5+49*x6>=150,"c1")
m.addConstr(37*x1+53*x2+28*x3+24*x4+29*x5+20*x6>=125,"c2")
```




    <gurobi.Constr *Awaiting Model Update*>



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
