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

    def round(self, round_to):
        """
        Round a vector's elements to a certain decimal place.

        @params:
            - round_to: num decimal places to round vector elements (int)
        @returns:
            - the rounded vector (Vector)
        """
        # Make sure round_to is an int
        try:
            assert isinstance(round_to, int)
        except AssertionError as e:
            raise TypeError("A vector can only be rounded by an int, not %s."
                            % type(round_to).__name__) from e

        return Vector([round(x, round_to) for x in self.get_coordinates()])

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
        The normalization of a vector V is defined as the corresponding unit
        vector W that, when scaled by the magnitude of V, produces V.

        Geometrically, normalizing a vector returns a unit vector that
        describes its its *direction* in space.

        --------

        @params: none
        @returns:
            - normalized vector
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
            raise TypeError("You can only compute the dot product" +
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
            raise TypeError("You can only compute the inner angle" +
                            " of two vectors, not a vector and %s."
                            % type(v).__name__) from e

        try:
            rad_angle = (math.acos(self.dot(v) /
                        (self.magnitude() * v.magnitude())))
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
            raise TypeError("You can only determine the orthogonality" +
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
            raise TypeError("You can only determine the parallelism" +
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

        --------

        @params:
            - v: a Vector
        @returns:
            - the Vector projected onto v
        """
        # Make sure v is a vector
        try:
            assert isinstance(v, Vector)
        except AssertionError as e:
            raise TypeError("You can only perform projection between" +
                            " two vectors, not a vector and %s."
                            % type(v).__name__) from e

        # Compute the projection of this vector onto v
        return v.normalized() * self.dot(v.normalized())

    def orthogonal_component(self, v):
        """
        Determine the orthogonal component of a vector with another vector v.

        Given two vectors, v and w, the orthogonal component of v is defined as
        the vector that sums with v.project(w) to produce v.

        In this way, the parallel component of v (its projection onto w) and
        the orthogonal component of v allow us to "decompose" v on w, that is,
        to define v strictly in terms of w.
        """
        # Make sure v is a vector
        try:
            assert isinstance(v, Vector)
        except AssertionError as e:
            raise TypeError("You can only find the orthogonal component" +
                            " between two vectors, not a vector and %s."
                            % type(v).__name__) from e

        # Compute the orthogonal component of the vector
        return Vector(self.get_coordinates()) - self.project(v)

    def cross(self, b):
        """
        Calculate the cross product of a vector and another vector b.

        Given two 3D vectors, v and w, the cross product `v x w` defines a
        vector with the following properties:
            * Orthogonal to the plane defined by v and w
            * Has magnitude equal to the area of the parallelogram between
              v and w
            * Direction obeys the right-hand rule

        In the same way that the dot product corresponds geometrically to
        treating one vector as a linear transformation to the number line,
        the cross product has a similar geometric understanding: given a
        linear transformation to the number line, the cross product returns
        a vector. In that sense, think of it as a "reverse" dot product, in
        three dimensions.

        --------

        @params:
            - b: a Vector
        @returns:
            - the cross product (a Vector)
        """
        # Make sure w is a vector
        try:
            assert isinstance(b, Vector)
        except AssertionError as e:
            raise TypeError("You can only find the cross product" +
                            " between two vectors, not a vector and %s."
                            % type(v).__name__) from e

        # Make sure the dimensions of v and w match
        try:
            assert self.get_dimension() == b.get_dimension()
        except AssertionError as e:
            raise Exception("You can only find the cross product" +
                            " of two vectors in" +
                            " the same dimension.") from e

        # Prepare different arrays based on the dimension
        if self.get_dimension() == 3:
            v = self.get_coordinates()
            w = b.get_coordinates()
        elif self.get_dimensions() == 2:
            v = self.get_coordinates() + [0]
            w = b.get_coordinates() + [0]
        else:
            raise Exception("This library only supports calculating" +
                            " cross products in two and three dimensions.")

        # Perform cross product algorithm
        return Vector([(v[1] * w[2]) - (v[2] * w[1]),
                       (v[2] * w[0]) - (v[0] * w[2]),
                       (v[0] * w[1]) - (v[1] * w[0])])

    def parallelogram_area(self, v):
        """
        Calculate the area of the parallelogram spanned by a vector and
        another vector v.

        The magnitude of the cross product v x w is equivalent to the area
        of the parallelogram spanned by the two vectors. Hence:

            ` |v x w| = |v| * |w| * sin(theta)`

        Since |w| * sin(theta) gives us the height of the parallelogram.
        """
        cross = self.cross(v)
        return cross.magnitude()

    def triangle_area(self, v):
        """
        Calculate the area of the triangle spanned by a vector and another
        vector v.

        Like all triangles, the area of this triangle is equivalent to half
        of the area of the parallelogram spanned by the two vectors.
        """
        return self.parallelogram_area(v) / 2
