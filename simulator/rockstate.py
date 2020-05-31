import numpy as np

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
    
    All others are derived from these.
    """

    LENGTH = .51 # length of the rocket
    position = np.array(0) # position of base
    velocity = np.array(0) # position of base
    avelocity = np.array(0) # position of base
    orientation = 0 # store this in euler angles or quaternions
    abrake_extension = np.array(0) # 3-vector for each airbrake extension in radians

    def euler(self):
        """
        :returns: ndarray(double) 3-vector of rocket roll, pitch, yaw
        """
        raise NotImplementedError
        return roll, pitch, yaw

    def quaternion(self):
        """
        :returns: ndarray(quat) 1-vector of quaternion pose
        """
        raise NotImplementedError
        return quat

    def pos_com(self):
        """
        :returns: a numpy 3-vector of position at the center of mass
        """
        raise NotImplementedError
        return xyz

    def pos_top(self):
        """
        :return: ndarray 3-vector of position at the tip of the nose
        """
        raise NotImplementedError
        return xyz

    def pos_abrake(self):
        """
        :return: ndarray 3-vector of position position at 
            the center of the tube at the top of the airbrakes
        """
        raise NotImplementedError
        return xyz

    def mass(self):
        """
        :return: current mass of rocket as a float
        """
        raise NotImplementedError
        return kg

    def velocity(self):
        """
        :return: current velocity of rocket as ndarray(double) 3-vector
        """
        raise NotImplementedError
        return v

    def euler_velocity(self):
        """
        :return: ndarray(double) 3-vector of angular velocity
            roll, pitch, yaw over time
        """
        raise NotImplementedError
        return omega

    def quaternion_velocity(self):
        """
        :return: ndarray(quaternion) 1-vector of angular pose over time
        """
        raise NotImplementedError
        return omega

    def abrake(self):
        """
        :return: ndarray(double) 3-vector of the extension of each airbrake
        """
        raise NotImplementedError
        return self.abrake_extension
