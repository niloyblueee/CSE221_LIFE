nodes, edges = map(int, input().split())

diction = {} 

u = list(map(int, input().split()))
v = list(map(int, input().split()))
w = list(map(int, input().split()))

for idx in range(1, nodes+1):
    diction[idx] = []

for idx in range(len(u)):
    diction[u[idx]].append((v[idx], w[idx]))
        
sorted_dict = dict(sorted(diction.items()))

for i in sorted_dict.keys():
    print(f"{i}: ",end=(""))
    print(*sorted_dict[i])