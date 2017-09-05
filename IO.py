_pin = None
_opin = None
_servopin = None
_p = None

class SERVO:
 
 import RPi.GPIO as GPIO
 import time

 def __init__(self,pin):
  global _servopin
  global _p
  _servopin = pin
  self.GPIO.setmode(self.GPIO.BOARD)
  self.GPIO.setwarnings(False)
  self.GPIO.setup(_servopin, self.GPIO.OUT)
  _p = self.GPIO.PWM(_servopin, 50)
  _p.start(0)
 
 def CCW(self):
  global _p
  global _servopin
  print "Turning servo at " + str(_servopin) + " counter clockwise"
  for dc in range(10,0,-1):
   _p.ChangeDutyCycle(dc)
   self.time.sleep(0.1)
 
 def CW(self):
  global _p
  global _servopin
  print "Turning servo at " + str(_servopin) + " clockwise"
  for dc in range(0,10,1):
   _p.ChangeDutyCycle(dc)
   self.time.sleep(0.1)
  
 def SETANGLE(self, angle):
  global _p
  global _servopin
  print "Turning servo at " + str(_servopin) + " an angle of " + str(angle)
  dc = (angle+2)/18
  _p.ChangeDutyCycle(dc)
  self.time.sleep(0.1) 


class LED:

 import RPi.GPIO as GPIO

 def __init__(self,pin):
  global _pin
  _pin = pin
  self.GPIO.setmode(self.GPIO.BOARD)
  self.GPIO.setwarnings(False)
  self.GPIO.setup(_pin, self.GPIO.OUT)

 def ON(self):
  global _pin
  print "Turning On LED at " ,_pin
  self.GPIO.setmode(self.GPIO.BOARD)
  self.GPIO.setup(_pin, self.GPIO.OUT)
  self.GPIO.output(_pin, 1)
  #self.GPIO.cleanup()

 def OFF(self):
  global _pin
  print "Turning Off LED at " ,_pin
  self.GPIO.setmode(self.GPIO.BOARD)
  self.GPIO.setup(_pin, self.GPIO.OUT)
  self.GPIO.output(_pin, 0)
  #self.GPIO.cleanup()

class BUTTON:
 
 import RPi.GPIO as GPIO

 def __init__(self, opin):
  global _opin
  _opin = opin
  self.GPIO.setmode(self.GPIO.BOARD)
  self.GPIO.setwarnings(False)
  self.GPIO.setup(_opin, self.GPIO.IN, pull_up_down=self.GPIO.PUD_UP)

 def READ(self):
  global _opin
  self.GPIO.setmode(self.GPIO.BOARD)
  self.GPIO.setwarnings(False)
  self.GPIO.setup(_opin, self.GPIO.IN, pull_up_down=self.GPIO.PUD_UP)
  if self.GPIO.input(_opin)==0:
   return True
  elif self.GPIO.input(_opin)==1:
   return False
  self.GPIO.cleanup()
 
def delay(sec):
  import time as time
  time.sleep(sec)
