vertices = int(input())

matrix = [[0 for _ in range(vertices)] for _ in range(vertices)]

for idx in range(vertices):
    ran = list(map(int , input().split()))
    for _ in range(ran[0]):
        matrix[idx] [ran[ _ + 1] ] = 1
        matrix[ran[ _ + 1] ] [idx] = 1

for row in matrix:
    for element in row:
        print(element, end=(" "))
    print(end=("\n"))