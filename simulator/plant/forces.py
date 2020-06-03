"""
Functions to recover the forces and torques acting on the rocket
"""

def force_axial(velocity, aoa, mach, rey, roll_axis):
    """
    :param velocity: ndarray(double) apparent velocity of the rocket
    :param aoa: current angle of attack of the rocket
    :param mach: current mach number of the rocket
    :param rey: current reynolds number
    :param roll_axis: ndarray(double) direction of the roll axis in the reference frame
    :return: the force acting on the roll axis of the rocket
    """
    return NotImplementedError

def force_normal(velocity, aoa, mach, rey, roll_axis):
    """
    :param velocity: ndarray(double) apparent velocity of the rocket
    :param aoa: current angle of attack of the rocket
    :param mach: current mach number of the rocket
    :param rey: current reynolds number
    :param roll_axis: ndarray(double) direction of the roll axis in the reference frame
    :return: the force acting perpendicular to the roll axis of the rocket
    """
    return NotImplementedError

def force_thrust(time):
    """
    :param time: current time
    :return: ndarray(double) the thrust force
    """
    return NotImplementedError

def force_gravity(altitude):
    """"
    :param altitude: current altitude from sea level
    :return: ndarray(array) the gravitational force
    """
    return NotImplementedError

def sum_forces(normal, axial, thrust, gravity):
    """
    :param normal: ndarray(double) normal force
    :param axial: ndarray(double) axial force
    :param thrust: ndarray(double) thrust force
    :param gravity: ndarray(double) gravitational force
    :return: ndarray(double) total force on the rocket
    could make these calls instead, just here for completeness
    """
    return NotImplementedError

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