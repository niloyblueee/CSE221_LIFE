n = int(input())

id = list(map(int, input().split()))
marks = list(map(int, input().split()))
id_marks = []
for idx in range(n):
    id_marks.append([id[idx],marks[idx]])

def swaps(data):
    n = len(data)
    swap_count = 0

    for i in range(n):
        max_idx = i
        for j in range(i + 1, n):
            if data[j][1] > data[max_idx][1]:
                max_idx = j
            elif data[j][1] == data[max_idx][1] and data[j][0] < data[max_idx][0]:
                max_idx = j
        
        if max_idx != i:
            data[i], data[max_idx] = data[max_idx], data[i]
            swap_count += 1

    return data, swap_count

final , count = swaps(id_marks)
print(f"Minimum swaps: {count}")

for i in range(n):
    print(f"ID: {final[i][0]} Mark: {final[i][1]}")