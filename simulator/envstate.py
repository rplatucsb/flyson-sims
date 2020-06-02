import numpy as np

class EnvironmentState():
    """
    Stores information about the current environment --- wind, gravity, etc.
    """
    wind = np.array([1, 2, 3]) # 3-vector for wind, in m/s
    gravity = -9.8 # force of gravity in N, needs to be a function of altitude
    ref_yaw = np.array([1, 0, 0])
    ref_pitch = np.array([0, 1, 0])
    ref_roll = np.array([0, 0, 1])
