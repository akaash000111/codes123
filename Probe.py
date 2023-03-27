from collections import defaultdict
class sl:
    def __init__(self):
        self.gg=defaultdict(list)
    def inh(self,u,v,n):
        n[u].append(v)
    def merge1(self,ss1,ss2):
        ss2=self.gg.copy()
        self.gg.clear()
        for f in(ss1,ss2):
            for k,v in f.items():
                for p in v:
                    self.gg[k].append(p)
    def check(self,di,k):
        for i in di.keys():
            if i==k:
                return 1
        return 0
    def sol(self,k,j):
        ls=[]
        lss=[]
        m={}
        ls.append(k)
        lss.append(k)
        while ls:
            t=ls.pop(0)
            for i in j[t]:
                if i not in m.keys():
                    m[i]=[list((k,t,i))]
                else:
                    m[i].append(list((k,t,i)))
                # print(m)
                if i not in lss:
                    lss.append(i)
                    ls.append(i)
        return m

s=sl()
dh=defaultdict(list)
dr=defaultdict(list)
r=int(input("Enter the number of resources : "))
p=int(input("Enter the number of processes : "))
lss=[]
while(True):
    r1=int(input("Enter the resource : "))
    if r1<0:
        break
    if r1==0 or r1>r:
        print("Enter valid resource")
    q = int(input("Enter the process holding resources : "))
    if q==0 or q>p:
        print("Enter valid process")
    qq = int(input("Enter the process requesting resources : "))
    if qq==0 or qq>p:
        print("Enter valid process")
    w=str(input("Enter the site for the processes : "))
    if w not in lss:
        lss.append(w)
        vars()[w]=defaultdict(list)
    s.inh(q,qq,vars()[w])
    dh[r1].append(q)
    dr[r1].append(qq)
for i in lss:
    print(f"Site {i}:\n{dict(vars()[i])}")
flag1=1
y1=int(input("Enter requesting process: "))
x1=int(input("Enter resource holding process: "))
flag=1
for i in lss:
    if flag==1:
        s.gg=vars()[i].copy()
        flag=0
    else:
        s.merge1(vars()[i],s.gg)
print(f"WFG:\n{dict(s.gg)}")
d1=s.sol(y1,s.gg)
print(f"Probe message received:\n{dict(d1)}")
if(s.check(d1,y1)==1):
    print("Deadlock")
else:
    print("No deadlock")