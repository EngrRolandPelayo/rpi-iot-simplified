_pin = None
_opin = None
_servopin = None
_p = None
_trig = None
_echo = None
BTDT = None

class USONIC:
 
 import RPi.GPIO as GPIO
 import time

 def __init__(self,trig,echo):
  global _trig
  global _echo
  _trig = trig
  _echo = echo
  self.GPIO.setwarnings(False)
  self.GPIO.setmode(self.GPIO.BOARD)
  self.GPIO.setup(_trig, self.GPIO.OUT)
  self.GPIO.setup(_echo, self.GPIO.IN)
  
 def GETDISTANCE(self):
  global _trig
  global _echo

  self.time.sleep(0.5)
  self.GPIO.output(_trig, 0)
  self.time.sleep(0.5)

  self.GPIO.output(_trig,1)
  self.time.sleep(0.00001)
  self.GPIO.output(_trig,0)

  while self.GPIO.input(_echo) == 0:
   pulse_start = self.time.time()

  while self.GPIO.input(_echo) == 1:
   pulse_end = self.time.time()

  pulse_duration = pulse_end - pulse_start
  distance = pulse_duration * 17150
  distance = round(distance, 2)
  print distance
  return distance


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
  global BTDT
  if BTDT != "CCW":
   print "Turning servo at " + str(_servopin) + " counter clockwise"
   for dc in range(10,0,-1):
    _p.ChangeDutyCycle(dc)
    self.time.sleep(0.1)
  BTDT = "CCW"
 
 def CW(self):
  global _p
  global _servopin
  global BTDT
  if BTDT != "CW":
   print "Turning servo at " + str(_servopin) + " clockwise"
   for dc in range(0,10,1):
    _p.ChangeDutyCycle(dc)
    self.time.sleep(0.1)
  BTDT = "CW"

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
