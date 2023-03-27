print("Enter the processes : ", end="")
p = list(int(i) for i in input().split())
coordinator = max(p)
print(f"current coordinator {max(p)} dies")
p.remove(coordinator)
print("Enter finder : ", end="")
finder = int(input())
finder_position = p.index(finder)
position = finder_position
message = [finder]
print(f"\nP{p[position]} passes {message}")
position += 1
while (p[position] != message[0]):
    message.append(p[position])
    print(f"P{p[position]} passes {message}")
    position = (position+1)%len(p)
print(f"\nNew coordinator : P{max(message)}")