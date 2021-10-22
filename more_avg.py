import pytest

class Maxtix:
    def __init__(self, n, fill_value=0):
        self.rows = [[fill_value] * n for _ in range(n)]

    def __str__(self):
        return "\n".join(map(str, self.rows))
myMat = Maxtix(3)

print(myMat)

