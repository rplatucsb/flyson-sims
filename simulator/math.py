import numpy as np
from .envstate import EnvironmentState as es

class math():
    """
    Store the mathematical functions necessary for the calculations involved in the
    simulation
    """
    def orien_in_ref(self, rot_matrix):
        """
        :param rot_matrix: ndarray(double) that describes the rotation in matrix form
        :return: ndarray(double) the axes of the rocket in the reference frame
        """
        yaw = np.dot(rot_matrix, es.ref_yaw)
        pitch = np.dot(rot_matrix, es.ref_pitch)
        roll = np.dot(rot_matrix, es.ref_roll)
        return np.array([yaw, roll, pitch])


    def quat_dot(self, velocity, angular_velocity):  # may be better to put in smit, idk rn
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