# Netflow problem
*POLab*
<br>
*2017/11/02*
<br>
[【回到首頁】](https://github.com/PO-LAB/Python-Gurobi) <br>
##### ※參考資料: https://wenku.baidu.com/view/b34a6a8f680203d8ce2f24b1?pcf=2#8 、[Gurobi-Python Interface](https://www.gurobi.com/documentation/6.5/quickstart_windows/py_python_interface.html#section:Python)

## (一)問題描述
### ● 題目:
有兩項產品(**鉛筆及鋼筆**)，分別由兩個城市生產(**底特律及丹佛**)，並送至其他三個城市(**波士頓、紐約及西雅圖**)，且必須滿足這三個
城市所需商品數量，每項商品運輸過程中不得超過每條路徑所能負荷的運能。

### ● 已知:
如下圖所示<br>
每條路徑都有相對應的運輸成本及運能，分別表示為:
- (capacity , pencils transportation cost , pens transportation cost)<br>

每個城市所擁有或所需要的商品數量:
- (pencils inflow , pens inflows)
<div align=center>
<img src="https://github.com/wurmen/Gurobi-Python/blob/master/python-gurobi%20%20model/picture/Netflow%20problem/netflow%20problem%20picture.PNG"  width="614" height="356"/>
</div>

### ● 目標:
- 最小化總運輸成本
### ● 限制:
- 每條路徑不得超過所能負荷的運能
- 必須滿足波士頓、紐約及西雅圖所需的商品數量

## (二)數學模型

### ● 符號設定
- arcs:所有可能的運輸路線<br>

- nodes:所有運輸路線上的城市<br>

- commodities:所有等待運輸的產品<br>

### ● 參數設定
- cost[h,i,j]:商品h從城市i到城市j的運輸成本<br>

- capacity[i,j]:從城市i到城市j 的運能<br>

- inflow[h,j]:商品h在城市j的生產量或需求量<br>

### ● 決策變數
- flow[h,i,j]:商品h從城市i到城市j的運輸總量






