from decimal import Decimal, getcontext

from vector import Vector

getcontext().prec = 6


class Line(object):
    NO_NONZERO_ELTS_FOUND_MSG = 'No nonzero elements found'

    def __init__(self, normal_vector=None, constant_term=None):
        self.dimension = 2

        if not normal_vector:
            all_zeros = ['0'] * self.dimension
            normal_vector = (all_zeros)
        normal_vector = [Decimal(x) for x in normal_vector]
        self.normal_vector = normal_vector

        if not constant_term:
            constant_term = Decimal('0')
        self.constant_term = Decimal(constant_term)

        self.set_basepoint()

    def set_basepoint(self):
        try:
            n = self.normal_vector
            c = Decimal(self.constant_term)
            basepoint_coords = ['0'] * self.dimension

            initial_index = Line.first_nonzero_index(n)
            initial_coefficient = Decimal(n[initial_index])

            basepoint_coords[initial_index] = c / initial_coefficient
            self.basepoint = Vector(basepoint_coords)

        except Exception as e:
            if str(e) == Line.NO_NONZERO_ELTS_FOUND_MSG:
                self.basepoint = None
            else:
                raise e

    def __str__(self):

        num_decimal_places = 3

        def write_coefficient(coefficient, is_initial_term=False):
            coefficient = round(coefficient, num_decimal_places)
            if coefficient % 1 == 0:
                coefficient = int(coefficient)

            output = ''

            if coefficient < 0:
                output += '-'
            if coefficient > 0 and not is_initial_term:
                output += '+'

            if not is_initial_term:
                output += ' '

            if abs(coefficient) != 1:
                output += '{}'.format(abs(coefficient))

            return output

        n = self.normal_vector

        try:
            initial_index = Line.first_nonzero_index(n)
            terms = [write_coefficient(n[i], is_initial_term=(i == initial_index)) + 'x_{}'.format(i + 1)
                     for i in range(self.dimension) if round(n[i], num_decimal_places) != 0]
            output = ' '.join(terms)

        except Exception as e:
            if str(e) == self.NO_NONZERO_ELTS_FOUND_MSG:
                output = '0'
            else:
                raise e

        constant = round(self.constant_term, num_decimal_places)
        if constant % 1 == 0:
            constant = int(constant)
        output += ' = {}'.format(constant)

        return output

    @staticmethod
    def first_nonzero_index(iterable):
        for k, item in enumerate(iterable):
            if not MyDecimal(item).is_near_zero():
                return k
        raise Exception(Line.NO_NONZERO_ELTS_FOUND_MSG)

    def parallel_lines(self, line1):
        self_parallel_vector = [self.normal_vector[1], -(self.normal_vector[0])]
        line1_parallel_vector = [line1.normal_vector[1], -(line1.normal_vector[0])]
        vector1 = Vector(self_parallel_vector)
        vector2 = Vector(line1_parallel_vector)
        vector1.are_parallel(vector2)

        if (vector1.inner_angle(vector2)[0]) == 0.0 or (vector1.inner_angle(vector2)[0]) == 180.0:

            if self.basepoint == line1.basepoint:
                return "they are the same line"
            else:
                return "They are parallel but not the same line"
        else:
            return "They are not parallel"

    def intersection(self, line1):
        try:
            y_value = (((-(self.constant_term * line1.normal_vector[0])) + (self.normal_vector[0] * line1.constant_term))
                       /((self.normal_vector[0] * line1.normal_vector[1]) - (
                            self.normal_vector[1] * line1.normal_vector[0])))
            x_value = (((self.constant_term * line1.normal_vector[1]) - (self.normal_vector[1] * line1.constant_term)) /
                   ((self.normal_vector[0] * line1.normal_vector[1]) - (
                               self.normal_vector[1] * line1.normal_vector[0])))
            return [x_value, y_value]
        except:
            return 'there is no intersection'


class MyDecimal(Decimal):
    def is_near_zero(self, eps=1e-10):
        return abs(self) < eps



line1 = Line([1.182, 5.562], 6.744)
line2 = Line([1.773, 8.343], 9.525)

print(line1.parallel_lines(line2))
print(line1.intersection(line2))

