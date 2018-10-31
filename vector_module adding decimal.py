from math import sqrt, pi, acos
#import numpy as np
from decimal import Decimal, getcontext

getcontext().prec = 6

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple([Decimal(x) for x in coordinates])
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
            add_vector.append(Decimal(scalar) * self.coordinates[i])
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
        return Decimal(sqrt(sq_total))

    def normalize(self):
        try:
            mag_temp = self.magnitude()
            new_coordinates = [x / mag_temp for x in self.coordinates]
            new_coordinates_dec = [Decimal(x) for x in new_coordinates]
            return Vector(new_coordinates_dec)
        except ZeroDivisionError:
            print('Cannot normalize the zero vector')

    def dot_product(self, w):
        new_coordinates = [x * y for x, y in zip(self.coordinates, w.coordinates)]
        new_coordinates = [Decimal(x) for x in new_coordinates]
        return sum(new_coordinates)

    def inner_angle(self, w):
        temp_dot = self.dot_product(w)
        mag_self = self.magnitude()
        mag_w = w.magnitude()
        try:
            ang_radians = acos(temp_dot / (mag_self * mag_w))
            ang_degrees = 180 * (ang_radians / pi)
            return ang_radians , ang_degrees
        except:
            print("Cannot compute angle with zero vector")

    def are_ortho_par(self, v):
        if (self.magnitude() and v.magnitude()) > Decimal(0):
            if self.inner_angle(v)[0] == 0:
                print("The are parellel")
            elif self.dot_product(v) == 0:
                print("They are orthogonal")
            else:
                print("They are neither parallel or orthogonal")
        else:
            return(print("they are both orthogonal and parallel"))

my_vector = Vector([7.887, 4.138])
my_vector2 = Vector([-8.802, 6.776])
my_vector3 = Vector([-5.955, -4.904, -1.874])
my_vector4 = Vector([-4.496, -8.755, 7.103])
my_vector5 = Vector([3.183, -7.627])
my_vector6 = Vector([-2.668, 5.319])
my_vector7 = Vector([0,5])
my_vector8 = Vector([5, 0])
#print(my_vector.dot_product(my_vector2))
#print(my_vector3.dot_product(my_vector4))
#print(my_vector5.inner_angle(my_vector6))
print(my_vector7.inner_angle(my_vector8))
print(my_vector7.are_ortho_par(my_vector8))