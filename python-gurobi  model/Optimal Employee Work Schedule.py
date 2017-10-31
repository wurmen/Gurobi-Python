from gurobipy import*

    employee,min,max,cost,avs,ave=multidict({
            ("SMITH"):[6,8,30,6,20],("JOHNSON"):[6,8,50,0,24],('WILLIAMS'):[6,8,30,0,24],
            ('JONES'):[6,8,30,0,24],('BROWN'):[6,8,40,0,24],('DAVIS'):[6,8,50,0,24],
            ('MILLER'):[6,8,45,6,18],('WILSON'):[6,8,30,0,24],('MOORE'):[6,8,35,0,24],
            ('TAYLOR'):[6,8,40,0,24],('ANDERSON'):[2,3,60,0,6],('THOMAS'):[2,4,40,0,24],
            ('JACKSON'):[2,4,60,8,16],('WHITE'):[2,6,55,0,24],('HARRIS'):[2,6,45,0,24],
            ('MARTIN'):[2,3,40,0,24],('THOMPSON'):[2,5,50,12,24],('GARCIA'):[2,4,50,0,24],
            ('MARTINEZ'):[2,4,40,0,24],('ROBINSON'):[2,5,50,0,24]})

    
    required=[1,1,2,3,6,6,7,8,9,8,8,8,7,6,6,5,5,4,4,3,2,2,2,2]

    t=24
    
    x={}
    staffNumber={}
    m=Model("work_schedule")
    
    for d in employee:
        for i in range(t):
            for j in range(i+1,t+1):
                x[d,i,j]=m.addVar(vtype=GRB.BINARY,name="x_%s_%d_%d"%(d,i,j))
    for c in range(t):
        staffNumber[c]=m.addVar(vtype=GRB.INTEGER,lb=required[c],name='staffNumber_%d'%c)
 
    m.update()
     
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
 
    m.optimize()
    m.write("work_schedule.lp")
    
    print ("Optimal objective value is %g"%m.objVal)
    if m.status == GRB.Status.OPTIMAL:
        solution = m.getAttr('x', x)
        for d in employee :
            for i in range(t):
                for j in range(i+1,t+1):
                    if solution[d,i,j] == 1:
                        print("The working time of %s is from %g to %g" % (d,i,j))

        staffNumber_sol=m.getAttr('x',staffNumber)
        for c in range(t):
            print 'The number of staff from %d -%d: %d'%(c,c+1,staffNumber_sol[c])
        












