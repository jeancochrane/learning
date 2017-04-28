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

if __name__ == '__main__':
    unittest.main()
