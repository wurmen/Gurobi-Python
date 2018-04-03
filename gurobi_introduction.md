# Gurobi 簡介 (cont.)

[Gurobi](http://www.gurobi.com/index)，又稱Gurobi Optimizer，是一個用來求解數學規劃的優化引擎，為目前市面上相當知名的數學規劃優化器，主要由[Zonghao **Gu**、Edward  **Ro**thberg、Robert **Bi**xby](http://www.gurobi.com/company/management-team)開發，Gurobi即由三位開發者的名子命名而來。
###### ※以下內容相關連結會以:link:或藍色字體表示，可自行點擊查看
-------
### :black_nib: 支持的數學規劃類型 [:link:](http://www.gurobi.com/products/features-benefits)
目前Gurobi已經更新至7.5.2版本，並且能求解以下類型的數學規劃問題：
<br>

- Linear Programming (LP)
- Mixed-Integer Linear Programming (MILP)
- Quadratic Programming (QP)
- Mixed-Integer Quadratic Programming (MIQP)
- Quadratically Constrained Programming (QCP)
- Mixed-Integer Quadratically Constrained Programming (MIQCP)

:zap: 因此Gurobi是能夠求解非線性問題，但僅限於二次規劃問題。

------------
### :black_nib: 支持的程式語言(programming language)及建模語言(modeling language) [:link:](http://www.gurobi.com/products/features-benefits)
Gurobi支援許多不同程式語言及建模語言的開發，如以下所示：

:arrow_down_small: 程式語言
- 物件導向(Object-oriented interfaces)：C++, Java, .NET, and Python
- 矩陣導向(Matrix-oriented interfaces)：C, MATLAB, and R

:arrow_down_small: 建模語言
- AMPL, GAMS, AIMMS, and MPL

:zap: 本repository主要著重於python-gurobi的應用


----------
### :black_nib: License
要使用Gurobi，必須先取得[Gurobi License](http://www.gurobi.com/downloads/licenses/license-center)才能進行使用，Gurobi License主要分為兩個類型，[商業使用(Commercial Licenses)](http://www.gurobi.com/products/licensing-pricing/licensing-overview)及[學術使用(Academic Licenses)](http://www.gurobi.com/academia/academia-center)，商業使用是必須付費的，不過Gurobi有提供測試License，讓公司進行Gurobi試用，而學術使用是完全免費的，並且在Gurobi使用上沒有任何限制，不管是在建模的大小或功能的使用等，但學術License僅有一年的有效期，一旦到期了，就必須再重新申請新的License才可再次使用，不過以整體來說Gurobi算是非常好的數學規劃求解器，對於學術上的使用是非常大方的。
