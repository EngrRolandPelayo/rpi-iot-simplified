import IO 
from IO import delay

BUTTON1 = IO.BUTTON(11)
LED1 = IO.LED(7)

while True:
 if BUTTON1.READ() == True:
  LED1.ON()
 elif BUTTON1.READ() == False:
  LED1.OFF()


