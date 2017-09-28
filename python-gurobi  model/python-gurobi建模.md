# Python+Gurobi建模
-------------------
## (一)Python+Gurobi建模流程
![](https://github.com/wurmen/Gurobi-Python/blob/master/python-gurobi%20%20model/picture/Python%2Bgurobi%E5%BB%BA%E6%A8%A1%E6%B5%81%E7%A8%8B.png)

## (二)Python+Gurobi架構

### ● 在python介面中，數學式子的寫法相似於原本的式子
![](https://github.com/wurmen/Gurobi-Python/blob/master/python-gurobi%20%20model/picture/python%E6%95%B8%E5%AD%B8%E5%BC%8F%E5%AD%90.png)
### ● 在建構一個Python+Gurobi的數學模組時， 通常會依照此順序進行設定變數、目標函數、限制式等
![](https://github.com/wurmen/Gurobi-Python/blob/master/python-gurobi%20%20model/picture/Python%2Bgurobi%20%E6%9E%B6%E6%A7%8B.png)

### ● 建模時常用的for迴圈及if條件句
Python中宣告for迴圈及if條件式後，記得用**冒號:** 來結束聲明，接著在下一行打上要對for迴圈或if條件式做什麼事情，在此要特別注意的是
python是透過**縮排** 來辨別不同的程式區塊，所以當你要打包含在for迴圈及if條件句下的程式碼時，要記得按tab鍵，來做區隔，這樣程式才知道他們是包含在for迴圈跟if條件句之下的程式碼。
```python
for i in <some list>:
 <do something for each i here>
```
```python
if <condition>:
 <do something if condition is true here>
```
