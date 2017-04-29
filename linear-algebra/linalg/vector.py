import math


class Vector(object):

    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError as e:
            raise ValueError('Vector coordinates must be non-null.') from e

        except TypeError:
            raise TypeError('Vector coordinates must be an iterable.') from e

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
            raise TypeError("Vectors can only add " +
                            "with other vectors.") from e
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
                            "from other vectors.") from e
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
                                 % type(v).__name__) from e
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
                                 % type(v).__name__) from e

        try:
            rad_angle = math.acos(self.dot(v) / (self.magnitude() * v.magnitude()))
        except ZeroDivisionError as e:
            raise ZeroDivisionError("You cannot compute the inner angle" +
                                    " of the zero vector.") from e

        if not degrees:
            return rad_angle
        else:
            return rad_angle * (180 / math.pi)

    def is_orthogonal(self, v):
        """
        Determine whether or not two vectors are orthogonal (perpendicular).

        Two vectors are orthogonal when their dot product is 0.

        --------

        @params:
            - v: a vector (Vector)
        @returns:
            - whether the vectors are orthogonal (bool)
        """
        try:
            assert isinstance(v, Vector)
        except AssertionError as e:
            raise AssertionError("You can only determine the orthogonality" +
                                 " of two vectors, not a vector and %s."
                                 % type(v).__name__) from e

        return (round(self.dot(v), 7) == 0)

    def is_parallel(self, v):
        """
        Determine whether or not two vectors are parallel.

        Two vectors are parallel when their inner angle is 0 or pi/2 radians
        (0 or 180 degrees).

        --------

        @params:
            - v: a vector (Vector)
        @returns:
            - whether the vectors are parallel (bool)
        """
        try:
            assert isinstance(v, Vector)
        except AssertionError as e:
            raise AssertionError("You can only determine the parallelism" +
                                 " of two vectors, not a vector and %s."
                                 % type(v).__name__) from e
        try:
            return (round(self.inner_angle(v), 7) == 0 or
                    round(self.inner_angle(v, degrees=True), 7) == 180)
        except ZeroDivisionError as e:
            if str(e) == ("You cannot compute the inner angle" +
                          " of the zero vector."):
                return True
            else:
                raise(e)

    def project(self, v):
        """
        Project a vector onto another vector v.

        Projection is a convenient way to decompose two vectors. Geometrically,
        you can imagine it as "assuming the perspective" of one vector, and
        viewing the other vector from that lens.

        Given two vectors, v and w, the projection of v onto w is defined
        mathematically by taking the normalization of w (its direction) and
        scaling it by the dot product of v and the normalization of w (the
        length of v "seen from the perspective" of w).
        """
        pass

    def orthogonal_component(self, v):
        """
        Determine the orthogonal component of a vector with another vector v.

        Given two vectors, v and w, the orthogonal component of v is defined as
        the vector that sums with v.project(w) to produce v.

        In this way, the parallel component of v (its projection onto w) and
        the orthogonal component of v allow us to "decompose" v on w, that is,
        to define v strictly in terms of w.
        """
        pass
