import numpy as np

class EnvironmentState():
    """
    Stores information about the current environment --- wind, gravity, etc.
    """
    time = 0 # time in seconds
    wind = np.array([1, 2, 3])  # 3-vector for wind, in m/s
    gravity = -9.8  # force of gravity in N, needs to be a function of altitude
    ref_yaw = np.array([1, 0, 0])
    ref_pitch = np.array([0, 1, 0])
    ref_roll = np.array([0, 0, 1])
    rho = 1.0  # FIXME: use correct air density
    sutherland = 120  # sutherland's constant in kelvin
    ref_temp = 291.15  # reference temperature in kelvin
    ref_vis = 1.827e-7  # reference viscosity in Pascals * seconds
    gamma = 1.4  # ratio of specific heats of air

    def __init__(self):
        """
        :param dt: timestep
        """
        self.dt = dt

    def step(self, dt):
        return self.time += dt
