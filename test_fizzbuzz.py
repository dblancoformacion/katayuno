# test
import unittest
from fizzbuzz import *

class TestFizzBuzz(unittest.TestCase):
	kata=Kata()
	def test_ns(self):
		self.assertEqual(1, self.kata.fizzbuzz(1) )
	def test_x3(self):
		self.assertEqual('Fizz', self.kata.fizzbuzz(3) )
	def test_x5(self):
		self.assertEqual('Buzz', self.kata.fizzbuzz(5) )
	def test_x3x5(self):
		self.assertEqual('FizzBuzz', self.kata.fizzbuzz(15) )

# debería haber un assert por test
# si falla el primero no te enteras del resto
# hay test parametrizados
# usar ignore para los test (estoy con ello, pero ni es válido ni en rojo)

if __name__ == "__main__":
	unittest.main()