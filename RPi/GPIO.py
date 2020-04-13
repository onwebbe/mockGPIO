IN = 0
OUT = 1
LOW = 0
HIGH = 1
BOARD = 0
BCM = 1
MOCK = True
def setup(pin, level = 0):
  pass

def output(pin, level = 0):
  pass

def input(pin):
  return LOW

def setmode(mode):
  pass

class PWM:
  def __init__(self, pin, frequency = 50):
    pass

  def start(self, pin):
    pass

  def ChangeFrequency(self, frequency=50):
    pass

  def ChangeDutyCycle(self, cycle):
    pass
  
  def stop(self):
    pass