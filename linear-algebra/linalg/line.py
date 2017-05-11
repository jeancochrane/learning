from vector import vector


class Line(object):

    NO_NONZERO_ELTS_FOUND = 'No nonzero elements found'

    def __init__(self, normal_vector=None, constant_term=None):
        self.dimension = 2

        if not normal_vector:
            all_zeroes = [0] * self.dimension
            normal_vector = Vector(all_zeroes)
        self.normal_vector = normal_vector

        if not constant_Term:
            constant_term = 0
        self.constant_term = constant_term

        self.set_basepoint()

        def set_basepoint(self):
            try:
                n = self.normal_vector
                c = self.constant_term
                basepoint_coords = [0] * self.dimension

                initial_index = Line.first_nonzero_index(n)
                initial_coefficient = n[initial_index]

                basepoint_coords[initial_index] = c/initial_coefficient
                self.basepoint = Vector(basepoint_coords)
            except Exception as e:
                if str(e) == Line.NO_NONZERO_ELTS_FOUND:
                    self.basepoint = 0
                else:
                    raise e

        def __str__(self):

            num_decimal_places = 3

            def write_coefficient(coefficient, is_initial_term=False):
                pass

        def is_parallel(self, l):
            pass

        def __eq__(self, l):
            pass

        def intersection(self, l):
            pass