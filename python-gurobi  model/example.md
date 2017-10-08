
# Import gurobipy


```python
from gurobipy import* #導入Gurobi函式庫
```

# Model


```python
    m=Model('mip1') # 建立一個新的model，並傳至m
```

# Add decision variable


```python
    x = m.addVar(vtype=GRB.BINARY, name="x")  # m.addVar()加入變數
    y = m.addVar(vtype=GRB.BINARY, name="y")
    z = m.addVar(vtype=GRB.BINARY, name="z")
```

# Update


```python
m.update() #更新此model
```

# Add objective and constraints


```python
    # m.setObjective()設置目標函數
    m.setObjective(x + y + 2 * z, GRB.MAXIMIZE) 

    # m.addConstr()加入限制式
    # Add constraint: x + 2 y + 3 z <= 4
    m.addConstr(x + 2 * y + 3 * z <= 4, "c0") 

    # Add constraint: x + y >= 1
    m.addConstr(x + y >= 1, "c1")
```




    <gurobi.Constr *Awaiting Model Update*>



# Result


```python
    m.optimize() # m.optimize()求解
    
    # 透過屬性varName、x顯示決策變數名字及值
    for v in m.getVars():
        print('%s %g' % (v.varName, v.x))
    # 透過屬性objVal顯示最佳解
    print('Obj: %g' % m.objVal)
```

    Optimize a model with 2 rows, 3 columns and 5 nonzeros
    Variable types: 0 continuous, 3 integer (3 binary)
    Coefficient statistics:
      Matrix range     [1e+00, 3e+00]
      Objective range  [1e+00, 2e+00]
      Bounds range     [1e+00, 1e+00]
      RHS range        [1e+00, 4e+00]
    Found heuristic solution: objective 2
    Presolve removed 2 rows and 3 columns
    Presolve time: 0.06s
    Presolve: All rows and columns removed
    
    Explored 0 nodes (0 simplex iterations) in 0.23 seconds
    Thread count was 1 (of 4 available processors)
    
    Solution count 2: 3 2 
    
    Optimal solution found (tolerance 1.00e-04)
    Best objective 3.000000000000e+00, best bound 3.000000000000e+00, gap 0.0000%
    x 1
    y 0
    z 1
    Obj: 3
    
