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

    #gets a value inside a 1 by 1 square 
    pythagValue = math.sqrt(math.pow(xComponent,2) + math.pow(yComponent,2))

    #checking if the value is in the unit circle. If it is, add one to the counter.
    if (pythagValue <= 1):
        inUnitCircleCounter += 1;
        

valueOfPi = float((inUnitCircleCounter)/iterations * 4)
print("Value of Pi is!!!!")
print(valueOfPi)  


#dervation - number of values in a unit circle / area of one quadrant of a square that
#sits around the unit circle(1*1) 

#that actually equals 1/4*pir^2. The random distruction essentially equals one fourth of the arrea
#then you multiple by 4 to get the value of pi

 
#this is the branch with the changes. 
#dervation - pi(r^2)/(2pi)^2 = number of values in circle/number of values in square

