"""
Store the mathematical functions necessary for the calculations involved in the
simulation
"""

import numpy as np
from .envstate import EnvironmentState as es

def orien_in_ref(rot_matrix):
    """
    :param rot_matrix: ndarray(double) that describes the rotation in matrix form
    :return: ndarray(double) the axes of the rocket in the reference frame
    """
    yaw = np.dot(rot_matrix, es.ref_yaw)
    pitch = np.dot(rot_matrix, es.ref_pitch)
    roll = np.dot(rot_matrix, es.ref_roll)
    return np.array([yaw, roll, pitch])


def quat_dot(q, angular_velocity):  # may be better to put in smit, idk rn
    """
    :param q: a quaternion
    :param angular_velocity: ndarray(double) contains current angular velocity
    :return: ndarray(double) derivative of the quaternion describing orientation
    """
    s_dot = 0.5 * (np.vdot(q[:2], angular_velocity))
    v_dot = 0.5 * (np.add(q[3] * angular_velocity,
                   np.cross(q[:2], angular_velocity)))
    q_dot = np.array([v_dot, s_dot])
    return q_dot
