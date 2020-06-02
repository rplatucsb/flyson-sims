import numpy as np
from .envstate import EnvironmentState as es
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
    MASS = 3  # fill in actual, initial mass of rocket
    LENGTH = .51  # length of the rocket
    CM = 0.3  # fill in actual, initial center of mass from bottom of rocket
    position = np.array([0, 0, CM])  # position of CM
    momentum = np.zeros(3)  # initial momentum of the rocket
    velocity = momentum / MASS
    q = np.array([0, 0, 0, 1])  # initial orientation of the rocket as quaternion
    orientation = Rotation.from_quat(q)  # Rotation object that stores the orientation
    angular_momentum = np.zeros(3)  # initial angular momentum of the rocket
    angular_velocity = np.zeros(3)  # 3-vector of angular velocity
    abrake_extension = np.array(0)  # 3-vector for each airbrake extension in radians
    abrake_amps_prop = np.array(0)  # 3-vector for the current through each abrake motor

    def quat2mat(self, r):
        """
        :param r: rotation object, the quaternion orientation of the rocket
        :return: ndarray(double) the rotation matrix for the quaternion
        """
        r = r.as_matrix(r)
        return r

    def orien_in_ref(self, rot_matrix):
        """
        :param rot_matrix: ndarray(double) that describes the rotation in matrix form
        :return: ndarray(double) the axes of the rocket in the reference frame
        """
        yaw = np.dot(rot_matrix, es.ref_yaw)
        pitch = np.dot(rot_matrix, es.ref_pitch)
        roll = np.dot(rot_matrix, es.ref_roll)
        return np.array([yaw, roll, pitch])

    def quat_dot(self, velocity, angular_velocity): # may be better to put in smit, idk rn
        """
        :param velocity: ndarray(double) contains the current velocity vector
        :param angular_velocity: ndarray(double) contains current angular velocity
        :return: ndarray(double) derivative of the quaternion describing orientation
        """
        s_dot = 0.5 * (np.vdot(velocity, angular_velocity))
        v_dot = 0.5 * (np.add(self.q[3] * angular_velocity,
                              np.cross(velocity, angular_velocity)))
        q_dot = [v_dot, s_dot]
        return q_dot
