
# Generating an Optimal Employee Work Schedule Using Integer Linear Programming
*POLab*
<br>
*2017/09/27*
<br>
[【回到首頁】](https://github.com/PO-LAB/Python-Gurobi) <br>
##### ※參考資料: https://blogs.mathworks.com/loren/2016/01/06/generating-an-optimal-employee-work-schedule-using-integer-linear-programming/

## (一) 問題描述

### ● 題目:
- 利用整數線性規劃、最佳化員工工作班表。

### ● 已知:
如圖一、二所示:
- 所有員工可得的工作時間及每小時薪資。
- 每個員工每班最少所需工作時數及最多可工作時數。
- 每小時最低需求人數。

<div align=center>
<img src="https://github.com/wurmen/Gurobi-Python/blob/master/python-gurobi%20%20model/picture/Optimal%20Employee%20Work%20Schedule/%E5%93%A1%E5%B7%A5%E8%B3%87%E8%A8%8A.PNG" alt="GitHub" width="450" >
</div>

### ● 目標:
- 最小化每日需支付給員工的薪水。

### ● 限制:
- 需滿足每小時所需人數的最低需求。
- 每位員工每天只能工作一個班次
- 員工只能在他們可得的時間上班。
- 如果該員工需上班，則他必須滿足他最少所需上班的時數且不得大於他最多能上班時數

## (二) 數學模型

### ● 符號設定
D:員工人數(d=1,...,|D|) <br>

I:總時間(i,j,c=1,...,|I|)

### ● 參數設定

### ● 決策變數

### ● 目標函數

### ● 限制式

## (三) Python+Gurobi

## Import gurobipy


```python
from gurobipy import*
```

## Model


```python
    m=Model("work_schedule")
```

## Add parameters


```python
    #設定每位員工資訊 
    employee,min,max,cost,avs,ave=multidict({
            ("SMITH"):[6,8,30,6,20],("JOHNSON"):[6,8,50,0,24],('WILLIAMS'):[6,8,30,0,24],
            ('JONES'):[6,8,30,0,24],('BROWN'):[6,8,40,0,24],('DAVIS'):[6,8,50,0,24],
            ('MILLER'):[6,8,45,6,18],('WILSON'):[6,8,30,0,24],('MOORE'):[6,8,35,0,24],
            ('TAYLOR'):[6,8,40,0,24],('ANDERSON'):[2,3,60,0,6],('THOMAS'):[2,4,40,0,24],
            ('JACKSON'):[2,4,60,8,16],('WHITE'):[2,6,55,0,24],('HARRIS'):[2,6,45,0,24],
            ('MARTIN'):[2,3,40,0,24],('THOMPSON'):[2,5,50,12,24],('GARCIA'):[2,4,50,0,24],
            ('MARTINEZ'):[2,4,40,0,24],('ROBINSON'):[2,5,50,0,24]})

    #每個時段所需要的員工數
    required=[1,1,2,3,6,6,7,8,9,8,8,8,7,6,6,5,5,4,4,3,2,2,2,2]
    #總時間為24小時
    t=24
```

## Add decision variables


```python
    x={}
    staffNumber={}
    for d in employee:
        for i in range(t):
            for j in range(i+1,t+1):
                x[d,i,j]=m.addVar(vtype=GRB.BINARY,name="x_%s_%d_%d"%(d,i,j))
    for c in range(t):
        staffNumber[c]=m.addVar(vtype=GRB.INTEGER,lb=required[c],name='staffNumber_%d'%c)

```

## Add objective and constraints


```python
    m.setObjective(quicksum(quicksum(quicksum((j-i)*x[d,i,j]*cost[d] for j in range(i+1,t+1))for i in range(t))for d in employee),GRB.MINIMIZE)
    
    for d in employee:
        m.addConstr(quicksum(quicksum(x[d,i,j] for j in range(i+1,ave[d]+1)if min[d] <= (j-i) <= max[d])for i in range(avs[d],ave[d]))<=1)
        m.addConstr(quicksum(quicksum(x[d,i,j] for j in range(i+1,t+1))for i in range(t))<=quicksum(quicksum(x[d,i,j] for j in range(i+1,ave[d]+1)
        if min[d] <= (j-i) <= max[d])for i in range(avs[d],ave[d])))
    for c in range(t):
        m.addConstr(quicksum(quicksum(quicksum(x[d,i,j] for j in range(i+1,t+1)if i <= c <j) for i in range(t))for d in employee)==staffNumber[c])
    D101=quicksum(quicksum(x['ANDERSON',i,j] for j in range(i+1,7)if min["ANDERSON"]<=(j-i)<=max["ANDERSON"])for i in range(0,7))
    D102=quicksum(quicksum(x['ANDERSON',i,j] for j in range(i+1,21))for i in range(18,21))
    m.addConstr(D101+D102<=1,"F")
    m.addConstr(quicksum(quicksum(x['ANDERSON',i,j] for j in range(i+1,t+1))for i in range(t))<=D101+D102)

```




    <gurobi.Constr *Awaiting Model Update*>



## Result


```python
    m.optimize()
    m.write("nursing_type1-2.lp")
    
    print ("Optimal objective value is %g"%m.objVal)
    if m.status == GRB.Status.OPTIMAL:
        ##透過X屬性取得決策變數x的值，並列印出每個人的上班情形
        solution = m.getAttr('x', x)
        for d in employee :
            for i in range(t):
                for j in range(i+1,t+1):
                    if solution[d,i,j] == 1:
                        print("The working time of %s is from %g to %g" % (d,i,j))
        #透過X屬性取得決策變數staffNumber的值，也就是每時段的上班人數
        staffNumber_sol=m.getAttr('x',staffNumber)
        for c in range(t):
            print 'The number of staff from %d -%d: %d'%(c,c+1,staffNumber_sol[c])

```

    Optimize a model with 66 rows, 6024 columns and 58324 nonzeros
    Variable types: 0 continuous, 6024 integer (6000 binary)
    Coefficient statistics:
      Matrix range     [1e+00, 1e+00]
      Objective range  [3e+01, 1e+03]
      Bounds range     [1e+00, 9e+00]
      RHS range        [1e+00, 1e+00]
    Presolve removed 24 rows and 5050 columns
    Presolve time: 0.02s
    Presolved: 42 rows, 974 columns, 5659 nonzeros
    Variable types: 0 continuous, 974 integer (974 binary)
    
    Root relaxation: objective 4.670000e+03, 290 iterations, 0.01 seconds
    
        Nodes    |    Current Node    |     Objective Bounds      |     Work
     Expl Unexpl |  Obj  Depth IntInf | Incumbent    BestBd   Gap | It/Node Time
    
    *    0     0               0    4670.0000000 4670.00000  0.00%     -    0s
    
    Explored 0 nodes (290 simplex iterations) in 0.07 seconds
    Thread count was 8 (of 8 available processors)
    
    Solution count 1: 4670 
    Pool objective bound 4670
    
    Optimal solution found (tolerance 1.00e-04)
    Best objective 4.670000000000e+03, best bound 4.670000000000e+03, gap 0.0000%
    Optimal objective value is 4670
    The working time of JONES is from 2 to 10
    The working time of THOMAS is from 4 to 8
    The working time of TAYLOR is from 6 to 14
    The working time of JOHNSON is from 0 to 8
    The working time of MILLER is from 8 to 16
    The working time of SMITH is from 12 to 20
    The working time of MARTINEZ is from 10 to 14
    The working time of HARRIS is from 7 to 13
    The working time of DAVIS is from 16 to 24
    The working time of WHITE is from 8 to 12
    The working time of ROBINSON is from 4 to 9
    The working time of BROWN is from 8 to 16
    The working time of WILSON is from 4 to 12
    The working time of MOORE is from 16 to 24
    The working time of GARCIA is from 3 to 7
    The working time of MARTIN is from 14 to 17
    The working time of THOMPSON is from 14 to 19
    The working time of WILLIAMS is from 7 to 15
    The number of staff from 0 -1: 1
    The number of staff from 1 -2: 1
    The number of staff from 2 -3: 2
    The number of staff from 3 -4: 3
    The number of staff from 4 -5: 6
    The number of staff from 5 -6: 6
    The number of staff from 6 -7: 7
    The number of staff from 7 -8: 8
    The number of staff from 8 -9: 9
    The number of staff from 9 -10: 8
    The number of staff from 10 -11: 8
    The number of staff from 11 -12: 8
    The number of staff from 12 -13: 7
    The number of staff from 13 -14: 6
    The number of staff from 14 -15: 6
    The number of staff from 15 -16: 5
    The number of staff from 16 -17: 5
    The number of staff from 17 -18: 4
    The number of staff from 18 -19: 4
    The number of staff from 19 -20: 3
    The number of staff from 20 -21: 2
    The number of staff from 21 -22: 2
    The number of staff from 22 -23: 2
    The number of staff from 23 -24: 2
    
