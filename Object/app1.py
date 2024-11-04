from math import sqrt


class Point:
    def __init__(self,X,Y):
        self.X = X
        self.Y = Y
        
    def distance(self,point):
        return sqrt((point.X - self.X) ** 2 + (point.Y - self.Y) ** 2)


##Test##
point1 = Point(3,4)
point2 = Point(5,9)
dist = point1.distance(point2)
#print(dist)