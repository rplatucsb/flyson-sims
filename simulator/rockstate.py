import numpy as np
from scipy.spatial.transform import Rotation

class RocketState(np.ndarray):
    """
    RocketState stores information about the state of the rocket at a given time.
    Unit Standards
    ------------------------
    Force: Newtons
    Distance: Meters
    Time: Seconds
    Mass: Kilograms
    Angles: Radians
    Current: Amps
    
    All others are derived from these.
    """

    LENGTH = .51 # length of the rocket
    position = np.array(0) # position of base
    velocity = np.array(0) # position of base
    angular_position = Rotation() # scipy spatial Rotation of angular position
    angular_velocity = np.array(0) # 3-vector of angular velocity
    abrake_extension = np.array(0) # 3-vector for each airbrake extension in radians
    abrake_amps_prop = np.array(0) # 3-vector for the current through each abrake motor
