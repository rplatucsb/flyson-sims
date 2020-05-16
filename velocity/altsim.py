import matplotlib.pyplot as plt
from numpy import sin, cos, pi
import numpy as np
from eng import Engine

G = -9.8
DRAG_COEFFICIENT = .8
DENSITY = 1.2
INITIAL_ANGLE = 0
 

f50 = Engine("f50.eng")
f15 = Engine("f15.eng")
g40 = Engine("g40.eng")
 
INTERVAL = .01

nd = 100
nm = 100

diameters = np.linspace(0.03, 0.10, nd)
masses = np.linspace(0.400, 1.000, nm)

x, y = np.meshgrid(diameters, masses)
z = np.zeros(x.shape)

for d in range(nd):
    for m in range(nm):
         
        area = pi * (x[d, m]/2) ** 2
        f_grav = G * y[d, m]
        def drag(v):
            return (-0.5 if v > 0 else 0.5) * DENSITY * DRAG_COEFFICIENT * area * (v ** 2)
         
        curr_time = 0
        curr_v = 0
        altitude = 0
        total_impulse = 0

        z[d, m] = 0
        while altitude >= 0:
             
            # idx = int(curr_time * 4)
            # slope = -(IMPULSE[idx] - IMPULSE[idx + 1]) / .25
            # thrust = IMPULSE[idx] + slope * (curr_time % .25)
            thrust = g40(curr_time)

            force = thrust + f_grav + drag(curr_v)
            impulse = force * INTERVAL

            total_impulse += thrust * INTERVAL

            curr_v += impulse / y[d, m]
            altitude += curr_v * INTERVAL
             
            if altitude > z[d, m]:
                z[d, m] = altitude

            curr_time += INTERVAL

z *= 3.28084 # to feet
x *= 39.37008 # to inches

np.save("xyz.npy", np.vstack((x, y, z)))
c = plt.pcolormesh(x, y, z, cmap="RdBu", vmin=0, vmax=z.max())
plt.gca().axis([x.min(), x.max(), y.min(), y.max()])
plt.gcf().colorbar(c, ax=plt.gca())
plt.title("Maximum Altitude of Estes G40 (Feet)")
plt.xlabel("Diameter (inches)")
plt.ylabel("Mass (kg)")
plt.show()
