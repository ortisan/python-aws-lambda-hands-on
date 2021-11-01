class Calculadora(object):

  def soma(self, num1, num2):
    return num1 + num2
  
  def subtrai(self, num1, num2):
    return num1 - num2
  
  def multiplica(self, num1, num2):
    return num1 * num2
  
  def divide(self, num1, num2):
    return num1 / num2

# > pytest exemplos/2-teste-unitario.py
import pytest

def test_divisao():
  calc = Calculadora()
  # calc.divide(2, 0)
  with pytest.raises(ZeroDivisionError):
    calc.divide(2, 0)

   