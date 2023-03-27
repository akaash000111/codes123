import math
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
    def sol(self,k,ls,j):
        ls.append(k)
        # print(ls)
        for i in j[k]:
            if i in ls:
                return 1
            if i not in ls:
                if(self.sol(i,ls,j)==1):
                    return 1
        return -1
    def check(self,l1):
        ls=[]
        if((self.sol(list(l1.keys())[0],ls,l1))==1):
            print("Deadlock")
        else:
            print("No deadlock")

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
m=65
for i in lss:
    print(f"Site {i}:\n{dict(vars()[i])}")
    print("Controller: ",chr(m))
    m+=1
    ls=[]
    if((s.sol(list(vars()[i].keys())[0],ls,vars()[i]))==1):
        print("Deadlock")
    else:
        print("No deadlock")

print("Merge")
r,k=0,0
flag=1
while True:
    if r<len(lss):
        if flag==1:
            s.gg.clear()
            s.gg=vars()[lss[r]].copy()
        else:
            s.merge1(vars()[lss[r]],s.gg)
            vars()[lss[r-1]].clear()
            vars()[lss[r-1]]=s.gg.copy()
            if(r==len(lss)-2 and (r+1)%2==0):
                s.merge1(vars()[lss[r+1]],vars()[lss[r-1]])
                vars()[lss[r-1]].clear()
                vars()[lss[r-1]]=s.gg.copy() 
                r+=1
                k-=1
            print("Controller: ",chr(m))
            m+=1
            print(f"After merging:\n{dict(s.gg)}")
            s.check(s.gg)
    flag=not(flag)
    r+=1
    k=r-1
    if r==len(lss):
        for i in range(len(lss)):
            if(i%2!=0):
                lss[i]=math.inf
        for i in lss:
            if i==math.inf:
                lss.remove(i)
        if(r%2!=0):
            lss.remove(lss[len(lss)-1])
        r=0
    if len(lss)==1:
        print("Final graph")
        s.gg=vars()[lss[0]].copy()
        print("Controller: ",chr(m-1))
        print(dict(s.gg))
        s.check(s.gg)
        break