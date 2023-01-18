from arithmetics import *
from unittest import TestCase

class Test(TestCase):
	def test_lcm(self):
		self.assertTrue(0 == lcm(0, 0))
		self.assertTrue(0 == lcm(0, 100))
		self.assertTrue(0 == lcm(100, 0))
		self.assertTrue(200 == lcm(200, 200))
		self.assertTrue(840 == lcm(60, 168))

	def test_lcm_better(self):
		self.assertTrue(0 == lcm_better(0, 0))
		self.assertTrue(0 == lcm_better(0, 100))
		self.assertTrue(0 == lcm_better(100, 0))
		self.assertTrue(200 == lcm_better(200, 200))
		self.assertTrue(840 == lcm_better(60, 168))

	def test_lcm_faulty(self):
		self.assertTrue(0 == lcm_faulty(0, 0))
		self.assertTrue(0 == lcm_faulty(0, 100))
		self.assertTrue(0 == lcm_faulty(100, 0))
		self.assertTrue(200 == lcm_faulty(200, 200))
		self.assertTrue(840 == lcm_faulty(60, 168))