n = int(input())
count = -999999999999999
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))
    
for i in range(n):
    for j in range(n):
        if i > j:
            print(matrix[i][j])
