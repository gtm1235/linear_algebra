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
        return tuple(add_vector)

    def __mul__(self, v):
        add_vector = []
        for i in range(self.dimension):
            add_vector.append(self.coordinates[i] * v.coordinates[i])
        return tuple(add_vector)

    def __sub__(self, v):
        add_vector = []
        for i in range(self.dimension):
            add_vector.append(self.coordinates[i] - v.coordinates[i])
        return tuple(add_vector)

my_vector = Vector([1,2,3])
print(my_vector)
my_vector2 = Vector([1,2,3])
print(my_vector2)
print(my_vector + my_vector2)
print(my_vector - my_vector2)
print(my_vector * my_vector2)