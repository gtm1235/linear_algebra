from math import sqrt, pi
import numpy as np


class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple([coordinates])
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be non empty')

        except TypeError:
            raise TypeError('The coordinates must be an iteratable')

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def __add__(self, v):
        add_vector = []
        for i in range(self.dimension):
            add_vector.append(self.coordinates[i] + v.coordinates[i])
        return Vector(add_vector)

    def __mul__(self, scalar):
        add_vector = []
        for i in range(self.dimension):
            add_vector.append(scalar * self.coordinates[i])
        return Vector(add_vector)

    def __sub__(self, v):
        add_vector = []
        for i in range(self.dimension):
            add_vector.append(self.coordinates[i] - v.coordinates[i])
        return Vector(add_vector)

    def magnitude(self):
        sq_total = 0
        for i in range(self.dimension):
            sq_total += self.coordinates[i] ** 2
        return sqrt(sq_total)

    def normalize(self):
        try:
            mag_temp = self.magnitude()
            new_coordinates = [x / mag_temp for x in self.coordinates]
            return Vector(new_coordinates)
        except ZeroDivisionError:
            print('Cannot normalize the zero vector')

    def dot_product(self, w):
        new_coordinates = [x * y for x, y in zip(self.coordinates, w.coordinates)]
        return sum(new_coordinates)

    def inner_angle(self, w):
        temp_dot = self.dot_product(w)
        mag_self = self.magnitude()
        mag_w = w.magnitude()
        try:
            ang_radians = np.arccos(temp_dot / (mag_self * mag_w))
            ang_degrees = 180 * (ang_radians / pi)
            return ang_radians , ang_degrees
        except ZeroDivisionError:
            print("Cannot compute angle with zero vector")

my_vector = Vector([7.887, 4.138])
my_vector2 = Vector([-8.802, 6.776])
my_vector3 = Vector([-5.955, -4.904, -1.874])
my_vector4 = Vector([-4.496, -8.755, 7.103])
my_vector5 = Vector([3.183, -7.627])
my_vector6 = Vector([-2.668, 5.319])
my_vector7 = Vector([0,0,1])
my_vector8 = Vector([2.751, 8.259, 3.985])
#print(my_vector.dot_product(my_vector2))
#print(my_vector3.dot_product(my_vector4))
#print(my_vector5.inner_angle(my_vector6))
print(my_vector7.inner_angle(my_vector8))