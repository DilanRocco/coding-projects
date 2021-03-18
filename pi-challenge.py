import random 
import math
iterations = 51000
inUnitCircleCounter = 0
for i in range(iterations):
    #Creates the X and Y values used to plot on unit circle values from 0.0 to 1.0
    xComponent = random.random()
    yComponent = random.random()

    #Check Values
    #print(xComponent)
    #print(yComponent)

    pythagValue = math.sqrt(math.pow(xComponent,2) + math.pow(yComponent,2))

    #checking if the value is in the unit circle. If it is, add one to the counter.
    if (pythagValue <= 1):
        inUnitCircleCounter += 1;
        

valueOfPi = float((inUnitCircleCounter*4))/iterations
print("Value of Pi is!!!!")
print(valueOfPi)  



#dervation - pi(r^2)/(2pi)^2 = number of values in circle/number of values in square

