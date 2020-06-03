"""
Functions to recover the forces acting on the rocket
"""

def force_axial(velocity, aoa, mach, rey, rot_matrix):
    """
    :param velocity: apparent velocity of the rocket
    :param aoa: current angle of attack of the rocket
    :param mach: current mach number of the rocket
    :param rey: current reynolds number
    :param rot_matrix: the rotation matrix of the current orientation
    :return: the force acting on the roll axis of the rocket
    """