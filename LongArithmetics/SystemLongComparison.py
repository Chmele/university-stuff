from LongComparison import LongComparison
from LongNumber import LongNumber
import itertools
import functools

class SystemLongComparison:
    def __init__(self, comparisons):
        self.c = comparisons

    def solve(self):
        self.normalize()
        list_m = [i.m for i in self.c]
        list_b = [i.b for i in self.c]
        m = functools.reduce(lambda a, b: a * b, list_m)
        list_M = [m // n.m for n in self.c]
        list_Mi = [LongComparison(a,LongNumber('1'),m).solve()[0] for a, m in zip(list_M, list_m)]
        x = [a*b*c for a,b,c in zip(list_b, list_M, list_Mi)]
        s = functools.reduce(lambda a, b: a + b, x)

        return s % m, m

    def normalize(self):
        new = []
        for c in self.c:
            b, m = c.solve()
            new.append(LongComparison(LongNumber('1'), b, m))
        self.c = new
        self.comprime_modules()

    def comprime_modules(self):
        for i, j in itertools.combinations(self.c, 2):
            new = i.combine(j)
            if new:
                self.try_merge(new)

    def try_merge(self, new):
        for i in self.c:
            t = new.combine(i) 
            if t:
                self.try_merge(t)
        self.c.append(new)