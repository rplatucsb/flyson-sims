import matplotlib.pyplot as plt
import numpy as np
import pickle as pkl
from .smit import SimIter

rs = []
time = np.array(0)
pos = np.array(0.3)
vel = np.array(0)
sm = SimIter()
for r in sm:
    rs.append(r)
    print('Altitude: {:.3f} Velocity: {:.3f} Time: {:.1f}'.format(r.position, r.velocity, sm.envstate.time))
    time = np.append(time, sm.envstate.time)
    pos = np.append(pos, r.position)
    vel = np.append(vel, r.velocity)
plt.figure(1)
plt.plot(time, pos, '.')
plt.plot(time, vel, '.')
plt.xlabel('Time (s)')
plt.ylabel('Altitude (m)')
plt.title('1 DOF Rocket Simulation')
plt.show()
input()

pkl.dump(rs, open("firstrun.pkl", "wb"))
