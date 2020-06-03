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
    MASS = 3  # FIXME: , initial mass of rocket
    LENGTH = .51  # length of the rocket
    CM = 0.3  # FIXME, initial center of mass from bottom of rocket
    position = np.array([0, 0, CM])  # position of CM
    velocity = np.zeros(3)  # initial momentum of the rocket
    q = np.array([0, 0, 0, 1])  # initial orientation of the rocket as quaternion
    orientation = Rotation.from_quat(q)  # Rotation object that stores the orientation
    angular_momentum = np.zeros(3)  # initial angular momentum of the rocket
    abrake_current = np.array(0)  # 3-vector for each airbrake extension in radians
    abrake_desired = np.array(0)  # 3-vector for the current through each abrake motor

    def get_momentum(self):
        return self.velocity * self.MASS

    def quat2mat(self, r):
        """
        :param r: rotation object, the quaternion orientation of the rocket
        :return: ndarray(double) the rotation matrix for the quaternion
        """
        r = r.as_matrix(r)
        return r



    def omega(self, rot_matrix, L):
        """
        :param rot_matrix: ndarray(double) the rotation matrix
        :param L: ndarray(double) angular momentum
        :return: the angular velocity of the rocket
        """
        return NotImplementedError

    def v_app(self, v_omega, v_cm):
        """
        :param v_omega: ndarray(double) apparent velocity due to angular velocity
        :param v_cm: ndarray(double) apparent velocity of the center of mass
        :return: ndarray(double) the total apparent velocity
        """
        return NotImplementedError


    def ang_of_att(self, v_app):
        """
        :param v_app: apparent velocity of the rocket
        :return: the current angle of attack of the rocket
        """
        return NotImplementedError
