import IO

myUSONIC = IO.USONIC(11, 12)

while True:
 print myUSONIC.GETDISTANCE()
 
