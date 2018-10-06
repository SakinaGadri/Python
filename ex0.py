print ("Hello World")
print ("Is the tank full?")
'''
The dumbest program you'll ever see, sorry!
input: 
area of the tank and intial level of the water
process:
if the intial level < the area of the tank
then add 50 to initial level
else print the tank is full
'''
areaOfTank = 1000
initialLevel = 50 

if initialLevel > areaOfTank: 
    initialLevel +=50
else:
    print ("The tank is now full")