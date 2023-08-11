from math import sqrt
from itertools import product, combinations


X = [
    [3, 6],
    [2, 3],
    [2, 2],
    [5, 5],
    [3, 5],
    [1, 1]
]

X = [
    (1,4),
    (2,5),
    (2,8),
    (3,4),
    (3,5),
    (4,1),
    (4,7),
    (5,6),
    (7,6),
    (8,1)
]


class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __mod__(self, other):
        return sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

    def __eq__(self, other):
        return self.x, self.y == other.x, other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __repr__(self):
        return str((self.x, self.y))

    def copy(self):
        return Point(self.x, self.y)


class Cluster:
    def __init__(self, points):
        self.points = set(points)

    def __add__(self, other):
        return self.__class__(self.points | other.points)

    def __eq__(self, other):
        return self.points == other.points

    def __str__(self):
        return str(self.points)

    def __repr__(self) -> str:
        return str(self)

    @property
    def center(self):
        return Point(sum(p.x for p in self.points), sum(p.y for p in self.points))

    def copy(self):
        return Cluster({point.copy() for point in self.points})


class SingleLink(Cluster):
    def __mod__(self, other):
        return min(product(self.points, other.points), key=lambda x: Point.__mod__(*x))


class CompleteLink(Cluster):
    def __mod__(self, other):
        return max(product(self.points, other.points), key=lambda x: Point.__mod__(*x))


class AverageLink(Cluster):
    def __mod__(self, other):
        return self.center, other.center


class KMeans:
    def process_point_list(self, point_list, k):
        point_list = [Point(*point) for point in point_list]
        old = [Cluster([point]) for point in point_list[:k]]
        print(f"KMeans:\n{old}")
        for point in point_list:
            min(old, key=lambda cluster: point.__mod__(
                cluster.center)).points.add(point)
        print(old)
        current = []
        while current != old:
            for point in point_list:
                for cluster in old:
                    if point in cluster.points:
                        cluster.points.remove(point)
                min(old, key=lambda cluster: point.__mod__(
                    cluster.center)).points.add(point)

            current = old.copy()
        print(old)
        return old


class ClusterGrouper:
    def process_point_list(self, point_list, cluster_class=SingleLink, point_class=Point):
        print(f"{cluster_class.__name__}: ")
        pl = [point_class(*pair) for pair in point_list]
        clusters = [cluster_class([point]) for point in pl]

        while len(clusters) > 1:
            c1, c2 = min(combinations(clusters, 2), key=lambda x: point_class.__mod__(
                *cluster_class.__mod__(*x)))
            clusters.remove(c1)
            clusters.remove(c2)
            clusters.append(c1 + c2)
            print(*clusters)

        return clusters


cg = ClusterGrouper()
cg.process_point_list(X, cluster_class=SingleLink)
cg.process_point_list(X, cluster_class=CompleteLink)
cg.process_point_list(X, cluster_class=AverageLink)

KMeans().process_point_list(X, 3)
