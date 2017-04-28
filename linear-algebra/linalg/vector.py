import math


class Vector(object):

    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    def get_coordinates(self):
        """
        Getter function to return vector coordinates.
        """
        return self.coordinates

    def get_dimension(self):
        """
        Getter function to return vector dimensions.
        """
        return self.dimension

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, v):
        return self.get_coordinates() == v.get_coordinates()

    def __add__(self, v):
        """
        Vector addition is defined by adding each corresponding element
        by index.

        @params:
            - v: Vector to add (Vector)
        @returns:
            - sum of the two vectors (Vector)
        """
        try:
            assert isinstance(v, Vector)
        except AssertionError as e:
            raise TypeError("Vectors can only sum " +
            "with other vectors.").with_traceback(e.__traceback__)
        return Vector([si + vi for si, vi in zip(self.get_coordinates(),
                                                 v.get_coordinates())])

    def __sub__(self, v):
        """
        Vector subtraction is just the inverse of vector addition.
        """
        try:
            assert isinstance(v, Vector)
        except AssertionError as e:
            raise TypeError("Vectors can only subtract " +
            "from other vectors.").with_traceback(e.__traceback__)
        return Vector([si - vi for si, vi in zip(self.get_coordinates(),
                                                 v.get_coordinates())])

    def __mul__(self, x):
        """
        Scalar multiplication multiplies each element of the vector
        by the scalar.

        Note: Due to Python strangeness, the scalar must follow the
        vector for this operation to work (Vector * scalar). __rmul__
        special attributes do not work in this case.

        @params:
            - x: scalar to mulitiply with the vector (int or float)
        @returns:
            - scaled vector (Vector)
        """
        if isinstance(x, int) or isinstance(x, float):
            return Vector([x * c for c in self.get_coordinates()])
        else:
            raise TypeError("Scalar multiplications cannot be performed" +
                            " with objects of type '%s', only ints or floats. "
                            % type(x).__name__)

    def magnitude(self):
        """
        The magnitude of a vector is defined as its "length," spatial
        distance quantified by the Pythagorean theorem.

        @params: none
        @returns: vector magnitude (int)
        """
        return math.sqrt(sum([x**2 for x in self.get_coordinates()]))

    def normalized(self):
        """
        The direction of a vector V is defined as the corresponding unit
        vector W that, when scaled by the magnitude of V, produces V.

        @params: none
        @returns: vector
        """
        return Vector([x/self.magnitude() for x in self.get_coordinates()])

    def dot(self, v):
        """
        Dot (inner) product of two vectors.

        Algorithmically equivalent to projecting one vector onto the other,
        and then multiplying their magnitudes. The dot product is useful
        for computing the inner angle theta between two vectors:

            `v.dot(w) = v.magnitude() * w.magnitude() * cosine(theta)`

        Hence,

            `theta = arccosine( v.dot(w) / ( v.magnitude() * w.magnitude() ) )`

        The sign of the dot product also tells us about the relationship
        between the direction of the two vectors:

            - positive:     vectors point in the same direction
            - zero:         vectors are orthogonal
            - negative:     vectors point in opposite directions

        Additionally, when cos(theta) = 1, the vectors point in the same
        direction and lie on the same line; and when cos(theta) = -1 the
        vectors point in opposite directions and lie on the same line.

        --------

        @params:
            - v: a vector (Vector)
        @returns:
            - the dot product of the two vectors (float)
        """
        try:
            assert isinstance(v, Vector)
        except AssertionError as e:
            raise AssertionError("You can only compute the dot product" +
                                 " of two vectors, not a vector and %s."
                                 % type(v).__name__).with_traceback(
                e.__traceback__)
        return sum([vi * wi for vi, wi in zip(self.get_coordinates(),
                                              v.get_coordinates())])

    def inner_angle(self, v, degrees=False):
        """
        Size of the inner angle between two vectors, in radians.

        See the docstring for the `dot()` method for an explanation for why
        this works.

        --------

        @params:
            - v: a vector (Vector)
        @returns:
            - angle between the two vectors, in radians (float)
        """
        try:
            assert isinstance(v, Vector)
        except AssertionError as e:
            raise AssertionError("You can only compute the inner angle" +
                                 " of two vectors, not a vector and %s."
                                 % type(v).__name__).with_traceback(
                e.__traceback__)
        rad_angle = math.acos(self.dot(v) / (self.magnitude() * v.magnitude()))
        if not degrees:
            return rad_angle
        else:
            return rad_angle * (180 / math.pi)
