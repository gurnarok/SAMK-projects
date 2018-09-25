import numpy as np

def force(angle,weight):
    angle=np.deg2rad(angle)

    force=weight/(1.74*np.sin(angle)+np.cos(angle))

    return force

def looper(angle_start, angle_end, decimals,n_decimals, weight):
    old_force = 99999999999
    old_angle = 99999999999

    angle_start=angle_start*np.power(10,decimals)
    angle_end=angle_end*np.power(10,decimals)
    
    for angle in range(angle_start, angle_end+1):
        angle = angle/np.power(10,decimals)
        new_force = force(angle,weight)
        if old_force<=new_force:
                print("Angle", end=' ')
                print(round(angle,decimals), end=', ')
                print("with force of", end=' ')
                print(round(old_force,n_decimals),end=' kN\n')
                #print("Angle {:f} degrees, with force of {:.14f} newtons".format(round(old_angle,decimals),old_force))
                break
        old_force = new_force
        old_angle = angle
    
looper(0,90,2,10,6)
