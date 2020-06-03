"""
Functions to calculate torques acting on rocket
"""


def torque_normal(force_normal, x_bar, roll_axis, velocity):
    """
    :param force_normal: ndarray(double) normal force
    :param x_bar: distance between center of pressure and center of mass
    :param roll_axis: ndarray(double) direction of roll axis in reference frame
    :param velocity: ndarray(double) apparent velocity of the rocket
    :return: ndarray(double) the torque due to the normal force
    """
    return NotImplementedError

def torque_damping(damping_co, rot_matrix, m, omega):
    """
    :param damping_co: damping coefficient, FIXME calculate this
    :param rot_matrix: ndarray(double) rotation matrix
    :param m: diagonal matrix defined as [1, 1, 0] across the diagonal
    :param omega: ndarray(double) angular velocity of the rocket
    :return: adarray(double) the torque due to thrust damping
    """
    return NotImplementedError

def sum_torques(normal, damping):
    """
    :param normal: ndarray(double) torque due to normal force
    :param damping: ndarray(double) torque due to jet damping
    :return: ndarray(double) total torque
    """
    return NotImplementedError
