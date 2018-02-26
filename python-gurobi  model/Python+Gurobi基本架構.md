# Python+Gurobi基本架構

*POLab*
<br>
*2017/09/27*
<br>
[【回到首頁】](https://github.com/PO-LAB/Python-Gurobi)


## (一)Python+Gurobi架構 
### ● 在Python介面中，數學式子的寫法相似於原本的式子，只是將式子都拆解開來
<img src="https://github.com/wurmen/Gurobi-Python/blob/master/python-gurobi%20%20model/picture/python%E6%95%B8%E5%AD%B8%E5%BC%8F%E5%AD%90.png" width="550">

### ● 在利用Python+Gurobi建構一個數學規劃時， 通常會依照此順序進行設定變數、目標函數、限制式等
<img src="https://github.com/wurmen/Gurobi-Python/blob/master/python-gurobi%20%20model/picture/Python%2Bgurobi%20%E6%9E%B6%E6%A7%8B.png" width="650">

### ● 建模時常用的for迴圈及if條件句
 Python中宣告for迴圈及if條件式後，記得用**冒號':'** 來結束聲明，接著在下一行打上要對for迴圈或if條件式做的事情，在此要特別注意的是Python是透過**縮排**來辨別不同的程式區塊，因此在下一行開始前，要記得按**tab鍵**來做區隔，這樣程式才知道他們是包含在for迴圈跟if條件句之下的程式碼。

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

### ● quicksum()相當於Python的sum()函數及數學符號 ∑
#### e.g.
<br> <img src="https://github.com/wurmen/Gurobi-Python/blob/master/python-gurobi%20%20model/picture/quicksum_example.png" width="200">
<br>上述限制式在Python+Gurobi中表示為:
```python
for i in I:
    m.addConstr(quicksum(x[i,j] for j in J)<=5)
```

### ● Python字符串格式化

在建立數學規劃的最後，通常需顯示最終求得之最佳解，例如:目標函數值、各決策變數值等...<br>
此時，可藉由格式符來替我們列印各項數值及名稱，以下為幾個常用的格式符:
#### ※如果對格式化字符串的使用較不熟悉，可參考[這裡](http://gohom.win/2015/09/13/PyStringFormat/)
|符號|說明|
|-----|-----|
|%s|字符串|
|%d|格式化整數|
|%f|格式化浮點數|
|%e|指數，科學計數法|
|%g|根據值的大小決定使用%f或%e|
#### e.g.
```python
print('She is %s. She weights %gkg and is %dcm tall.'%('Rima',50.4,166))
```
    She is Rima. She weights 50.4kg and is 166cm tall.

```python
print('obj:%d'%m.objVal)
```
```
obj:36
```
## (二)常用的三大函數及屬性
### 1.三大函數
在建立一個數學規劃時，我們必須加入我們的決策變數、目標函數及限制式，以下是在設定這些變數及式子常用的三大函數的詳細內容介紹
<br>P.S. 在Gurobi中設定目標函數及限制式還有其他不一樣的方式，在此只介紹這三個函數的應用，若想要有更進一步的了解可至Gurboi網站內的[Python](http://www.gurobi.com/documentation/7.5/refman/py_python_api_overview.html)專區查詢，若想了解其他函數的詳細資訊可點擊[這裡](http://www.gurobi.com/documentation/7.5/refman/py_python_api_details.html)
### ● 決策變數函數

 變數預設的範圍上限為無限，下限為0，變數型態為連續變數(continuous)<br>
 
<img src="https://github.com/wurmen/Gurobi-Python/blob/master/python-gurobi%20%20model/picture/m.addvar.png" width="700"><br>

### ● 目標函數
<img src="https://github.com/wurmen/Gurobi-Python/blob/master/python-gurobi%20%20model/picture/m.setobjective.png" width="700"><br>

### ● 限制式函數
<img src="https://github.com/wurmen/Gurobi-Python/blob/master/python-gurobi%20%20model/picture/m.addconstr.png" width="700">


### 2.Gurobi attributes
在Guroib中，可以透過各種屬性來查詢或更改所建立數學規劃的內容，以下為常用的幾個屬性:
<br>P.S. 更多屬性查詢，可點擊[這裡](https://www.gurobi.com/documentation/7.0/refman/attributes.html)
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
