from arithmetics import *
from unittest import TestCase

class Test(TestCase):
	def test_lcm(self):
		self.assertTrue(lcm(0, 0) == 0)

	def test_lcm_better(self):
		self.assertTrue(lcm_better(0, 0) == 0)

	def test_lcm_faulty(self):
		self.assertTrue(lcm_faulty(0, 0) == 0)