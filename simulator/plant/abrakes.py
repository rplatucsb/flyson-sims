"""
Function to propagate airbrake motion
"""

SEC60 = 0.06 # seconds to turn 60 degrees, standard airbrake measurement
SPEED = 60 / 0.06 # speed in degrees / seconds

def step(curr_ab, desired_ab, dt):
    """
    :param curr_ab: ndarray(double) 3-vec in radians
        the current state of the airbrakes
    :param desired_ab: ndarray(double) 3-vec in radians
        the desired state of the airbrakes
    :param dt: timestep
    :return: ndarray(double) 3-vec of the airbrakes in the next dt
    """

    diff_ab = desired_ab - curr_ab
    diff_ab[d<0] = -1
    diff_ab[d>0] = 1
    return curr_ab + diff_ab * SPEED * dt
