from math import sqrt

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be non empty')

        except TypeError:
            raise TypeError('The coordinates must be an iteratable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def __add__(self,v):
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
            sq_total  += self.coordinates[i]**2
        return sqrt(sq_total)

    def normalize(self):
        mag_temp = self.magnitude()
        new_coordinates = [x/(mag_temp) for x in self.coordinates]
        return Vector(new_coordinates)


my_vector = Vector([-0.221, 7.437])
print(my_vector.magnitude())
my_vector2 = Vector([8.813, -1.331, -6.247])
print(my_vector2.magnitude())
my_vector3 = Vector([5.581, -2.136])
print(my_vector3.normalize())
my_vector4 = Vector([1.996, 3.108, -4.554])
print(my_vector4.normalize())