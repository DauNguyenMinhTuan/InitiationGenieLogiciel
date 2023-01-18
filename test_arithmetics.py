from arithmetics import *
from unittest import TestCase, TestSuite, TestLoader, TextTestRunner


class Test(TestCase):
	def test_lcm1(self):
		self.assertRaises(ValueError, lcm, 0, 0)

	def test_lcm2(self):
		self.assertRaises(ValueError, lcm, 0, 100)

	def test_lcm3(self):
		self.assertRaises(ValueError, lcm, 100, 0)

	def test_lcm4(self):
		self.assertTrue(200 == lcm(200, 200))

	def test_lcm5(self):
		self.assertTrue(840 == lcm(60, 168))

	def test_lcm_better1(self):
		self.assertRaises(ValueError, lcm_better, 0, 0)

	def test_lcm_better2(self):
		self.assertRaises(ValueError, lcm_better, 0, 100)

	def test_lcm_better3(self):
		self.assertRaises(ValueError, lcm_better, 100, 0)

	def test_lcm_better4(self):
		self.assertTrue(200 == lcm_better(200, 200))

	def test_lcm_better5(self):
		self.assertTrue(840 == lcm_better(60, 168))

	def test_lcm_faulty1(self):
		self.assertRaises(ValueError, lcm_faulty, 0, 0)

	def test_lcm_faulty2(self):
		self.assertRaises(ValueError, lcm_faulty, 0, 100)

	def test_lcm_faulty3(self):
		self.assertRaises(ValueError, lcm_faulty, 100, 0)

	def test_lcm_faulty4(self):
		self.assertFalse(200 == lcm_faulty(200, 200))

	def test_lcm_faulty5(self):
		self.assertTrue(840 == lcm_faulty(60, 168))


def suite():
	suite = TestSuite()
	suite.addTests(TestLoader().loadTestsFromTestCase(Test))
	return suite


if __name__ == '__main__':
	TextTestRunner(verbosity=2).run(suite())
