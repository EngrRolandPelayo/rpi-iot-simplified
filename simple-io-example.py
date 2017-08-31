import IO
from IO import delay

LED1 = IO.LED(7)

while True:
 LED1.ON()
 delay(1)
 LED1.OFF()
 delay(1)



