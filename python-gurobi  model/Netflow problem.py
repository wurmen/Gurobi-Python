
# coding: utf-8

# ## (三)Python+Gurobi

# ## Import gurobipy

# In[1]:

from gurobipy import *


# ## Add parameters

# - 定義兩種商品，以及包含五個節點六條路徑的網絡結構，形成commodities與nodes兩個列表
# - 利用multidict函數初始化arcs與capacity，將arcs轉入tuplelist
# 
# 
# 

# In[2]:

commodities = ['Pencils', 'Pens']
nodes = ['Detroit', 'Denver', 'Boston', 'New York', 'Seattle']

arcs, capacity = multidict({
  ('Detroit', 'Boston'):   100,
  ('Detroit', 'New York'):  80,
  ('Detroit', 'Seattle'):  120,
  ('Denver',  'Boston'):   120,
  ('Denver',  'New York'): 120,
  ('Denver',  'Seattle'):  120 })
arcs = tuplelist(arcs)


# - 建立每個商品在每條路徑的運輸成本數據，以及每個節點的生產或需求量
# - 透過cost[h,i,j]來索引運輸成本
# - 透過inflow[h,j]來索引每個節點的生產或需求量

# In[3]:

cost = {
  ('Pencils', 'Detroit', 'Boston'):   10,
  ('Pencils', 'Detroit', 'New York'): 20,
  ('Pencils', 'Detroit', 'Seattle'):  60,
  ('Pencils', 'Denver',  'Boston'):   40,
  ('Pencils', 'Denver',  'New York'): 40,
  ('Pencils', 'Denver',  'Seattle'):  30,
  ('Pens',    'Detroit', 'Boston'):   20,
  ('Pens',    'Detroit', 'New York'): 20,
  ('Pens',    'Detroit', 'Seattle'):  80,
  ('Pens',    'Denver',  'Boston'):   60,
  ('Pens',    'Denver',  'New York'): 70,
  ('Pens',    'Denver',  'Seattle'):  30 }

inflow = {
  ('Pencils', 'Detroit'):   50,
  ('Pencils', 'Denver'):    60,
  ('Pencils', 'Boston'):   -50,
  ('Pencils', 'New York'): -50,
  ('Pencils', 'Seattle'):  -10,
  ('Pens',    'Detroit'):   60,
  ('Pens',    'Denver'):    40,
  ('Pens',    'Boston'):   -40,
  ('Pens',    'New York'): -30,
  ('Pens',    'Seattle'):  -30 }


# ## Model

# In[4]:

# Create optimization model
m = Model('netflow')


# ## Add decision variables

# - 創建字典flow來儲存決策變數
# - 透過obj參數來設定決策變數的目標係數

# In[5]:

# Create variables
flow = {}
for h in commodities:
    for i,j in arcs:
        flow[h,i,j] = m.addVar(ub=capacity[i,j], obj=cost[h,i,j],
                               name='flow_%s_%s_%s' % (h, i, j))
m.update()


# ## Update

# In[6]:

m.update()


# ## Add constraints

# - 加入運輸容量限制式
# - 加入流量守恆限制式

# In[7]:

# Arc capacity constraints
for i,j in arcs:
    m.addConstr(quicksum(flow[h,i,j] for h in commodities) <= capacity[i,j],
                'cap_%s_%s' % (i, j))

# Flow conservation constraints
for h in commodities:
    for j in nodes:
        m.addConstr(
          quicksum(flow[h,i,j] for i,j in arcs.select('*',j)) +
              inflow[h,j] ==
          quicksum(flow[h,j,k] for j,k in arcs.select(j,'*')),
                   'node_%s_%s' % (h, j))


# ## Result

# - 透過getAttr()函數取得模型m中決策變數flow的屬性值x，也就是決策變數flow的最佳解
# - getAttr()函數詳細內容可點擊[這裡](https://www.gurobi.com/documentation/7.0/refman/py_model_getattr.html)

# In[8]:

# Compute optimal solution
m.optimize()

# Print solution
if m.status == GRB.Status.OPTIMAL:
    solution = m.getAttr('x', flow)
    for h in commodities:
        print('\nOptimal flows for %s:' % h)
        for i,j in arcs:
            if solution[h,i,j] > 0:
                print('%s -> %s: %g' % (i, j, solution[h,i,j]))


# In[ ]:



