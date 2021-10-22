n, k = map(int, input().split())
test_list = []
for i in range(1, n, 1):
    for j in range(i+1, n+1, 1):
        print(i, j," ", i & j)
        test_list.append(i & j)
res = max(set(test_list), key = test_list.count)
print(res)
    # n , k = map(int , input().split())
    # print(k-1 if ((k-1) | k) <= n else k-2)