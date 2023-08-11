from LongComparison import LongComparison
from LongNumber import LongNumber
from SystemLongComparison import SystemLongComparison

a1 = LongNumber('13')
b1 = LongNumber('7')
m1 = LongNumber('24')

a2 = LongNumber('8')
b2 = LongNumber('5')
m2 = LongNumber('75')

c1 = LongComparison(a1, b1, m1)
c2 = LongComparison(a2, b2, m2)

s = SystemLongComparison([c1,c2])
answer = s.solve()
print(answer[0])
print(answer[1])