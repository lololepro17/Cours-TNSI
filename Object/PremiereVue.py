from math import sqrt


class Point:
    def __init__(self,X,Y):
        self.X = X
        self.Y = Y
        
    def distance(self,point):
        return sqrt((point.X - self.X) ** 2 + (point.Y - self.Y) ** 2)