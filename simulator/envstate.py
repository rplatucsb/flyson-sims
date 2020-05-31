import numpy as np

class EnvironmentState():
    """
    Stores information about the current environment --- wind, gravity, etc.
    """
    wind = np.array([1,2,3]) # 3-vector for wind, in m/s
    gravity = -9.8 # force of gravity in N
