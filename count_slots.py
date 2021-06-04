import math
def result(n):
    return math.ceil(1000 / n) * 20 + 1000 / (600-n)

for k in range(1,600):
    print(f"{k}, {600-k}, {result(k)}")