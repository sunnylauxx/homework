class Point:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self,x=0, y=0):
        """ Create a new point at the origin """
        self.x = x
        self.y = y



    def distance_from_origin(self):
            """ Compute my distance from the origin """
            return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def __str__(self):  # All we have done is renamed the method
        return "({0}, {1})".format(self.x, self.y)

p = Point(3,4)         # Instantiate an object of type Point

q = Point(10,11)         # Make a second point

f = Point(3,4)

print(p.x, p.y, q.x, q.y)  # Each point object has its own x and y
p.x=4
p.y=6
q.x=10
q.y=11
print(p.x, p.y, q.x, q.y)


print("(x={0}, y={1})".format(p.x, p.y),"before")
distance_squared_from_origin = p.x * p.x + p.y * p.y
dist = q.distance_from_origin()
print(dist)


def print_point(pt):
    print("({0}, {1})".format(pt.x, pt.y))

print_point(p)

#print(p.to_string())
print(str(p))