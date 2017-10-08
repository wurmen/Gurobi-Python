# Python+Gurobi建模
-------------------

## (一)最佳化流程
<img src="https://github.com/wurmen/Gurobi-Python/blob/master/python-gurobi%20%20model/picture/Python%2Bgurobi%E5%BB%BA%E6%A8%A1/%E6%9C%80%E4%BD%B3%E5%8C%96%E6%B5%81%E7%A8%8B.png" width="650">

## (二)問題產生
●有x、y、z三個活動想在同一天舉辦<br>
●場地總時間只有四個小時可使用<br>
●活動3的價值為活動x及y的兩倍<br>
●活動x與活動y至少要選一個舉辦<br>
●活動x需花費1小時<br>
●活動y需花費2小時<br>
●活動z需花費3小時<br>
●舉辦哪幾個活動可以使價值最大化?<br>

## (三)數學模式

<img src="https://github.com/wurmen/Gurobi-Python/blob/master/python-gurobi%20%20model/picture/Python%2Bgurobi%E5%BB%BA%E6%A8%A1/%E5%BB%BA%E6%A8%A1%E7%AF%84%E4%BE%8B.png" width="850">


## (四)Python+Gurobi建模求解
### 1.建模流程
<img src="https://github.com/wurmen/Gurobi-Python/blob/master/python-gurobi%20%20model/picture/Python%2Bgurobi%E5%BB%BA%E6%A8%A1%E6%B5%81%E7%A8%8B.png" width="750">
