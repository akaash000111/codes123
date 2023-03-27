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
ls1=[]
for i in lss:
    print(f"Enter the coordinating the process for {i}: ")
    ls1.append(int(input()))
for i in lss:
    print(f"Site {i}:\n{dict(vars()[i])}")
flag1=1
print("Check for local deadlock")
for i,j in zip(lss,ls1):
    ls=[]
    print(f"Site : {i} and Coordinator : {j}")
    if((s.sol(j,ls,vars()[i]))==1):
        print("Deadlock")
        flag1=0
    else:
        print("No deadlock")
print(f"Check for global deadlock\nCoordinating process : {ls1[0]}")
if flag1==1:
    flag=1
    for i in lss:
        if flag==1:
            s.gg=vars()[i].copy()
            flag=0
        else:
            s.merge1(vars()[i],s.gg)
    print(f"After merging:\n{dict(s.gg)}")
    ls=[]
    if((s.sol(ls1[0],ls,s.gg))==1):
        print("Deadlock")
    else:
        print("No deadlock")