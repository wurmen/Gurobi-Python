# Python+Gurobi建模

*POLab*
<br>
*2017/10/08*
<br>
[【回到首頁】](https://github.com/PO-LAB/Python-Gurobi)

## (一)最佳化流程
<img src="https://github.com/wurmen/Gurobi-Python/blob/master/python-gurobi%20%20model/picture/Python%2Bgurobi%E5%BB%BA%E6%A8%A1/%E6%9C%80%E4%BD%B3%E5%8C%96%E6%B5%81%E7%A8%8B.png" width="650">

## (二)問題產生
● 有x、y、z三個活動想在同一天舉辦<br>
● 場地總時間只有四個小時可使用<br>
● 活動z的價值為活動x及y的兩倍<br>
● 活動x與活動y至少要選一個舉辦<br>
● 活動x需花費1小時<br>
● 活動y需花費2小時<br>
● 活動z需花費3小時<br>
● 舉辦哪幾個活動可以使價值最大化?<br>

## (三)數學模式

<img src="https://github.com/wurmen/Gurobi-Python/blob/master/python-gurobi%20%20model/picture/Python%2Bgurobi%E5%BB%BA%E6%A8%A1/%E5%BB%BA%E6%A8%A1%E7%AF%84%E4%BE%8B.png" width="850">


## (四)Python+Gurobi建模求解
## 1.建模流程
<img src="https://github.com/wurmen/Gurobi-Python/blob/master/python-gurobi%20%20model/picture/Python%2Bgurobi%E5%BB%BA%E6%A8%A1%E6%B5%81%E7%A8%8B.png" width="750">

## 2.Python+Gurobi建模

<img src="https://github.com/wurmen/Gurobi-Python/blob/master/python-gurobi%20%20model/picture/Python%2Bgurobi%E5%BB%BA%E6%A8%A1/example.png" width="450">

## Import gurobipy


```python
from gurobipy import* #導入Gurobi函式庫
```

## Model


```python
m=Model('mip1') # 建立一個新的model，並傳至m
```

## Add decision variable


```python
x = m.addVar(vtype=GRB.BINARY, name="x")  # m.addVar()加入變數
y = m.addVar(vtype=GRB.BINARY, name="y")
z = m.addVar(vtype=GRB.BINARY, name="z")
```

## Update


```python
m.update() #更新此model
```

## Add objective and constraints


```python
# m.setObjective()設置目標函數
m.setObjective(x + y + 2 * z, GRB.MAXIMIZE) 

# m.addConstr()加入限制式
# Add constraint: x + 2 y + 3 z <= 4
m.addConstr(x + 2 * y + 3 * z <= 4, "c0") 

# Add constraint: x + y >= 1
m.addConstr(x + y >= 1, "c1")
```








## Result
- 如果不想要顯示求解的過程，可在optimize()之前加入此程式碼：**m.setParam('OutputFlag',0)**

```python
m.optimize() # m.optimize()求解
```
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

```
```python
# 透過屬性varName、x顯示決策變數名字及值
for v in m.getVars():
    print('%s %g' % (v.varName, v.x))
# 透過屬性objVal顯示最佳解
print('Obj: %g' % m.objVal)
```

```
x 1
y 0
z 1
Obj: 3
```
