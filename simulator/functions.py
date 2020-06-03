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


def rot_inert(mass):  # FIXME: needs to change as mass changes
    """
    :param mass: the current mass of the rocket
    :return: the rotational inertia tensor for the rocket
    """
    ixx = 60  # FIXME: not correct values
    iyy = 60
    izz = 60
    return np.array([[ixx, 0, 0],
                     [0, iyy, 0],
                     [0, 0, izz]])


def v_cm(wind, velocity):
    """
    :param wind: ndarray(double) vector for wind velocity
    :param velocity: ndarray(double) velocity of rocket without wind
    :return: ndarray(double) apparent velocity due to wind
    """
    return NotImplementedError


def v_omega(omega, roll_a, X_bar):
    """
    :param omega: ndarray(double) angular velocity vector
    :param roll_a: roll axis
    :param X_bar: distance between CM and CP
    :return: ndarray(double) apparent velocity due to angular velocity
    """
    return NotImplementedError


def reynolds(length, velocity, mu):
    """
    :param length: length of the rocket
    :param velocity: apparent velocity
    :param mu: kinematic viscosity
    :return: the current Reynolds Number
    """
    return NotImplementedError


def mu(temp_ground, temp_alt, C):
    """
    :param temp_ground: reference temperature
    :param temp_alt: temperature at current altitude
    :param C: Sutherland's Constant
    :return: the current kinetic viscosity
    """
    raise NotImplementedError


def mach_num(velocity, gamma, R, temp_alt):
    """
    :param velocity: apparent velocity of the rocket
    :param gamma: ratio of specific heats of air
    :param R: Reynold's Number
    :param temp_alt: temperature at the current altitude
    :return: the current Mach Number
    """
    return NotImplementedError
