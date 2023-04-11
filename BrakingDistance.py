import numpy as np

FRICTION_COEF = 0.5 #dry surface lowest value
WET_FRICTION_COEF = 0.25 #wet surface lowest value
STANDARD_GRAVITY = 9.780318
HEIGHT_ASL = 383 #height above sea level in Cracow
LATITUDE = 50.07 #in Cracow
MASS = 1500 #car mass (kg)

real_standard_gravity = STANDARD_GRAVITY * (1 + 0.0053024 * (np.sin(LATITUDE) ** 2)
                                            - 0.0000058 * (np.sin(LATITUDE) ** 2)
                                            - 3.086 * (10**-6)*HEIGHT_ASL)
#print(real_standard_gravity)
normal_force = real_standard_gravity * MASS
friction_force = normal_force * FRICTION_COEF

acceleration = friction_force/MASS

acceleration = round(acceleration,2)
print(acceleration)


def convertKmtoM(speedList):
    for i in range(len(speedList)):
        speedList[i] = speedList[i]*1000/3600
    return speedList


def meassureBrakingDistance(speed):
    return (speed ** 2)/(2*acceleration)


def reponseToTwoDistance(objectDistance, brakingDistance):
    if objectDistance >= brakingDistance:
        if objectDistance >= brakingDistance + objectDistance*(calculateError(objectDistance)) +0.5:
            print("Will stop safely")
        else :
            print("Likely to stop safely")
    else:
        if objectDistance*(1+calculateError(objectDistance))+0.5 >= brakingDistance:
            print("Will collide likely")
        else:
            print("Collision is certain")


def calculateError(distance):
    return (-0.0043 * pow(distance,3) + 0.3293 * pow(distance,2) - 8.0092 * distance + 63.624)/100   # formula for parking error


speeds = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]
speeds = convertKmtoM(speeds)
distances1 = [0.96, 5.78, 11.56, 15.75, 22.05] #chodnik
distances2 = [1.56, 12.04, 20.65, 32.47, 38.05] #parking
distances3 = [1.65, 8.65, 12.75, 17.65, 24.67] #pas
lister = []
for i in speeds:
    lister.append(meassureBrakingDistance(i))

print(lister)

#for i in lister:
#    reponseToTwoDistance(20.65,i)

#for d in distances2:
#    reponseToTwoDistance(d,lister[6])

#for i in lister:
#    for d in distances2:
#        reponseToTwoDistance(d,i)

#    print("nastepny")