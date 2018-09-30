import numpy as np

def force(angle,weight):
    angle=np.deg2rad(angle)

    force=weight/(1.74*np.sin(angle)+np.cos(angle))

    return force
#END force
def looper(angle_start, angle_end, decimals,n_decimals, weight):
    for dec in range(0,decimals+1):
        old_force = 99999999999
        old_angle = 99999999999
        angle_start = int(angle_start*(10**dec))
        angle_end   = int(angle_end*(10**dec))
        for angle in range(angle_start, angle_end+1):
            angle = angle*(10**-dec)
            new_force = force(angle,weight)
            if old_force<=new_force:
                print("Angle", end=' ')
                print(round(angle,dec))
                print("Force", end=' ')
                print(round(old_force,n_decimals),end=' kN\n')
                #print("Angle {:f} degrees, with force of {:.14f} newtons".format(round(old_angle,decimals),old_force))
                break
            old_force = new_force
            old_angle = angle
        angle_start = angle-(10**-dec)
        angle_end   = angle
        # FOR angle
    #FOR dec
#END looper

aStart = 0
aEnd = 90
decimalPoints = 5
newtonDecimals = 10
weightkiloNewtons = 6
looper(0,90,5,10,6)
