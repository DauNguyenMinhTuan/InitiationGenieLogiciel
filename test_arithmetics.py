from unittest import TestCase
import unittest
from arithmetics import *
from lcmException import LcmException


class Test(TestCase):
    def setUp(self):
        self.a = 60
        self.b = 168


    # Test lcm
    def test_lcm_001(self):
        self.assertRaises(LcmException, lcm, 0, 0)

    def test_lcm_002(self):
        self.assertRaises(LcmException, lcm, 0, self.a)

    def test_lcm_003(self):
        self.assertRaises(LcmException, lcm, self.a, 0)

    def test_lcm_004(self):
        self.assertTrue(self.a == lcm(self.a, self.a))

    def test_lcm_005(self):
        self.assertTrue(840 == lcm(self.a, self.b))


    # Test lcm_better
    def test_lcm_better_001(self):
        self.assertRaises(LcmException, lcm_better, 0, 0)

    def test_lcm_better_002(self):
        self.assertRaises(LcmException, lcm_better, 0, self.a)

    def test_lcm_better_003(self):
        self.assertRaises(LcmException, lcm_better, self.a, 0)

    def test_lcm_better_004(self):
        self.assertTrue(self.a == lcm_better(self.a, self.a))

    def test_lcm_better_005(self):
        self.assertTrue(840 == lcm_better(self.a, self.b))


    # Test lcm_faulty
    def test_lcm_faulty_001(self):
        self.assertRaises(LcmException, lcm_faulty, 0, 0)

    def test_lcm_faulty_002(self):
        self.assertRaises(LcmException, lcm_faulty, 0, self.a)

    def test_lcm_faulty_003(self):
        self.assertRaises(LcmException, lcm_faulty, self.a, 0)

    def test_lcm_faulty_004(self):
        self.assertFalse(self.a == lcm_faulty(self.a, self.a))

    def test_lcm_faulty_005(self):
        self.assertTrue(840 == lcm_faulty(self.a, self.b))

    # Test main



def suite():
    # Test suite
    suite = unittest.TestSuite()
    suite.addTests(
        unittest.TestLoader().loadTestsFromTestCase(Test)
    )
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())
