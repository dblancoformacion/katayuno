# test
import unittest
from fizzbuzz import *

class TestFizzBuzz(unittest.TestCase):
	def test_ns(self):
		self.assertEqual(1, Kata.fizzbuzz(1) )
	def test_x3(self):
		self.assertEqual('Fizz', Kata.fizzbuzz(3) )
	def test_x5(self):
		self.assertEqual('Buzz', Kata.fizzbuzz(5) )
	def test_x3x5(self):
		self.assertEqual('FizzBuzz', Kata.fizzbuzz(15) )

# debería haber un assert por test
# si falla el primero no te enteras del resto
# hay test parametrizados
# usar ignore para los test (estoy con ello, pero ni es válido ni en rojo)

if __name__ == "__main__":
	unittest.main()