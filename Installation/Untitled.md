

```python
from gurobipy import*
```


```python
try:
```


      File "<ipython-input-6-b9ba6b887214>", line 1
        try:
            ^
    SyntaxError: unexpected EOF while parsing
    



```python
    m=Model("mip1")
```


```python
except GurobiError:
    print(''Encountered a Gurobi error'')
    
```
