"""
Functions to calculate the forces acting on the rocket
"""
import numpy as np
from .eng import f50

def force_axial(velocity, aoa, mach, rey, roll_axis, abrakes):
    """
    :param velocity: ndarray(double) apparent velocity of the rocket
    :param aoa: current angle of attack of the rocket
    :param mach: current mach number of the rocket
    :param rey: current reynolds number
    :param roll_axis: ndarray(double) direction of the roll axis in the reference frame
    :return: the force acting on the roll axis of the rocket
    """
    
    # TODO this is an eyeball from solidworks data; improve this regression
    body_force = (3.9 / (60**2)) * velocity ** 2
    # TODO make airbrakes articulable
    abrake_force = np.sum((5.8/80) * (60 ** -2) * np.rad2deg(abrakes) * velocity**2)
    return np.array([0, 0, -(body_force + abrake_force)])

def force_normal(velocity, aoa, mach, rey, roll_axis):
    """
    :param velocity: ndarray(double) apparent velocity of the rocket
    :param aoa: current angle of attack of the rocket
    :param mach: current mach number of the rocket
    :param rey: current reynolds number
    :param roll_axis: ndarray(double) direction of the roll axis in the reference frame
    :return: the force acting perpendicular to the roll axis of the rocket
    """
    return np.array([0, 0, 0]) # TODO make it not a 1-D sim

def force_thrust(time):
    """
    :param time: current time
    :return: ndarray(double) the thrust force
    """
    return np.array([0, 0, f50(time)])

def force_gravity(altitude, mass):
    """"
    :param mass: mass of the rocket
    :param altitude: current altitude from sea level
    :return: ndarray(array) the gravitational force
    """
    g0 = 9.80665
    R_e = 6.3781e6
    return np.array([0, 0, mass * g0 * ((R_e / (R_e + altitude)) ** 2)])

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
