import unittest

class Calculadora(object):

  def soma(self, num1, num2):
    return num1 + num2
  
  def subtrai(self, num1, num2):
    return num1 - num2
  
  def multiplica(self, num1, num2):
    return num1 * num2
  
  def divide(self, num1, num2):
    return num1 / num2

class TestCalculadora(unittest.TestCase):

    def test_soma(self):
        calc = Calculadora()
        self.assertEqual(calc.soma(1, 1), 2)

    def test_subtrai(self):
        calc = Calculadora()
        self.assertEqual(calc.subtrai(1, 1), 0)

    def test_multiplica(self):
        calc = Calculadora()
        self.assertEqual(calc.multiplica(2, 2), 4)

    def test_divide(self):
        calc = Calculadora()
        self.assertEqual(calc.divide(4, 2), 2)

if __name__ == '__main__':
    unittest.main()    