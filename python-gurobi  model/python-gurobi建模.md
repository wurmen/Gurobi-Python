# Python+Gurobi建模
-------------------
## (一)Python+Gurobi建模流程
![](https://github.com/wurmen/Gurobi-Python/blob/master/python-gurobi%20%20model/picture/Python%2Bgurobi%E5%BB%BA%E6%A8%A1%E6%B5%81%E7%A8%8B.png)

## (二)Python+Gurobi架構

### ● 在python介面中，數學式子的寫法相似於原本的式子，只是將式子都拆解開來
![](https://github.com/wurmen/Gurobi-Python/blob/master/python-gurobi%20%20model/picture/python%E6%95%B8%E5%AD%B8%E5%BC%8F%E5%AD%90.png)
### ● 在建構一個Python+Gurobi的數學模組時， 通常會依照此順序進行設定變數、目標函數、限制式等
![](https://github.com/wurmen/Gurobi-Python/blob/master/python-gurobi%20%20model/picture/Python%2Bgurobi%20%E6%9E%B6%E6%A7%8B.png)

### ● 建模時常用的for迴圈及if條件句
 Python中宣告for迴圈及if條件式後，記得用**冒號':'** 來結束聲明，接著在下一行打上要對for迴圈或if條件式做什麼事情，在此要特別注意的是python是透過**縮排**來辨別不同的程式區塊，所以當你要打包含在for迴圈及if條件句下的程式碼時，要記得按**tab鍵**來做區隔，這樣程式才知道他們是包含在for迴圈跟if條件句之下的程式碼。
<br>-**for迴圈**
```python
for i in <some list>:
 <do something for each i here>
```
-**if條件句**
```python
if <condition>:
 <do something if condition is true here>
```

### ● quicksum()相當於python的sum()函數及數學符號 ∑
Ex:
<br>![](https://github.com/wurmen/Gurobi-Python/blob/master/python-gurobi%20%20model/picture/quicksum_example.png)
<br>上述限制式在Python+Gurobi中表示為:
```python
for i in I:
 m.addConstr(quicksum(x[i,j] for j in J)<=5)
```
## (三)常用的三大函數及屬性
### 1.三大函數
在建立一個數學模式時，我們必須加入我們的決策變數、目標函式及限制式，以下是在設定這些變數及式子常用的三大函數的詳細內容介紹
<br>Ps.在Gurobi中設定目標函式及限制式還有其他不一樣的方式，在此只介紹這三個函數的應用，若想要有更進一步的了解可至Gurboi網站內的[Python](http://www.gurobi.com/documentation/7.5/refman/py_python_api_overview.html)專區查詢，若想了解其他函數的詳細資訊可點擊[這裡](http://www.gurobi.com/documentation/7.5/refman/py_python_api_details.html)
### ● 加入決策變數函數
![](https://github.com/wurmen/Gurobi-Python/blob/master/python-gurobi%20%20model/picture/m.addvar.png)
### ● 加入目標函式函數
![](https://github.com/wurmen/Gurobi-Python/blob/master/python-gurobi%20%20model/picture/m.setobjective.png)
### ● 加入限制式函數
![](https://github.com/wurmen/Gurobi-Python/blob/master/python-gurobi%20%20model/picture/m.addconstr.png)

### 2.Gurobi attributes
在Guroib中，可以透過各種屬性來查詢或更改所建立數學模組的內容，以下為常用的幾個屬性:
<br>Ps.更多屬性查詢，可點擊[這裡](https://www.gurobi.com/documentation/7.0/refman/attributes.html)
### ● Model attributes:
|Attribute Name|Description|
|-----|-----|
|**NumVars**|Number of variables|
|**NumConstrs**|Number of linear constraints|
|**ObjVal**|objective value for current solution|

### ● Variable attributes:
|Attribute Name|Description|
|-----|-----|
|**LB**|Lower bound|
|**Obj**|Linear objective coefficient|
|**VarName**|Variable name|
|**X**|Value in the current solution|

### ● Linear constraint attributes:
|Attribute Name|Description|
|-----|-----|
|**ConstrName**|Constraint name|
|**Pi**|Dual value (also known as the shadow price)|
|**Slack**|Slack in the current solution|
