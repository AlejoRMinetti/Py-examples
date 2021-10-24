from enum import Enum

class Action(Enum):
  SELL = -1
  HOLD = 0
  BUY = 1

class Velas(Enum):
  OPEN = 0
  CLOSE = 1
  HIGH = 2
  LOW = 3

print("Action.SELL",Action.SELL,"con repr",repr(Action.SELL))
print("Es una Accion?",isinstance(Action.SELL, Action))
print("nombre: "+Action.SELL.name)
print("valor",Action.SELL.value)

print("Asigno con valor:",Action(0))
print("Asigno con key:",Action["BUY"])