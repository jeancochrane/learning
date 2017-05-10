import unittest

import env
from linalg.vector import Vector


class TestVectorOperations(unittest.TestCase):

    def test_vector_equality(self):
        a = Vector([1, 2, 3])
        b = Vector([1, 2, 3])
        self.assertEqual(a, b)

    def test_vector_inequality(self):
        a = Vector([1, 2, 3])
        b = Vector([4, 5, 6])
        self.assertNotEqual(a, b)

    def test_vector_addition(self):
        a = Vector([8.218, -9.341])
        b = Vector([-1.129, 2.111])
        self.assertEqual(a + b, Vector([7.089, -7.229999999999999]))

    def test_vector_subtraction(self):
        a = Vector([7.119, 8.215])
        b = Vector([-8.223, 0.878])
        self.assertEqual(a - b, Vector([15.342, 7.337]))

    def test_scalar_multiplication(self):
        a = Vector([1.671, -1.012, -0.318])
        c = 7.41
        self.assertEqual(a * c, Vector([12.38211, -7.49892, -2.35638]))

    def test_vector_rounding(self):
        v = Vector([1.2345, 6.6789])
        self.assertEqual(v.round(2), Vector([1.23, 6.68]))

    def test_vector_magnitude(self):
        v = Vector([-0.221, 7.437])
        self.assertEqual(round(v.magnitude(), 3), 7.440)

    def test_vector_normalization(self):
        w = Vector([1.996, 3.108, -4.554])
        self.assertEqual(w.normalized(), Vector([0.3404012959433014,
                                                 0.5300437012984873,
                                                -0.7766470449528028]))

    def test_dot_product(self):
        v = Vector([7.887, 4.138])
        w = Vector([-8.802, 6.776])
        self.assertEqual(round(v.dot(w), 3), -41.382)

    def test_dot_product_association(self):
        """
        The dot product is associative, meaning it shouldn't matter what
        order the vectors go in.
        """
        v = Vector([7, 4])
        w = Vector([-8, 6.776])
        self.assertEqual(v.dot(w), w.dot(v))

    def test_inner_angle_radians(self):
        v = Vector([3.183, -7.627])
        w = Vector([-2.668, 5.319])
        self.assertEqual(round(v.inner_angle(w), 3), 3.072)

    def test_inner_angle_degrees(self):
        v = Vector([7.35, 0.221, 5.188])
        w = Vector([2.751, 8.259, 3.985])
        self.assertEqual(round(v.inner_angle(w, degrees=True), 3), 60.276)

    def test_orthogonality(self):
        v = Vector([-7.579, -7.88])
        w = Vector([22.737, 23.64])
        self.assertFalse(v.is_orthogonal(w))

        v = Vector([-2.029, 9.97, 4.172])
        w = Vector([-9.231, -6.639, -7.245])
        self.assertFalse(v.is_orthogonal(w))

        v = Vector([-2.328, -7.284, -1.214])
        w = Vector([-1.821, 1.072, -2.94])
        self.assertTrue(v.is_orthogonal(w))

        v = Vector([2.118, 4.827])
        w = Vector([0, 0])
        self.assertTrue(v.is_orthogonal(w))

    def test_parallelism(self):
        v = Vector([-7.579, -7.88])
        w = Vector([22.737, 23.64])
        self.assertTrue(v.is_parallel(w))

        v = Vector([-2.029, 9.97, 4.172])
        w = Vector([-9.231, -6.639, -7.245])
        self.assertFalse(v.is_parallel(w))

        v = Vector([-2.328, -7.284, -1.214])
        w = Vector([-1.821, 1.072, -2.94])
        self.assertFalse(v.is_parallel(w))

        v = Vector([2.118, 4.827])
        w = Vector([0, 0])
        self.assertTrue(v.is_parallel(w))

    def test_identity_vector_orthogonality_and_parallelism(self):
        """
        The zero vector is the only vector that is both orthogonal and
        parallel to itself.
        """
        v = Vector([0, 0, 0])
        self.assertTrue(v.is_orthogonal(v))
        self.assertTrue(v.is_parallel(v))

        w = Vector([4, 5, 6])
        self.assertFalse(w.is_orthogonal(w))
        self.assertTrue(w.is_parallel(w))

    def test_vector_projections(self):
        """
        Testing vector projection, orthogonal components, and
        decomposition.
        """
        v = Vector([3.039, 1.879])
        b = Vector([0.825, 2.036])
        proj = v.project(b)
        self.assertEqual(proj.round(3), Vector([1.083, 2.672]))

        v = Vector([-9.88, -3.264, -8.159])
        b = Vector([-2.155, -9.353, -9.473])
        orth = v.orthogonal_component(b)
        try:
            self.assertEqual(orth.round(3), Vector([-8.350, 3.376, -1.434]))
        except AssertionError as e:
            print(orth.round(3))
            print(Vector([-8.350, 3.376, -1.434]))
            raise(e)

        v = Vector([3.009, -6.172, 3.692, -2.51])
        b = Vector([6.404, -9.144, 2.759, 8.718])
        v_decomposed = (v.project(b) +
                        v.orthogonal_component(b))
        self.assertEqual(v, v_decomposed.round(3))

    def test_cross_product(self):
        """
        Testing the calculation of cross products, as well as the areas
        of parallelograms and triangles spanned by different vectors.
        """
        v = Vector([8.462, 7.893, -8.187])
        w = Vector([6.984, -5.975, 4.778])
        cross = v.cross(w)
        self.assertEqual(cross.round(3), Vector([-11.205,
                                                 -97.609,
                                                 -105.685]))

        v = Vector([-8.987, -9.838, 5.031])
        w = Vector([-4.268, -1.861, -8.866])
        par_area = v.parallelogram_area(w)
        self.assertEqual(round(par_area, 3), 142.122)

        v = Vector([1.5, 9.547, 3.691])
        w = Vector([-6.007, 0.124, 5.772])
        tri_area = v.triangle_area(w)
        self.assertEqual(round(tri_area, 3), 42.565)

if __name__ == '__main__':
    unittest.main()
