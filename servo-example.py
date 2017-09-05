import IO
from IO import delay

SERVO1 = IO.SERVO(12)

while True:
 SERVO1.SETANGLE(100)#SERVO1.CW()
 delay(1)
 SERVO1.SETANGLE(50)#SERVO1.CCW()
 delay(1)

