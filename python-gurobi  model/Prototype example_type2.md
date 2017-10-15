
# Prototype example


```python
from gurobipy import*
```


```python
    m=Model('Protorype example_type2')
```


```python
    v=[3,5]
    p=[[1,0],[0,2],[3,2]]
    a=[4,12,18]
```


```python
    x={}
    for i in range(2):
        x[i]=m.addVar(lb=0,vtype=GRB.CONTINUOUS,name='x_%d'%i)
```


```python
    m.update()
```


```python
    m.setObjective(quicksum(v[i]*x[i] for i in range(2)),GRB.MAXIMIZE)
```


```python
    for j in range(3):
        m.addConstr(quicksum(p[j][i]*x[i] for i in range(2))<=a[j],name='c0')
```


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
    x_0:2
    x_1:6
    


```python

```
