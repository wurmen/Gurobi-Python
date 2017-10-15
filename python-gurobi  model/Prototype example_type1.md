
# Prototype example


```python
from gurobipy import*
```


```python
    m=Model('Protorype example_type1')
```


```python
    x_1=m.addVar(lb=0,vtype=GRB.CONTINUOUS,name='x_1')
    x_2=m.addVar(lb=0,vtype=GRB.CONTINUOUS,name='x_2')
```


```python
    m.update()
```


```python
    m.setObjective(3*x_1+5*x_2,GRB.MAXIMIZE)
```


```python
    m.addConstr(x_1<=4,'c0')
    m.addConstr(2*x_2<=12,'c1')
    m.addConstr(3*x_1+2*x_2<=18,'c2')
```




    <gurobi.Constr *Awaiting Model Update*>




```python
    m.optimize()
```

    Optimize a model with 3 rows, 2 columns and 4 nonzeros
    Coefficient statistics:
      Matrix range     [1e+00, 3e+00]
      Objective range  [3e+00, 5e+00]
      Bounds range     [0e+00, 0e+00]
      RHS range        [4e+00, 2e+01]
    Presolve removed 2 rows and 0 columns
    Presolve time: 0.02s
    Presolved: 1 rows, 2 columns, 2 nonzeros
    
    Iteration    Objective       Primal Inf.    Dual Inf.      Time
           0    4.5000000e+01   1.500000e+00   0.000000e+00      0s
           1    3.6000000e+01   0.000000e+00   0.000000e+00      0s
    
    Solved in 1 iterations and 0.03 seconds
    Optimal objective  3.600000000e+01
    


```python
    print('obj:%d'%m.objVal)
    for v in m.getVars():
        print('%s:%d'%(v.varName,v.x))
```

    obj:36
    x_1:2
    x_2:6
    


```python

```
