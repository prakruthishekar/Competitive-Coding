# You are given a stream of points on the X-Y plane. Design an algorithm that:

# Adds new points from the stream into a data structure. Duplicate points 
# are allowed and should be treated as 
# different points.Given a query point, counts the number of ways to 
# choose three points from the data structure such that the three points
# and the query point form an axis-aligned square with positive area.
# An axis-aligned square is a square whose edges are all the same length 
# and are either parallel or perpendicular to the x-axis and y-axis.

# Implement the DetectSquares class:

# DetectSquares() Initializes the object with an empty data structure.
# void add(int[] point) Adds a new point point = [x, y] to the data structure.
# int count(int[] point) Counts the number of ways to form axis-aligned 
# squares with point point = [x, y] as described above.


from collections import defaultdict


class DetectSquares:

    def __init__(self):
        self.points = defaultdict(int)
        

    def add(self, point) -> None:
        self.points[tuple(point)] += 1
        

    def count(self, point) -> int:
        square_count = 0
        x1, y1 = point

        for (x2, y2), n in self.points.items():
            # find the diagonal point
            x_dist, y_dist = abs(x1 - x2), abs(y1 - y2)
            # if diagonal point exists
            if x_dist == y_dist and x_dist > 0:
                # find the other two points
                corner1 = (x1, y2) 
                corner2 = (x2, y1)
                if corner1 in self.points and corner2 in self.points:
                    square_count += n * self.points[corner1] * self.points[corner2]

        return square_count



detectSquares = DetectSquares()
detectSquares.add([3, 10])
detectSquares.add([11, 2])
detectSquares.add([3, 2])
print(detectSquares.count([11, 10]))# return 1. You can choose 
                               # - The first, second, and third points
print(detectSquares.count([14, 8])) # return 0. The query point cannot form a square with any points in the data structure.
detectSquares.add([11, 2])# Adding duplicate points is allowed.
print(detectSquares.count([11, 10])) #return 2. You can choose:
                               # - The first, second, and third points
                               # - The first, third, and fourth points