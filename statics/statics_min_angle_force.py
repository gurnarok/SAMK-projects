import numpy as np

def force(angle,weight):
    ## Calculate the force, with given weight and angle.
    angle=np.deg2rad(angle)

    force=weight/(1.74*np.sin(angle)+np.cos(angle))

    return force
#END force
def looper(angle_start, angle_end, decimals,n_decimals, weight):
    #
    # Loop until we get the decired decimal point count.
    #
    for dec in range(0,decimals+1):
        old_force = 99999999999
        old_angle = 99999999999
        # Python for loops don't seem to like float numbers, so we make a float(0.001) to int(1)
        # and float(89.999) into int(89999)
        angle_start = int(angle_start*(10**dec))
        angle_end   = int(angle_end*(10**dec))
        ## angle_end+1 because it would stop before the last max angle.
        for angle in range(angle_start, angle_end+1):
            angle = angle*(10**-dec)
            new_force = force(angle,weight)
            if old_force<=new_force:
                # Compare the angle-1 to angle.
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
