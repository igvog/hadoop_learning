# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

b, c = input().split()
b = b.upper() 
sort_list = []
for i in permutations(b, int(c)):
    sort_list.append(i[0]+ i[1])
    print(i)
sort_list.sort()
for j in sort_list:
    print(j)
