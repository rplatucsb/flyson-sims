import numpy as np
from scipy.spatial.transform import Rotation
import functions

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
    momentum = np.zeros(3)  # initial momentum of the rocket
    q = np.array([0, 0, 0, 1])  # initial orientation of the rocket as quaternion
    orientation = Rotation.from_quat(q)  # Rotation object that stores the orientation
    angular_momentum = np.zeros(3)  # initial angular momentum of the rocket
    abrake_extension = np.array(0)  # 3-vector for each airbrake extension in radians
    abrake_amps_prop = np.array(0)  # 3-vector for the current through each abrake motor

    def get_velo(self, momentum):
        return momentum / self.MASS

    def quat2mat(self, r):
        """
        :param r: rotation object, the quaternion orientation of the rocket
        :return: ndarray(double) the rotation matrix for the quaternion
        """
        r = r.as_matrix(r)
        return r

    def rot_inert(self):  # FIXME: needs to change as mass changes
        """
        :return: the rotational inertia tensor for the rocket
        """
        ixx = 60  # FIXME: not correct values
        iyy = 60
        izz = 60
        return np.array([[ixx, 0, 0],
                         [0, iyy, 0],
                         [0, 0, izz]])

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

    def v_cm(self, wind, velocity):
        """
        :param wind: ndarray(double) vector for wind velocity
        :param velocity: ndarray(double) velocity of rocket without wind
        :return: ndarray(double) apparent velocity due to wind
        """
        return NotImplementedError

    def v_omega(self, omega, roll_a, X_bar):
        """
        :param omega: ndarray(double) angular velocity vector
        :param roll_a: roll axis
        :param X_bar: distance between CM and CP
        :return: ndarray(double) apparent velocity due to angular velocity
        """
        return NotImplementedError

    def ang_of_att(self, v_app):
        """
        :param v_app: apparent velocity of the rocket
        :return: the current angle of attack of the rocket
        """
        return NotImplementedError

    def reynolds(self, length, velocity, mu):
        """
        :param length: length of the rocket
        :param velocity: apparent velocity
        :param mu: kinematic viscosity
        :return: the current Reynolds Number
        """
        return NotImplementedError

    def mu(self, temp_ground, temp_alt, C):
        """
        :param temp_ground: reference temperature
        :param temp_alt: temperature at current altitude
        :param C: Sutherland's Constant
        :return: the current kinetic viscosity
        """
        raise NotImplementedError

    def mach_num(self, velocity, gamma, R, temp_alt):
        """
        :param velocity: apparent velocity of the rocket
        :param gamma: ratio of specific heats of air
        :param R: Reynold's Number
        :param temp_alt: temperature at the current altitude
        :return: the current Mach Number
        """
        return NotImplementedError