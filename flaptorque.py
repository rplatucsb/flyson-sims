import numpy as np
import matplotlib.pyplot as plt

def torquefn(A0, rho, v, x, d, L):
    def torque(theta):
        c = A0 * rho * v**2 * np.sin(theta)
        return -c * (x * np.sin(theta) - d * np.cos(theta) / 2
                - L * np.sin(theta) * np.cos(theta))
    return torque

cmsame = torquefn(.07 ** 2, 1.225, 60, 0.0, 0.03, 0.07)
default = torquefn(.07 ** 2, 1.225, 60, .25, 0.03, 0.07)

theta = np.arange(0, np.pi/2, .1)
plt.scatter(np.rad2deg(theta), default(theta), label="default")
plt.scatter(np.rad2deg(theta), cmsame(theta), label="cmsame")
plt.legend()
plt.xlabel("Angle of Extension in degrees")
plt.ylabel("Torque (N*m)")
plt.show()
