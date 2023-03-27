a = list(int(i) for i in input("List the process :\n").split())
print(f"Current coordinator - {max(a)} dies\n")
print("Enter node which detects failure : ")
x = int(input())
print()
for i in a[a.index(x):]:
    for j in a[a.index(x):]:
        if i < j:
            print(f"Process{i} ->Election-> Process{j}")
print()
a.remove(max(a))
for i in a[a.index(x):]:# slice operation
    for j in a[a.index(x):]:
        if i < j:
            print(f"Process{i} <-OK Message<- Process{j}")
print()
print(f"Process {max(a)} is the new coordinator")